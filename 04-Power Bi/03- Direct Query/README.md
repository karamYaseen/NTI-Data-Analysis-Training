# Lab 3 only — `04-Power Bi/03- Direct Query/`

Everything for **NTI Power BI Lab 3** (AdventureWorks) is **here**. This is **not** the capstone **Final Project** at the repo root.

## Files

| File | Use |
|------|-----|
| **`Lab 3.txt`** | Instructor brief (tables, visuals, hints) |
| **`lab3.pbix`** | Your report — save here if you use this folder |
| **`AdventureWorks2019.bak`** | Optional local restore — restore in SSMS, then **DirectQuery** from Power BI |

If you add sectioned backgrounds or a fill-in checklist, you can place **`assets/`** images and **`DASHBOARD_FILL_IN.md`** here and link them from your notes.

## SQL + Power BI reminder

- **DirectQuery** to AdventureWorks **OLTP** (e.g. `Sales.SalesOrderHeader`).
- Card measures should match **SSMS** aggregates on the same table/columns.
- **OrderDate** / **ShipDate** / **DueDate** → one active relationship to `DimDates`; use **`USERELATIONSHIP`** in measures for non-active date roles.

Parent overview: [`../README.md`](../README.md).
