# DirectQuery Lab 3 — my AdventureWorks report

**My NTI coursework** — **Karam Yaseen.** **What I set out to do:** **DirectQuery** to **my** SQL Server instance, a lean model, **role-playing dates** as the lab demanded, and **my** drill-down sales story.

---

## Quick start (my setup)

1. [SQL Server](https://www.microsoft.com/sql-server/sql-server-downloads) + [SSMS](https://learn.microsoft.com/en-us/sql/ssms/download-sql-server-management-studio-ssms?view=sql-server-ver16) on **my** machine.
2. **I** restore **AdventureWorks2019** OLTP via [Microsoft’s docs](https://learn.microsoft.com/en-us/sql/samples/adventureworks-install-configure?view=sql-server-ver16&tabs=ssms) — no `.bak` in this repo (gitignored).
3. Power BI → SQL Server → **DirectQuery** — **my** connection string, **my** database.
4. Tables, relationships, DAX, pages on `assets/directquery_canvas_main.png` — **my** build.

**What I produced:** `Sales Performance Analysis.pbix`, optional `Sales Performance Analysis.png`.

**Assets**

- `assets/directquery_canvas_main.png` — minimal canvas background  
- Optional: `assets/directquery_EXPECTED_main.png` (layout mockup only)  
- Filenames use the **directquery_** prefix so graphics stay neutral (no “Lab 3” text baked into images).

**My checklist:** load the tables **my** brief listed; measures for orders, amounts, quantity; spot-check vs SSMS; **USERELATIONSHIP** where **I** needed role-playing dates.

---

## What this lab was about (for me)

**I** built sales analytics on a real OLTP schema — orders, lines, products, territories — with **live** DirectQuery against **my** SQL Server.

---

## Dataset

**Database:** AdventureWorks **2019** OLTP on **my** SQL Server (local / lab — wherever **I** hosted it).

**Key tables I used:** `Sales.SalesOrderHeader`, `Sales.SalesOrderDetail`, `Sales.SalesPerson` / `Sales.vSalesPerson` (per **my** brief), `Sales.SalesTerritory`, `Purchasing.ShipMethod`, `Production.Product`, `Production.ProductSubcategory`, `Production.ProductCategory`

**Measures / facts:** order counts; `SubTotal`, `TaxAmt`, `Freight`, `TotalDue`; line `OrderQty` — **I** matched **my** assignment brief.

**Resources:** [AdventureWorks install](https://learn.microsoft.com/en-us/sql/samples/adventureworks-install-configure?view=sql-server-ver16&tabs=ssms) · [SSMS](https://learn.microsoft.com/en-us/sql/ssms/download-sql-server-management-studio-ssms?view=sql-server-ver16) · [USERELATIONSHIP / role-playing dates](https://radacad.com/userelationship-or-role-playing-dimension-dealing-with-inactive-relationships-in-power-bi)

---

## What I walked through

| Phase | What I did |
|-------|------------|
| **Environment** | SQL Server + SSMS; **my** AdventureWorks restore |
| **Connection** | DirectQuery to **my** database (not Import) |
| **Tables** | **I** loaded what **I** needed; hid the rest |
| **Power Query** | Names/types/merges **I** kept minimal for DirectQuery |
| **Model** | Star schema; hierarchy; dates + **USERELATIONSHIP** **my** lab needed |
| **DAX** | Orders, money, quantity — **my** measures table |
| **Report** | Cards, trends, drill, tooltips, slicers — **my** pages |
| **QA** | **I** checked totals vs SSMS on the same filters |

**Previous:** [`../02- Modeling/README.md`](../02-%20Modeling/README.md) · **Next:** [`../04- Full Project/README.md`](../04-%20Full%20Project/README.md)

**Author:** Karam Yaseen — **my** Lab 3, **my** build.

**Parent:** [`../README.md`](../README.md)
