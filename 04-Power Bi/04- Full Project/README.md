# Telecom churn — my Power BI full project

**My NTI coursework** — **Karam Yaseen.** **What I set out to do:** an **end-to-end BI mini-project** — **my** SQL Server ETL, **my** Power Query rules, **my** DAX, and **my** churn-focused dashboard.

This folder is **my** Power BI “full project” under `04-Power Bi/`. **[`06-Final-Project/`](../../06-Final-Project/README.md)** at the repo root is **my separate capstone** (Python / marketplace) — not the same assignment.

---

## Quick start

1. Install SQL Server + SSMS.
2. **I** created a database for **my** lab; imported `Customer_Data.csv` (staging → cleaned tables/views **the way my brief asked**).
3. `SQLQuery1.sql` was **my** starting sketch for ETL — **I** extended it for **my** schema.
4. Power BI → connect to SQL views or tables → **Transform** in Power Query → **Model** + **Report**.

**Walkthrough:** [Introduction to Churn Analysis](https://www.youtube.com/watch?v=QFDslca5AX8) (YouTube)

**Theme colors:** `#4A44F2`, `#9B9FF2`, `#F2F2F2`, `#A0D1FF`

**Typical output:** a churn report PBIX (in this repo: `full project.pbix` — consider renaming locally to `Telecom_Churn_Analysis.pbix` for clarity).

**Local SQL backups:** any `*.bak` **I** used stayed on **my** machine; `.gitignore` drops `*.bak` so **I** don’t push them.

---

## What I explored

Telecom churn — who leaves, why, and how revenue/services tie in — **my** demographic and geographic views in Power BI.

---

## Dataset

| File | Description |
|------|-------------|
| `Customer_Data.csv` | Telecom customer-level data |
| `SQLQuery1.sql` | Sample ETL / exploration SQL |

**Key columns (verify against the CSV header):** Customer_ID, Gender, Age, Married, State, Number_of_Referrals, Tenure_in_Months, Value_Deal, Phone_Service, Multiple_Lines, Internet_Service, Internet_Type, Online_Security, Online_Backup, Device_Protection_Plan, Premium_Support, Streaming_TV, Streaming_Movies, Streaming_Music, Unlimited_Data, Contract, Paperless_Billing, Payment_Method, Monthly_Charge, Total_Charges, Total_Refunds, Total_Extra_Data_Charges, Total_Long_Distance_Charges, Total_Revenue, Customer_Status, Churn_Category, Churn_Reason

Optional branding assets under `Data-Resources/` — **I** only used what **my** report needed.

---

## What I walked through

| Phase | What I did |
|-------|------------|
| **SQL Server (ETL)** | **My** staging import, cleaning rules, prod tables/views |
| **Power Query** | **My** groups (age, tenure, charges), service flags, churn labels |
| **DAX** | Total Customers, New Joiners, Total Churn, Churn Rate — **my** variants per brief |
| **Report** | **My** summary pages + churn reason detail/tooltips |

**Scope:** **Not** my AdventureWorks Lab 3. **[`06-Final-Project/`](../../06-Final-Project/README.md)** at repo root is **my other capstone** (Python / marketplace).

**Previous:** [`../03- Direct Query/README.md`](../03-%20Direct%20Query/README.md)

**Author:** Karam Yaseen — **my** churn BI project.

**Parent:** [`../README.md`](../README.md)
