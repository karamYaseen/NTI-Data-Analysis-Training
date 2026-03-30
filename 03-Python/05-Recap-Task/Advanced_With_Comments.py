# Advanced.py — With Detailed Comments and Improvement Points
# This version includes inline comments explaining every section, especially Tasks B, C, and Bonus (2,3,5)
# At the end: specific points to improve these tasks

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

# ---------------------------------------------------------------------------  # Section divider for imports
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

import os  # For environment variables and file operations
import re  # For regex pattern matching
import ssl  # For secure email connections
import smtplib  # For sending emails
from email.message import EmailMessage  # To construct email messages
from pathlib import Path  # For cross-platform file paths

import pandas as pd  # Data manipulation and I/O
import pyodbc  # SQL Server connectivity
import requests  # HTTP requests for web scraping
from bs4 import BeautifulSoup  # HTML parsing

# ---------------------------------------------------------------------------  # Section divider for file paths
# WHERE FILES LIVE (folder next to this script)
# ---------------------------------------------------------------------------
try:
    base = Path(__file__).resolve().parent  # Get the directory of this script
except NameError:
    base = Path.cwd()  # Fallback to current working directory

# Define paths for input/output files relative to script location
sample_text = base / "sample_text.txt"   # Input: text for regex (Part C2)
sample_xlsx = base / "sample.xlsx"      # Input: Excel for cleaning (Part C3)
scraped_csv = base / "scraped_data.csv"  # Output: web scraping results (Part C1)
cleaned_xlsx = base / "cleaned_file.xlsx"  # Output: cleaned Excel (Part C3)
combined_csv = base / "combined_report.csv"  # Output: combined pipeline data

# ---------------------------------------------------------------------------  # Section divider for database connection
# SQL SERVER CONNECTION STRING
# ---------------------------------------------------------------------------
# You can set ONE full string in env var MSSQL_CONN_STR, OR set pieces:
# MSSQL_SERVER, MSSQL_DATABASE, and (optional) MSSQL_USER + MSSQL_PASSWORD.
# If no SQL user/password → Windows login (Trusted_Connection=yes).

if os.getenv("MSSQL_CONN_STR"):  # Check if full connection string is provided
    _cs = os.environ["MSSQL_CONN_STR"]  # Use the full string
else:  # Build connection string from individual environment variables
    _drv = os.getenv("MSSQL_DRIVER", "ODBC Driver 17 for SQL Server")  # Default driver
    _srv = os.getenv("MSSQL_SERVER", r"localhost\SQLEXPRESS")  # Default server
    _dbn = os.getenv("MSSQL_DATABASE", "company")  # Default database
    if os.getenv("MSSQL_USER"):  # If username provided, use SQL authentication
        _cs = (
            f"DRIVER={{{_drv}}};SERVER={_srv};DATABASE={_dbn};"
            f"UID={os.environ['MSSQL_USER']};PWD={os.environ['MSSQL_PASSWORD']};"
        )
    else:  # Otherwise, use Windows authentication
        _cs = (
            f"DRIVER={{{_drv}}};SERVER={_srv};DATABASE={_dbn};Trusted_Connection=yes;"
        )

conn = pyodbc.connect(_cs, timeout=20)  # Connect to SQL Server with 20s timeout
cur = conn.cursor()  # Create cursor for executing SQL commands
print("Database: SQL Server (SSMS)")  # Confirm connection


def get_high_salary_employees(conn, min_salary=7000):  # Function for Task B
    """
    Assignment Part B: return only rows where salary is above min_salary,
    sorted from highest salary to lowest. Pandas runs the SQL for us.
    The ? is a placeholder for min_salary (safe from SQL injection).
    """
    q = "SELECT * FROM employees WHERE salary > ? ORDER BY salary DESC"  # Parameterized query
    return pd.read_sql(q, conn, params=(min_salary,))  # Execute and return DataFrame


# ##########################################################################  # Task A: Basic SQL setup
# TASK A — BASIC (SQL + Pandas)
# ##########################################################################
# Goal: create two tables, fill them with sample rows, then run SELECT
# and load the result into a DataFrame and show the first 5 rows.
#
# employees:  id, name, department, salary
# departments: department, manager  (one row per department)

cur.execute("DROP TABLE IF EXISTS employees;")  # Remove table if exists
cur.execute("DROP TABLE IF EXISTS departments;")  # Remove table if exists
cur.execute(  # Create employees table
    """
    CREATE TABLE employees (
        id INT NOT NULL PRIMARY KEY,
        name NVARCHAR(255) NOT NULL,
        department NVARCHAR(255) NOT NULL,
        salary FLOAT NOT NULL
    );
    """
)
cur.execute(  # Create departments table
    """
    CREATE TABLE departments (
        department NVARCHAR(255) NOT NULL PRIMARY KEY,
        manager NVARCHAR(255) NOT NULL
    );
    """
)

# Insert many rows at once (10 employees + 4 departments)
cur.executemany(  # Bulk insert employees
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
cur.executemany(  # Bulk insert departments
    "INSERT INTO departments (department, manager) VALUES (?,?)",
    [
        ("IT", "Susan Li"),
        ("Finance", "David Long"),
        ("HR", "Lina Noor"),
        ("Marketing", "Mona Kareem"),
    ],
)
conn.commit()  # Save all changes to database

# Read whole employees table into a DataFrame = table in Python
df_all = pd.read_sql("SELECT * FROM employees", conn)  # Query all employees
print(df_all.head(5))  # Show first 5 rows


# ##########################################################################  # Task B: Intermediate operations (Point 2)
# TASK B — INTERMEDIATE (filter + function + merge)
# ##########################################################################
# 1) Only employees with salary > 7000, sorted by salary (function above).
# 2) Load employees and departments again into two DataFrames.
# 3) merge on "department" so each employee row gets the right manager.

df_high = get_high_salary_employees(conn, min_salary=7000)  # Call function for filtered data
print(df_high)  # Display high salary employees

df_emp = pd.read_sql("SELECT * FROM employees", conn)  # Load employees table
df_dept = pd.read_sql("SELECT * FROM departments", conn)  # Load departments table
df_merged = pd.merge(df_emp, df_dept, on="department", how="left")  # Left join on department
print(df_merged[["name", "department", "salary", "manager"]].head())  # Show selected columns


# ##########################################################################  # Task C Part 1: Web scraping (Point 3)
# TASK C — PART 1: WEB SCRAPING (requests + BeautifulSoup)
# ##########################################################################
# We download the books page, find each book "card" in the HTML,
# pull title, price, availability, put them in a list of dicts,
# then build a DataFrame and save CSV.

url = "http://books.toscrape.com/"  # Target website
r = requests.get(url, timeout=25, headers={"User-Agent": "Mozilla/5.0"})  # Download page
r.raise_for_status()  # Raise error if request failed
soup = BeautifulSoup(r.text, "html.parser")  # Parse HTML
books = soup.find_all("article", class_="product_pod")  # Find all book elements
rows = []  # List to store extracted data
for book in books[:20]:  # Process first 20 books
    title = book.h3.a["title"]  # Extract title
    price = book.find("p", class_="price_color").text.strip()  # Extract price
    extra = book.find("p", class_="instock availability").text.strip()  # Extract availability
    rows.append({"Title": title, "Price": price, "Extra": extra})  # Add to list
df_scrape = pd.DataFrame(rows)  # Create DataFrame from list of dicts
print(df_scrape.head())  # Show first few rows
df_scrape.to_csv(scraped_csv, index=False, encoding="utf-8-sig")  # Save to CSV


# ##########################################################################  # Task C Part 2: Regex (Point 3)
# TASK C — PART 2: REGEX (read sample_text.txt)
# ##########################################################################
# re.findall(pattern, text) returns all matches as a list.
# Email pattern: characters @ domain . ending
# Numbers: \d+ means one or more digits (2024, 1500, 30, ...)

text = sample_text.read_text(encoding="utf-8")  # Read text file
emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)  # Find emails
numbers = re.findall(r"\d+", text)  # Find numbers
print("Emails found:", emails)  # Display emails
print("Numbers found:", numbers)  # Display numbers


# ##########################################################################  # Task C Part 3: Excel automation (Point 3)
# TASK C — PART 3: AUTOMATION (Excel cleaning — Option 1)
# ##########################################################################
# Drop completely empty rows/columns, make column names lowercase with underscores,
# save as a new Excel file.

if sample_xlsx.is_file():  # Check if Excel file exists
    df_x = pd.read_excel(sample_xlsx)  # Load Excel into DataFrame
    df_x = df_x.dropna(how="all").dropna(axis=1, how="all")  # Remove empty rows/columns
    df_x.columns = [str(c).strip().lower().replace(" ", "_") for c in df_x.columns]  # Clean column names
    df_x.to_excel(cleaned_xlsx, index=False)  # Save cleaned Excel
else:
    print("sample.xlsx not found, skipped Excel step.")  # Skip if file missing


# ##########################################################################  # Bonus: Pipeline (Point 5)
# BONUS: PIPELINE (SQL + web data + combined CSV + optional email)
# ##########################################################################
# 1) Run a SQL query that joins employees with departments (already in Task A/B).
# 2) Take the same number of rows from SQL and from scraped books (side by side).
# 3) concat puts columns next to each other; sql_ and web_ prefixes avoid name clashes.
# 4) Save CSV. If SMTP_* env vars are set, email that CSV as attachment.

df_sql = pd.read_sql(  # Query joined employee and department data
    """
    SELECT e.name, e.department, e.salary, d.manager
    FROM employees e
    LEFT JOIN departments d ON e.department = d.department
    """,
    conn,
)
n = min(len(df_sql), len(df_scrape))  # Get minimum length to match rows
part_sql = df_sql.head(n).reset_index(drop=True)  # Take first n rows from SQL
part_web = df_scrape.head(n).reset_index(drop=True)  # Take first n rows from web
pipeline_df = pd.concat([part_sql.add_prefix("sql_"), part_web.add_prefix("web_")], axis=1)  # Combine side-by-side
pipeline_df = pipeline_df.dropna(axis=1, how="all")  # Remove any all-NaN columns
pipeline_df.to_csv(combined_csv, index=False, encoding="utf-8-sig")  # Save combined CSV

smtp_user = os.getenv("SMTP_USER")  # Check if email is configured
if smtp_user:  # If email env vars are set
    msg = EmailMessage()  # Create email message
    msg["Subject"] = "Daily Automated Report"  # Set subject
    msg["From"] = os.environ["EMAIL_FROM"]  # Set sender
    msg["To"] = os.environ["EMAIL_TO"]  # Set recipient
    msg.set_content("Pipeline output attached.")  # Set body
    msg.add_attachment(  # Attach the CSV file
        combined_csv.read_bytes(),
        maintype="application",
        subtype="octet-stream",
        filename=combined_csv.name,
    )
    ctx = ssl.create_default_context()  # Create secure context
    with smtplib.SMTP(os.environ["SMTP_HOST"], int(os.environ["SMTP_PORT"])) as s:  # Connect to SMTP server
        s.starttls(context=ctx)  # Start TLS encryption
        s.login(smtp_user, os.environ["SMTP_PASSWORD"])  # Login
        s.send_message(msg)  # Send email
    print("Email sent: combined_report.csv attached.")  # Confirm sent
else:
    print("Email skipped (set SMTP_USER, SMTP_PASSWORD, SMTP_HOST, SMTP_PORT, EMAIL_FROM, EMAIL_TO).")  # Skip email

print("Pipeline executed successfully.")  # Confirm completion
conn.close()  # Close database connection

# ---------------------------------------------------------------------------  # Optional scheduling section
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

# =============================================================================
# IMPROVEMENT POINTS FOR TASKS 2, 3, 5 (B, C, BONUS)
# =============================================================================

# TASK B (Point 2) — INTERMEDIATE IMPROVEMENTS:
# 1. Add error handling: try-except around pd.read_sql in case of connection issues
# 2. Make min_salary configurable via command line argument (argparse)
# 3. Add data validation: check if tables exist before merging
# 4. Include more merge options: inner join, outer join with explanation
# 5. Add logging: use logging module to track operations instead of print

# TASK C (Point 3) — WEB SCRAPING + REGEX + EXCEL IMPROVEMENTS:
# 1. Web scraping: Add retry logic for failed requests (requests.adapters)
# 2. Web scraping: Handle rate limiting with time.sleep() between requests
# 3. Web scraping: Add user-agent rotation to avoid blocking
# 4. Regex: Make patterns more robust (e.g., handle international domains)
# 5. Regex: Add case-insensitive matching option
# 6. Excel: Add data type validation before cleaning
# 7. Excel: Handle large files with chunking (pd.read_excel with chunksize)
# 8. Excel: Add progress bars for long operations (tqdm)

# BONUS (Point 5) — PIPELINE IMPROVEMENTS:
# 1. Add configuration file (config.json) for all settings instead of env vars
# 2. Implement proper logging with timestamps and log levels
# 3. Add data quality checks: validate row counts, check for duplicates
# 4. Make pipeline modular: separate functions for each step
# 5. Add error recovery: save intermediate results on failure
# 6. Email: Add HTML email template instead of plain text
# 7. Email: Add multiple recipients and CC options
# 8. Add monitoring: send alerts if pipeline fails or data is empty
# 9. Add testing: unit tests for each component
# 10. Add scheduling: proper cron job setup with error handling