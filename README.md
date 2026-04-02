# NTI Data Analysis Training

Personal coursework for an **NTI Data Analysis** program: relational design, SQL, Python for analytics, Power BI, and a capstone e‑commerce project.

---

## What’s inside

| Path | Focus |
|------|--------|
| [`01-Database-Design/`](01-Database-Design/) | ERDs and relational mapping (Musicana, Hospital, Real Estate, Airline, …) |
| [`02-SQL/`](02-SQL/) | DDL/DML, joins, aggregations, advanced queries |
| [`03-Python/`](03-Python/) | Core Python → NumPy / Pandas / plots → recap automation |
| [`04-Power Bi/`](04-Power%20Bi/README.md) | Power Query, modeling, dashboards; **Lab 3** → [`04-Power Bi/03- Direct Query/`](04-Power%20Bi/03-%20Direct%20Query/README.md) |
| [`Final Project/`](Final%20Project/README.md) | **Capstone:** sales data, KPIs, cohorts, RFM, churn model, exports, executive summary |

---

## Skills covered

- **Databases:** ERD → tables, keys, normalization mindset  
- **SQL:** create/load data, filter, join, aggregate, subqueries  
- **Python:** types, collections, functions, OOP, NumPy/Pandas, matplotlib  
- **Analytics:** cleaning, KPIs, segmentation, simple ML (Random Forest), reporting  
- **BI:** dashboards and storytelling with Power BI  

---

## Quick start

| Goal | Steps |
|------|--------|
| **Full Python track** | `pip install -r requirements.txt` then optional `python 03-Python/tutorial.py` (run from `03-Python` or use paths as in that folder’s README). |
| **Capstone only** | Uses [`Final Project/requirements.txt`](Final%20Project/requirements.txt) (pandas, numpy, matplotlib, scikit-learn — lighter than the repo root). |

**Capstone commands:**

```bash
cd "Final Project"
pip install -r requirements.txt
python task.py
```

Outputs: `data_clean/`, `outputs/figures/`, `EXECUTIVE_SUMMARY.md`, `sql/`. See [`Final Project/README.md`](Final%20Project/README.md).

---

## About this repo

It’s a **learning journal**: exercises, notes, and runnable projects in one place. Fork or clone for structure; content reflects the curriculum as completed.

**Author:** Karam Yaseen
