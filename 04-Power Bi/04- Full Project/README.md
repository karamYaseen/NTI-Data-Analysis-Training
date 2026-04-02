# 04 — Full project: Telecom churn (ETL + Power BI)

**Walkthrough:** **[Introduction to Churn Analysis](https://www.youtube.com/watch?v=QFDslca5AX8)** (YouTube)

**Theme colors:** `#4A44F2`, `#9B9FF2`, `#F2F2F2`, `#A0D1FF`

**Tools:** [Power BI Desktop](https://powerbi.microsoft.com/desktop/) · SQL Server + [SSMS](https://learn.microsoft.com/en-us/sql/ssms/download-sql-server-management-studio-ssms?view=sql-server-ver16)

**Repo files:** `Customer_Data.csv`, `SQLQuery1.sql`

**Typical files:** your churn `.pbix` (local name is your choice).

**Scope:** Churn module in this folder — **not** Lab 3 (`03- Direct Query/`). Capstone: repo **`Final Project/`**.

## Tasks — SQL Server (ETL)

- [ ] Create database (e.g. `db_Churn`).
- [ ] Import CSV into **staging** (e.g. `stg_Churn`): primary key on **Customer_ID**; adjust types if the import wizard fails on BIT (e.g. use `VARCHAR(50)` where needed).
- [ ] Explore: distributions and **null counts** per column.
- [ ] Clean and load **production** table (e.g. `prod_Churn`) with `ISNULL` / defaults as in the video.
- [ ] Create views for Power BI, e.g. **`vw_ChurnData`** (`Customer_Status` in `Churned`, `Stayed`) and **`vw_JoinData`** (`Joined`).

## Tasks — Power Query

- [ ] **Churn Status** = 1 if churned, else 0; numeric type.
- [ ] **Monthly Charge Range** bands (`< 20`, `20–50`, `50–100`, `> 100`).
- [ ] **mapping_AgeGrp:** distinct ages → age groups + sort column.
- [ ] **mapping_TenureGrp:** tenure bins + sort column.
- [ ] **prod_Services:** unpivot service columns → **Services** / **Status**.

## Tasks — DAX

- [ ] Total Customers  
- [ ] New Joiners (status Joined)  
- [ ] Total Churn  
- [ ] Churn Rate = Total Churn ÷ Total Customers  

## Tasks — Report

**Summary page**

- [ ] Cards: Total Customers, New Joiners, Total Churn, Churn Rate %.
- [ ] Demographic: gender churn rate; age group — customers & churn rate.
- [ ] Account: payment method, contract, tenure group — churn metrics.
- [ ] Geographic: e.g. top states by churn rate.
- [ ] Churn category totals; **tooltip** with churn reasons.
- [ ] Services: internet type churn rate; unpivoted services vs churn.

**Churn reason**

- [ ] Page or tooltip: churn reason vs total churn.

**Related:** [`../03- Direct Query/README.md`](../03-%20Direct%20Query/README.md) (Lab 3).

Parent: [`../README.md`](../README.md)
