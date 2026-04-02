# Power BI — Data Visualization & Modeling

Hands-on Power BI Desktop work: Kickstarter analytics, e‑commerce modeling, AdventureWorks DirectQuery (Lab 3), and a telecom **churn analysis** full project aligned with the course video.

**Folder names** use spaces after the number (e.g. `02- Modeling`, `03- Direct Query`). In links, use `%20` for spaces where needed.

---

## Topics covered

### 1. Basic Dashboard — Kickstarter (`01-Basic-Dashboard/`)

- CSV import and shaping for reporting
- KPIs, trends, categories, filters, one-page story

### 2. Data modeling — E‑commerce sales (`02- Modeling/`)

- Relationships, facts/dimensions, DAX measures
- Sales-focused dashboard (typically `E-Commerce Sales.pbix` and `Sales.xlsx` alongside this module)

### 3. Lab 3 — AdventureWorks DirectQuery (`03- Direct Query/`)

- SQL Server **AdventureWorks OLTP**, **DirectQuery**, star schema, DAX
- Role-playing dates (Order / Ship / Due) with **`USERELATIONSHIP`**
- See [`03- Direct Query/README.md`](03-%20Direct%20Query/README.md) — `Lab 3.txt`, AdventureWorks **DirectQuery**, SSMS checks

> **Scope:** Lab 3 only. Not the capstone **Final Project** in `Final Project/` at repo root.

### 4. Full project — Churn analysis (`04- Full Project/`)

- ETL in **SQL Server** (`db_Churn`, staging → production, views) + **Power BI** churn dashboard
- Spec, colors, measures, and visuals follow: [Introduction to Churn Analysis](https://www.youtube.com/watch?v=QFDslca5AX8)
- See [`04- Full Project/README.md`](04-%20Full%20Project/README.md)

---

## Projects in this folder

| Folder | Focus | Key files (in repo or local) |
|--------|--------|------------------------------|
| `01-Basic-Dashboard/` | Kickstarter analytics | `Kickstarter-Projects-Data/*.csv`; dashboard `.pbix` / screenshot may be local |
| `02- Modeling/` | E‑commerce sales model | `README.md`; `.pbix` / `Sales.xlsx` often kept locally |
| `03- Direct Query/` | Lab 3 AdventureWorks | `Lab 3.txt`, `README.md`; restore AdventureWorks in SSMS (see that README) |
| `04- Full Project/` | Telecom churn ETL + BI | `Customer_Data.csv`, `SQLQuery1.sql`, `README.md`; churn `.pbix` may be local |

---

## Requirements

- [Power BI Desktop](https://powerbi.microsoft.com/desktop/) (Windows)
- For Lab 3: SQL Server + [SSMS](https://learn.microsoft.com/en-us/sql/ssms/download-sql-server-management-studio-ssms?view=sql-server-ver16), restore AdventureWorks
- For churn project: SQL Server + SSMS per [`04- Full Project/README.md`](04-%20Full%20Project/README.md)

### Data path note (Kickstarter)

The CSV folder is `01-Basic-Dashboard/Kickstarter-Projects-Data/`. If refresh fails, use **Transform data → Data source settings** and point to that folder.

---

## Learning objectives

- Import and transform CSV/Excel in Power Query
- Build interactive dashboards with filters and visuals
- Model relationships and measures for business questions
- Use DirectQuery against SQL Server where appropriate
- Run an end-to-end churn pipeline: database ETL + Power BI

## Author

Karam Yaseen
