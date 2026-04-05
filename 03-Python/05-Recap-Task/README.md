# Advanced Data Tools & Automation — my Session 7 recap

**My NTI coursework** — **Karam Yaseen.** **I** tied together SQL from Python, Pandas, scraping (requests + BeautifulSoup), regex, and small automation — **my** recap assignment and notes.

## Topics Covered

### 1. SQL + Pandas
- **SQL Server (SSMS)**: `Advanced.py` connects with **pyodbc** (ODBC Driver 17 for SQL Server). Create an empty database in SQL Server Management Studio first (e.g. `company`), then set env vars (see below) or `MSSQL_CONN_STR`.
- **Tables**: `employees` (id, name, department, salary) and `departments` (department, manager)
- **Queries**: `SELECT`, `WHERE`, `ORDER BY`, loading results with `pandas.read_sql`
- **Merge**: Joining employee and department data on `department`

### 2. Web scraping
- **HTTP**: `requests` to fetch a page
- **Parsing**: `BeautifulSoup` to read HTML (example: books.toscrape.com)
- **Output**: DataFrame and `scraped_data.csv`

### 3. Regular expressions
- **Emails**: Pattern for addresses in text
- **Numbers**: Digit sequences in `sample_text.txt`
- **Results**: Python lists (`emails`, `numbers`)

### 4. Automation
- **Excel cleaning**: Load `sample.xlsx`, drop empty rows/columns, normalize column names, save `cleaned_file.xlsx`

### 5. Bonus pipeline (optional)
- Run SQL → scrape → combine → clean → `combined_report.csv`
- Optional email via `smtplib` when environment variables are set (see below)

## Files in This Folder

- `README.md` - This documentation file
- `recap_advanced_guide.py` - Topic-by-topic reference (same style as earlier day guides)
- `Advanced.py` - Assignment solution: tasks A–C and bonus
- `session7_assignment.ipynb` - Notebook version of the assignment
- `sample_text.txt` - Text for regex exercises
- `sample.xlsx` - Sample Excel for automation task
- `.gitignore` - Ignores generated outputs (`scraped_data.csv`, `cleaned_file.xlsx`, `combined_report.csv`)

Generated when you run `Advanced.py` (not always tracked in git): `scraped_data.csv`, `cleaned_file.xlsx`, `combined_report.csv`

## Learning Objectives

After completing this section, you should be able to:

- Connect to SQL Server (SSMS), create tables, insert data, and query from Python
- Load SQL results into Pandas and merge DataFrames
- Scrape a public page with requests + BeautifulSoup and export CSV
- Use `re` to extract emails and numbers from text files
- Clean Excel files programmatically and save a cleaned workbook
- Outline a multi-step pipeline and optional scheduling (Task Scheduler / cron / `schedule`)

## How to Run

1. Open a terminal in this folder (or use your IDE terminal).
2. Create a virtual environment (recommended) and install dependencies:

```bash
pip install pandas requests beautifulsoup4 openpyxl lxml pyodbc
```

3. **SQL Server**: Install [ODBC Driver 17 for SQL Server](https://learn.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server). Create a database in SSMS. Then either set a full connection string:

```text
set MSSQL_CONN_STR=DRIVER={ODBC Driver 17 for SQL Server};SERVER=YOUR_PC\SQLEXPRESS;DATABASE=company;Trusted_Connection=yes;
```

Or use separate variables: `MSSQL_SERVER`, `MSSQL_DATABASE`, and optionally `MSSQL_USER` / `MSSQL_PASSWORD` (otherwise Windows auth). Override driver with `MSSQL_DRIVER` if needed.

4. Run the assignment script:

```bash
python Advanced.py
```

5. Optional — bonus email: set `SMTP_HOST`, `SMTP_PORT`, `SMTP_USER`, `SMTP_PASSWORD`, `EMAIL_FROM`, `EMAIL_TO` (and use an app password for Gmail). If unset, the script skips sending and prints a short notice.

6. Optional — daily schedule: use **Windows Task Scheduler** or **cron** to run `python Advanced.py` on a schedule, or install `schedule` and extend the script as described in your course notes.

## Required Libraries

- `pandas` — DataFrames and I/O
- `pyodbc` — SQL Server (SSMS) access
- `requests` — HTTP
- `beautifulsoup4` — HTML parsing
- `lxml` or `html.parser` — Parser backend for BeautifulSoup
- `openpyxl` — Read/write `.xlsx`
- `re`, `smtplib`, `ssl`, `os` — Standard library

**Parent:** [`../README.md`](../README.md) · **Previous:** [`../04-NumPy-Pandas-Plotting/README.md`](../04-NumPy-Pandas-Plotting/README.md) · **Next track:** [`../../04-Power Bi/README.md`](../../04-Power%20Bi/README.md)

## Author

Karam Yaseen
