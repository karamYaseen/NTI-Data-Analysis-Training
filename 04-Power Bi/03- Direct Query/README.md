# 03 — Lab 3 (AdventureWorks DirectQuery)

**Database:** AdventureWorks **OLTP** in SQL Server — restore from [AdventureWorks sample databases](https://learn.microsoft.com/en-us/sql/samples/adventureworks-install-configure?view=sql-server-ver16&tabs=ssms) (large `.bak` files stay local; not in this repo).

**Tools:** [Power BI Desktop](https://powerbi.microsoft.com/desktop/) · [SSMS](https://learn.microsoft.com/en-us/sql/ssms/download-sql-server-management-studio-ssms?view=sql-server-ver16) (check numbers vs the report)

**Typical files:** your lab `.pbix` (any name you use in class).

**Scope:** Lab 3 only — **not** the repo root **`Final Project/`** capstone.

## Tasks — Environment

- [ ] SQL Server + SSMS installed; AdventureWorks restored and reachable.

## Tasks — Power BI connection

- [ ] New report → **DirectQuery** into AdventureWorks OLTP (this lab expects DirectQuery, not a pure Import workflow).

## Tasks — Tables (minimum)

- [ ] `Sales.SalesOrderHeader`, `Sales.SalesOrderDetail`, `Sales.vSalesPerson`, `Sales.SalesTerritory`, `Purchasing.ShipMethod`, `Production.Product`, `Production.ProductSubcategory`, `Production.ProductCategory`

## Tasks — Power Query

- [ ] Rename tables/columns; drop unused columns.
- [ ] **Status** aligned with `ufnGetSalesOrderStatusText` (or equivalent).
- [ ] **Dates** table or logic as your model needs.
- [ ] Merge **Product** + **Subcategory** + **Category** → one table: **ProductID**, **Product**, **SubCategory**, **Category**.
- [ ] **TotalDue**, **Tax**, **Freight** — Power Query or DAX per brief.

## Tasks — Model

- [ ] Star schema + **product hierarchy**.
- [ ] One **active** date relationship from the fact to your calendar table; **OrderDate** / **ShipDate** / **DueDate** handled with **`USERELATIONSHIP`** for inactive roles ([Radacad](https://radacad.com/userelationship-or-role-playing-dimension-dealing-with-inactive-relationships-in-power-bi)).

## Tasks — DAX

- [ ] Measures: # Orders, Total SubTotal, Total Tax, Total Freight, Total Due, # Qty — in a **measures table**.

## Tasks — Report

- [ ] Drill down, drillthrough, **tooltip** page.
- [ ] Cards: # Orders, Total SubTotal, Total Tax, Total Freight, Total Due.
- [ ] # Orders by **OrderDate** vs **ShipDate** vs **DueDate** (role-playing pattern).
- [ ] # Orders by Status; by ShipMethod; Qty by Category → SubCategory → Product; online/offline if present; Orders vs TotalDue by Territory; top 10 salespeople (filters as needed).

## Tasks — QA

- [ ] Card measures match **SSMS** on the same tables/columns.
- [ ] Clean layout, colors, **meaningful chart titles**.

Parent: [`../README.md`](../README.md)
