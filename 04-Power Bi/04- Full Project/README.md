# Full Project Module — Telecom Churn Analysis

Technical assessment: **ETL in SQL Server**, **Power Query transformations**, **DAX measures**, build **churn dashboard** with demographics and insights.

---

## Quick start

1. Install SQL Server + SSMS
2. Create database, import `Customer_Data.csv`
3. Clean data, create views
4. Open Power BI, connect to views
5. Transform, model, build report

**Walkthrough:** [Introduction to Churn Analysis](https://www.youtube.com/watch?v=QFDslca5AX8) (YouTube)

**Theme colors:** `#4A44F2`, `#9B9FF2`, `#F2F2F2`, `#A0D1FF`

**Typical output:** Churn `.pbix` file.

---

## Scenario

Analyze telecom customer churn: ETL customer data, identify churn patterns, visualize demographics, accounts, services.

---

## Dataset

| File | Description |
|------|-------------|
| `Customer_Data.csv` | Telecom customer data |
| `SQLQuery1.sql` | Sample SQL for ETL |

**Key columns (match `Customer_Data.csv`):** Customer_ID, Gender, Age, Married, State, Number_of_Referrals, Tenure_in_Months, Value_Deal, Phone_Service, Multiple_Lines, Internet_Service, Internet_Type, Online_Security, Online_Backup, Device_Protection_Plan, Premium_Support, Streaming_TV, Streaming_Movies, Streaming_Music, Unlimited_Data, Contract, Paperless_Billing, Payment_Method, Monthly_Charge, Total_Charges, Total_Refunds, Total_Extra_Data_Charges, Total_Long_Distance_Charges, Total_Revenue, Customer_Status, Churn_Category, Churn_Reason

---

## Tasks

| Phase | Deliverables |
|-------|--------------|
| **SQL Server (ETL)** | Create DB, import CSV to staging, explore, clean to production, create views |
| **Power Query** | Churn status, charge ranges, age/tenure groups, unpivot services |
| **DAX** | Total Customers, New Joiners, Total Churn, Churn Rate |
| **Report** | Summary page: cards, demographics, accounts, geographic, services; Churn reason page/tooltip |

**Scope:** Churn module — not Lab 3. Capstone: `Final Project/`.

Parent: [`../README.md`](../README.md)
