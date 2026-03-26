# Session 7 — Advanced Data Tools & Automation
# Database: SQL Server only (SQL Server Management Studio / pyodbc).
#
# WHAT THIS SCRIPT DOES (big picture)
# -----------------------------------
# 1) Talks to your SQL Server database (tables + data).
# 2) Uses Pandas to read query results as tables (DataFrames).
# 3) Downloads a web page, pulls book data, saves CSV.
# 4) Reads a text file and finds emails + numbers with regex.
# 5) Cleans an Excel file and saves a new Excel file.
# 6) (Bonus) Combines SQL results + scraped data into one CSV, optionally emails it.

# ---------------------------------------------------------------------------
# IMPORTS — each library has one main job
# ---------------------------------------------------------------------------
# os          → read environment variables (passwords, SMTP settings, SQL connection)
# re          → "regular expressions" = patterns to find emails and numbers in text
# ssl         → secure connection when sending email
# smtplib     → send email from Python
# EmailMessage → build an email (subject, body, attachment)
# Path        → file paths that work on Windows/Linux (from pathlib)
# pandas      → tables in Python (called DataFrames), read/write SQL & CSV & Excel
# pyodbc      → connect Python to SQL Server (same idea as SSMS, but from code)
# requests    → download a web page (HTTP GET)
# BeautifulSoup → read HTML and find tags (title, price, etc.)

import os
import re
import ssl
import smtplib
from email.message import EmailMessage
from pathlib import Path

import pandas as pd
import pyodbc
import requests
from bs4 import BeautifulSoup

# ---------------------------------------------------------------------------
# WHERE FILES LIVE (folder next to this script)
# ---------------------------------------------------------------------------
try:
    base = Path(__file__).resolve().parent
except NameError:
    base = Path.cwd()

sample_text = base / "sample_text.txt"   # text for regex (Part C2)
sample_xlsx = base / "sample.xlsx"      # Excel input for cleaning (Part C3)
scraped_csv = base / "scraped_data.csv"  # output of web scraping (Part C1)
cleaned_xlsx = base / "cleaned_file.xlsx"  # output of Excel cleaning (Part C3)
combined_csv = base / "combined_report.csv"  # bonus pipeline output

# ---------------------------------------------------------------------------
# SQL SERVER CONNECTION STRING
# ---------------------------------------------------------------------------
# You can set ONE full string in env var MSSQL_CONN_STR, OR set pieces:
# MSSQL_SERVER, MSSQL_DATABASE, and (optional) MSSQL_USER + MSSQL_PASSWORD.
# If no SQL user/password → Windows login (Trusted_Connection=yes).

if os.getenv("MSSQL_CONN_STR"):
    _cs = os.environ["MSSQL_CONN_STR"]
else:
    _drv = os.getenv("MSSQL_DRIVER", "ODBC Driver 17 for SQL Server")
    _srv = os.getenv("MSSQL_SERVER", r"localhost\SQLEXPRESS")
    _dbn = os.getenv("MSSQL_DATABASE", "company")
    if os.getenv("MSSQL_USER"):
        _cs = (
            f"DRIVER={{{_drv}}};SERVER={_srv};DATABASE={_dbn};"
            f"UID={os.environ['MSSQL_USER']};PWD={os.environ['MSSQL_PASSWORD']};"
        )
    else:
        _cs = (
            f"DRIVER={{{_drv}}};SERVER={_srv};DATABASE={_dbn};Trusted_Connection=yes;"
        )

conn = pyodbc.connect(_cs, timeout=20)
cur = conn.cursor()
print("Database: SQL Server (SSMS)")


def get_high_salary_employees(conn, min_salary=7000):
    """
    Assignment Part B: return only rows where salary is above min_salary,
    sorted from highest salary to lowest. Pandas runs the SQL for us.
    The ? is a placeholder for min_salary (safe from SQL injection).
    """
    q = "SELECT * FROM employees WHERE salary > ? ORDER BY salary DESC"
    return pd.read_sql(q, conn, params=(min_salary,))


# ##########################################################################
# TASK A — BASIC (SQL + Pandas)
# ##########################################################################
# Goal: create two tables, fill them with sample rows, then run SELECT
# and load the result into a DataFrame and show the first 5 rows.
#
# employees:  id, name, department, salary
# departments: department, manager  (one row per department)

cur.execute("DROP TABLE IF EXISTS employees;")
cur.execute("DROP TABLE IF EXISTS departments;")
cur.execute(
    """
    CREATE TABLE employees (
        id INT NOT NULL PRIMARY KEY,
        name NVARCHAR(255) NOT NULL,
        department NVARCHAR(255) NOT NULL,
        salary FLOAT NOT NULL
    );
    """
)
cur.execute(
    """
    CREATE TABLE departments (
        department NVARCHAR(255) NOT NULL PRIMARY KEY,
        manager NVARCHAR(255) NOT NULL
    );
    """
)

# Insert many rows at once (10 employees + 4 departments)
cur.executemany(
    "INSERT INTO employees (id, name, department, salary) VALUES (?,?,?,?)",
    [
        (1, "John Miller", "IT", 7000),
        (2, "Sara White", "Finance", 8500),
        (3, "Omar Ali", "IT", 9000),
        (4, "Lina Noor", "HR", 6200),
        (5, "David Long", "Finance", 7200),
        (6, "Susan Li", "IT", 8800),
        (7, "Mona Kareem", "Marketing", 6900),
        (8, "Yousef Hani", "HR", 7100),
        (9, "Nadia Salem", "Finance", 9100),
        (10, "Karim Fadel", "Marketing", 7400),
    ],
)
cur.executemany(
    "INSERT INTO departments (department, manager) VALUES (?,?)",
    [
        ("IT", "Susan Li"),
        ("Finance", "David Long"),
        ("HR", "Lina Noor"),
        ("Marketing", "Mona Kareem"),
    ],
)
conn.commit()

# Read whole employees table into a DataFrame = table in Python
df_all = pd.read_sql("SELECT * FROM employees", conn)
print(df_all.head(5))


# ##########################################################################
# TASK B — INTERMEDIATE (filter + function + merge)
# ##########################################################################
# 1) Only employees with salary > 7000, sorted by salary (function above).
# 2) Load employees and departments again into two DataFrames.
# 3) merge on "department" so each employee row gets the right manager.

df_high = get_high_salary_employees(conn, min_salary=7000)
print(df_high)

df_emp = pd.read_sql("SELECT * FROM employees", conn)
df_dept = pd.read_sql("SELECT * FROM departments", conn)
df_merged = pd.merge(df_emp, df_dept, on="department", how="left")
print(df_merged[["name", "department", "salary", "manager"]].head())


# ##########################################################################
# TASK C — PART 1: WEB SCRAPING (requests + BeautifulSoup)
# ##########################################################################
# We download the books page, find each book "card" in the HTML,
# pull title, price, availability, put them in a list of dicts,
# then build a DataFrame and save CSV.

url = "http://books.toscrape.com/"
r = requests.get(url, timeout=25, headers={"User-Agent": "Mozilla/5.0"})
r.raise_for_status()
soup = BeautifulSoup(r.text, "html.parser")
books = soup.find_all("article", class_="product_pod")
rows = []
for book in books[:20]:
    title = book.h3.a["title"]
    price = book.find("p", class_="price_color").text.strip()
    extra = book.find("p", class_="instock availability").text.strip()
    rows.append({"Title": title, "Price": price, "Extra": extra})
df_scrape = pd.DataFrame(rows)
print(df_scrape.head())
df_scrape.to_csv(scraped_csv, index=False, encoding="utf-8-sig")


# ##########################################################################
# TASK C — PART 2: REGEX (read sample_text.txt)
# ##########################################################################
# re.findall(pattern, text) returns all matches as a list.
# Email pattern: characters @ domain . ending
# Numbers: \d+ means one or more digits (2024, 1500, 30, ...)

text = sample_text.read_text(encoding="utf-8")
emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
numbers = re.findall(r"\d+", text)
print("Emails found:", emails)
print("Numbers found:", numbers)


# ##########################################################################
# TASK C — PART 3: AUTOMATION (Excel cleaning — Option 1)
# ##########################################################################
# Drop completely empty rows/columns, make column names lowercase with underscores,
# save as a new Excel file.

if sample_xlsx.is_file():
    df_x = pd.read_excel(sample_xlsx)
    df_x = df_x.dropna(how="all").dropna(axis=1, how="all")
    df_x.columns = [str(c).strip().lower().replace(" ", "_") for c in df_x.columns]
    df_x.to_excel(cleaned_xlsx, index=False)
else:
    print("sample.xlsx not found, skipped Excel step.")


# ##########################################################################
# BONUS: PIPELINE (SQL + web data + combined CSV + optional email)
# ##########################################################################
# 1) Run a SQL query that joins employees with departments (already in Task A/B).
# 2) Take the same number of rows from SQL and from scraped books (side by side).
# 3) concat puts columns next to each other; sql_ and web_ prefixes avoid name clashes.
# 4) Save CSV. If SMTP_* env vars are set, email that CSV as attachment.

df_sql = pd.read_sql(
    """
    SELECT e.name, e.department, e.salary, d.manager
    FROM employees e
    LEFT JOIN departments d ON e.department = d.department
    """,
    conn,
)
n = min(len(df_sql), len(df_scrape))
part_sql = df_sql.head(n).reset_index(drop=True)
part_web = df_scrape.head(n).reset_index(drop=True)
pipeline_df = pd.concat([part_sql.add_prefix("sql_"), part_web.add_prefix("web_")], axis=1)
pipeline_df = pipeline_df.dropna(axis=1, how="all")
pipeline_df.to_csv(combined_csv, index=False, encoding="utf-8-sig")

smtp_user = os.getenv("SMTP_USER")
if smtp_user:
    msg = EmailMessage()
    msg["Subject"] = "Daily Automated Report"
    msg["From"] = os.environ["EMAIL_FROM"]
    msg["To"] = os.environ["EMAIL_TO"]
    msg.set_content("Pipeline output attached.")
    msg.add_attachment(
        combined_csv.read_bytes(),
        maintype="application",
        subtype="octet-stream",
        filename=combined_csv.name,
    )
    ctx = ssl.create_default_context()
    with smtplib.SMTP(os.environ["SMTP_HOST"], int(os.environ["SMTP_PORT"])) as s:
        s.starttls(context=ctx)
        s.login(smtp_user, os.environ["SMTP_PASSWORD"])
        s.send_message(msg)
    print("Email sent: combined_report.csv attached.")
else:
    print("Email skipped (set SMTP_USER, SMTP_PASSWORD, SMTP_HOST, SMTP_PORT, EMAIL_FROM, EMAIL_TO).")

print("Pipeline executed successfully.")
conn.close()

# ---------------------------------------------------------------------------
# OPTIONAL: run this script every morning (not executed — uncomment to try)
# ---------------------------------------------------------------------------
# pip install schedule
# import schedule
# import time
# import subprocess
# import sys
# def job():
#     subprocess.run([sys.executable, str(base / "Advanced.py")])
# schedule.every().day.at("08:00").do(job)
# while True:
#     schedule.run_pending()
#     time.sleep(60)
