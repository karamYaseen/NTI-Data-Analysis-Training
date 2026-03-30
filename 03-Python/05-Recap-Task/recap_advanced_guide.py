# Advanced Data Tools & Automation — Reference Guide
# Session 7 recap: SQL + Pandas, scraping, regex, automation
# Style aligned with 03-Functions-OOP (functions.py / oop.py)

# ===========================================
# WHY ADVANCED AUTOMATION MATTER
# ===========================================
# This session combines multiple technologies for real-world data workflows.
# Benefits:
# - SQL: Structured data storage and complex queries
# - Web scraping: Extract data from websites automatically
# - Regex: Pattern-based text processing
# - Excel automation: Programmatic spreadsheet handling
# - Email integration: Automated reporting
#
# Use cases:
# - Daily business reports (sales, inventory)
# - Data monitoring and alerting
# - ETL pipelines (Extract, Transform, Load)
# - Competitive intelligence gathering
# - Automated testing and validation
#
# Common pitfalls:
# - SQL injection (always use parameterized queries)
# - Web scraping blocks (respect robots.txt, add delays)
# - Regex complexity (test patterns thoroughly)
# - Email spam (use proper authentication, rate limiting)
# - File encoding issues (specify UTF-8)

# ===========================================
# PATHS AND BASE DIRECTORY
# ===========================================

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

# ===========================================
# SQL SERVER (SSMS) + PANDAS (pyodbc)
# ===========================================

# import os
# import pandas as pd
# import pyodbc
#
# cs = os.environ["MSSQL_CONN_STR"]  # or build SERVER / DATABASE / Trusted_Connection
# conn = pyodbc.connect(cs, timeout=20)
# df = pd.read_sql("SELECT * FROM employees", conn)
# conn.close()

# ===========================================
# FILTERED QUERY + FUNCTION PATTERN
# ===========================================

# def get_high_salary_employees(conn, min_salary=7000):
#     q = "SELECT * FROM employees WHERE salary > ? ORDER BY salary DESC"
#     return pd.read_sql(q, conn, params=(min_salary,))

# ===========================================
# MERGE TWO TABLES FROM SQL
# ===========================================

# df_emp = pd.read_sql("SELECT * FROM employees", conn)
# df_dept = pd.read_sql("SELECT * FROM departments", conn)
# merged = pd.merge(df_emp, df_dept, on="department", how="left")

# ===========================================
# REQUESTS + BEAUTIFULSOUP (SCRAPING)
# ===========================================

# import requests
# from bs4 import BeautifulSoup
#
# url = "http://books.toscrape.com/"
# r = requests.get(url, timeout=15)
# r.raise_for_status()
# soup = BeautifulSoup(r.text, "html.parser")

# ===========================================
# REGEX — EMAILS AND NUMBERS
# ===========================================

# import re
#
# text = (BASE_DIR / "sample_text.txt").read_text(encoding="utf-8")
# emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
# numbers = re.findall(r"\d+", text)

# ===========================================
# EXCEL CLEANING PATTERN
# ===========================================

# import pandas as pd
#
# df = pd.read_excel(BASE_DIR / "sample.xlsx")
# df = df.dropna(how="all").dropna(axis=1, how="all")
# df.columns = [str(c).strip().lower().replace(" ", "_") for c in df.columns]
# df.to_excel(BASE_DIR / "cleaned_file.xlsx", index=False)

# ===========================================
# OPTIONAL: SMTP (ENV VARS)
# ===========================================

# import os, smtplib, ssl
# from email.message import EmailMessage
#
# if os.getenv("SMTP_USER"):
#     msg = EmailMessage()
#     msg["Subject"] = "Daily Automated Report"
#     msg["From"] = os.environ["EMAIL_FROM"]
#     msg["To"] = os.environ["EMAIL_TO"]
#     msg.set_content("Report attached.")
#     context = ssl.create_default_context()
#     with smtplib.SMTP(os.environ["SMTP_HOST"], int(os.environ["SMTP_PORT"])) as s:
#         s.starttls(context=context)
#         s.login(os.environ["SMTP_USER"], os.environ["SMTP_PASSWORD"])
#         s.send_message(msg)
