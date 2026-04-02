# DirectQuery Module — Lab 3 (AdventureWorks)

Technical assessment: **Connect DirectQuery** to SQL Server, **shape data**, build **star schema**, create **DAX measures**, design **drill-down report**.

---

## Quick start

1. Install SQL Server + SSMS; restore AdventureWorks
2. Open Power BI Desktop
3. DirectQuery connection to database
4. Shape, model, build report

**Typical output:** Lab 3 `.pbix` file.

---

## Scenario

Analyze AdventureWorks sales data using DirectQuery: orders, products, territories, with role-playing dates.

---

## Dataset

**Database:** AdventureWorks OLTP (SQL Server)

**Key tables:** `Sales.SalesOrderHeader`, `Sales.SalesOrderDetail`, `Sales.vSalesPerson`, `Sales.SalesTerritory`, `Purchasing.ShipMethod`, `Production.Product`, `Production.ProductSubcategory`, `Production.ProductCategory`

**DAX / facts:** order counts; SubTotal, Tax, Freight, TotalDue, quantity (per lab).

**Resources:** [AdventureWorks (install)](https://learn.microsoft.com/en-us/sql/samples/adventureworks-install-configure?view=sql-server-ver16&tabs=ssms) · [SSMS](https://learn.microsoft.com/en-us/sql/ssms/download-sql-server-management-studio-ssms?view=sql-server-ver16) · [USERELATIONSHIP / role-playing dates](https://radacad.com/userelationship-or-role-playing-dimension-dealing-with-inactive-relationships-in-power-bi)

---

## Tasks

| Phase | Deliverables |
|-------|--------------|
| **Environment** | SQL Server + SSMS installed; AdventureWorks restored |
| **Connection** | DirectQuery to AdventureWorks OLTP |
| **Tables** | Load minimum required tables |
| **Power Query** | Rename, merge, status/dates logic |
| **Model** | Star schema + product hierarchy; USERELATIONSHIP for dates |
| **DAX** | Measures table: orders, totals, quantities |
| **Report** | Drill-down, tooltips, cards, trends by dates/status |
| **QA** | Match SSMS numbers; clean layout |

Parent: [`../README.md`](../README.md)
