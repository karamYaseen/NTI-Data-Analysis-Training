# Lab 3 — AdventureWorks (Direct Query)

Everything for **NTI Power BI Lab 3** (AdventureWorks OLTP) lives in **`04-Power Bi/03- Direct Query/`**. This is **not** the capstone **Final Project** at the repo root.

## Files in this folder

| File | Purpose |
|------|---------|
| **`Lab 3.txt`** | Lab brief: tables, merges, measures, visuals, `USERELATIONSHIP` hint |
| **`README.md`** | This guide |

Your **`.pbix`** file is local (not always committed). Name it however your course requires (for example `lab3.pbix`).

## SQL Server database

- Install and connect with **[SQL Server Management Studio (SSMS)](https://learn.microsoft.com/en-us/sql/ssms/download-sql-server-management-studio-ssms?view=sql-server-ver16)**.
- Restore **AdventureWorks** from Microsoft’s sample databases: [AdventureWorks sample databases](https://learn.microsoft.com/en-us/sql/samples/adventureworks-install-configure?view=sql-server-ver16&tabs=ssms).
- Backup files (`.bak`) are **not** stored in this repository because they are large; download or restore using the official instructions above.

## Power BI connection

- Use **DirectQuery** (not Import) to the **AdventureWorks OLTP** database, as specified in **`Lab 3.txt`**.
- **Measures on card visuals** should match aggregates you verify in **SSMS** on the same tables and columns.
- **Order date, ship date, due date:** keep **one active relationship** from the fact table to your **calendar / date table**. For the other two date roles, use **`USERELATIONSHIP`** in measures (see the Radacad link in **`Lab 3.txt`**).

## Optional extras

If you use sectioned page backgrounds or a written checklist, you can add **`assets/`** (images) and **`DASHBOARD_FILL_IN.md`** in this folder yourself.

---

Parent overview: [`../README.md`](../README.md).
