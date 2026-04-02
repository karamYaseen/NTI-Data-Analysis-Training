# 03 — Lab 3: AdventureWorks (DirectQuery)

**Not** the repo root **`Final Project/`** capstone.

**Setup**

- [ ] Install SQL Server and [SSMS](https://learn.microsoft.com/en-us/sql/ssms/download-sql-server-management-studio-ssms?view=sql-server-ver16).
- [ ] Restore **AdventureWorks** using Microsoft’s guide: [AdventureWorks sample databases](https://learn.microsoft.com/en-us/sql/samples/adventureworks-install-configure?view=sql-server-ver16&tabs=ssms) (`.bak` files are large and are not committed here).

**Connection**

- [ ] New Power BI report → **DirectQuery** to the **AdventureWorks OLTP** database (not Import-only for this lab).

**Tables to use (minimum)**

- [ ] `Sales.SalesOrderHeader`
- [ ] `Sales.SalesOrderDetail`
- [ ] `Sales.vSalesPerson` (view)
- [ ] `Sales.SalesTerritory`
- [ ] `Purchasing.ShipMethod`
- [ ] `Production.Product`
- [ ] `Production.ProductSubcategory`
- [ ] `Production.ProductCategory`

**Power Query**

- [ ] Rename tables and columns for clarity; remove unused columns.
- [ ] Add **Status** (from `ufnGetSalesOrderStatusText` logic or equivalent).
- [ ] Build **Dates** in Power Query as needed for the model.
- [ ] **Merge** `Product`, `ProductSubcategory`, `ProductCategory` into one table with **ProductID**, **Product**, **SubCategory**, **Category**.
- [ ] Solve **TotalDue**, **Tax**, and **Freight** in Power Query or DAX (as specified by your instructor).

**Model**

- [ ] **Star schema** + **product hierarchy**.
- [ ] One **active** relationship from the sales fact to your **calendar / date** table for the primary date role.
- [ ] **OrderDate**, **ShipDate**, **DueDate:** use **`USERELATIONSHIP`** in measures for the non-active date roles (see [Radacad: USERELATIONSHIP](https://radacad.com/userelationship-or-role-playing-dimension-dealing-with-inactive-relationships-in-power-bi)).
- [ ] Line charts: compare counts by **order date** vs **ship date** vs **due date** using the pattern above.

**Measures (DAX)**

- [ ] # Orders  
- [ ] Total SubTotal  
- [ ] Total Tax  
- [ ] Total Freight  
- [ ] Total Due  
- [ ] # Qty  
- [ ] Put all measures in a **dedicated measures table**.

**Visuals (use measures on visuals)**

- [ ] Drill down, drillthrough, **tooltip** page.
- [ ] Cards: # Orders, Total SubTotal, Total Tax, Total Freight, Total Due.
- [ ] # Orders by OrderDate vs ShipDate vs DueDate.
- [ ] # Orders by Status.
- [ ] # Orders by ShipMethod.
- [ ] Order Qty by Category → SubCategory → Product.
- [ ] # Orders by online/offline flag (if in model).
- [ ] Orders vs TotalDue by Territory.
- [ ] Top 10 sales persons (# Orders or total amount); use filter pane as needed.

**Quality**

- [ ] Card values **match SSMS** on the same tables/columns.
- [ ] Clear colors, layout, and **meaningful chart titles**.

Parent: [`../README.md`](../README.md)
