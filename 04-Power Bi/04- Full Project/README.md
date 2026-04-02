# 04 — Full Project: Telecom churn (ETL + Power BI)

This module follows the walkthrough **[Introduction to Churn Analysis](https://www.youtube.com/watch?v=QFDslca5AX8)** (YouTube). The goal is an end-to-end **ETL in Microsoft SQL Server** and a **Power BI** dashboard on customer churn.

## Introduction to churn analysis

In competitive markets, **retaining customers** drives long-term results. **Churn analysis** uses customer data to find patterns and reasons behind attrition. Analytics and machine learning help predict who may leave and which factors matter, so the business can act early on satisfaction and loyalty.

Although the scenario is **telecom**, the same ideas apply to retail, finance, healthcare, and any industry that cares about retention.

## Data and resources

- **Video:** [Introduction to Churn Analysis](https://www.youtube.com/watch?v=QFDslca5AX8)
- **SSMS (SQL Server Management Studio):** [Download SSMS](https://learn.microsoft.com/en-us/sql/ssms/download-sql-server-management-studio-ssms?view=sql-server-ver16)
- **Theme colors (dashboard):**

  | Hex | Role (typical) |
  |-----|----------------|
  | `#4A44F2` | Primary accent |
  | `#9B9FF2` | Secondary / light accent |
  | `#F2F2F2` | Neutral background |
  | `#A0D1FF` | Highlight / chart fill |

- **Repo files:** `Customer_Data.csv` (source data), `SQLQuery1.sql` (exploration and ETL-style queries aligned with the lab). The Power BI **`.pbix`** may live only on your machine if you prefer not to commit binaries.

## Project target

1. **ETL in a database** and a **Power BI** report that uses customer data.
2. **Analyze** at least:
   - **Demographic** and **geographic**
   - **Payment & account** info
   - **Services**
3. **Profile churners** and spot areas for **marketing campaigns**.
4. **Approach to predict** future churners (method discussed in the video / course).

## Metrics required

| Metric | Definition (concept) |
|--------|----------------------|
| Total customers | Count of customers in scope |
| Total churn & churn rate | Churn count and churn ÷ total customers |
| New joiners | Customers with status “Joined” (or equivalent) |

---

## Step 1 — ETL in SQL Server

1. Install **SQL Server** and **SSMS**. Connect (note server name; use **Trust server certificate** if prompted).
2. Create database, e.g. `CREATE DATABASE db_Churn;`
3. **Import CSV** into a **staging** table (e.g. `stg_Churn`): Tasks → Import Flat File; set **`Customer_ID`** as primary key; allow nulls on other columns as needed; map **BIT** to **Varchar(50)** if the import wizard misbehaves.
4. **Explore:** distinct values for `Gender`, `Contract`, `Customer_Status`, `State`; null counts per column.
5. **Clean:** e.g. `ISNULL` / defaults for missing categories; load into **`prod_Churn`** (production table).
6. **Views for Power BI** (as in the video):
   - `vw_ChurnData` — rows where `Customer_Status` in `('Churned','Stayed')`
   - `vw_JoinData` — rows where `Customer_Status` = `'Joined'`

Your `SQLQuery1.sql` in this folder mirrors exploration and transformation patterns; align table names with your SSMS objects (`stg_Churn`, `prod_Churn`, etc.).

---

## Step 2 — Power Query (transform)

On the main fact table (e.g. `prod_Churn`):

1. **Churn Status** — `1` if `Customer_Status` = `"Churned"`, else `0`; type = whole number.
2. **Monthly Charge Range** — e.g. `< 20`, `20-50`, `50-100`, `> 100` from `Monthly_Charge`.

**Reference tables / bins:**

- **`mapping_AgeGrp`:** distinct `Age`, **Age Group** bands (e.g. `< 20`, `20 – 35`, `36 – 50`, `> 50`), **AgeGrpSorting** (1–4).
- **`mapping_TenureGrp`:** distinct `Tenure_in_Months`, **Tenure Group** (e.g. `< 6 Months` … `>= 24 Months`), **TenureGrpSorting** (1–5).
- **`prod_Services`:** unpivot service columns → **Services** (attribute) and **Status** (value).

---

## Step 3 — DAX measures (examples)

| Measure | Idea |
|---------|------|
| Total Customers | `COUNTROWS` / `DISTINCTCOUNT` on `Customer_ID` |
| New Joiners | `CALCULATE(..., Customer_Status = "Joined")` |
| Total Churn | `SUM` of **Churn Status** (or equivalent) |
| Churn Rate | `[Total Churn] / [Total Customers]` |

---

## Step 4 — Report pages and visuals

### Summary page

1. **Cards:** Total Customers, New Joiners, Total Churn, Churn Rate %.
2. **Demographic:** Gender → churn rate; Age Group → total customers & churn rate.
3. **Account:** Payment Method, Contract, Tenure Group → churn rate / volumes as specified.
4. **Geographic:** Top states by churn rate (e.g. top 5).
5. **Churn distribution:** Churn Category → total churn; **tooltip** with Churn Reason.
6. **Services:** Internet Type → churn rate; unpivoted services → **Services × Status** vs churn.

### Churn Reason page

- Use as **tooltip** or detail page: **Churn Reason** vs total churn.

---

## Related work elsewhere in the repo

- **Lab 3 (AdventureWorks):** [`../03- Direct Query/README.md`](../03-%20Direct%20Query/README.md)
- **Capstone “Final Project”** (if present): see `Final Project/` at repository root — separate from this Power BI churn folder.

Parent index: [`../README.md`](../README.md).
