# E‑commerce marketplace analysis — capstone (`06-Final-Project`)

End-to-end coursework capstone: prepare retail order data, compute KPIs, build RFM segments, train a simple churn model, and export CSVs for reporting or Power BI.

**Author:** Karam Yaseen — personal portfolio work for the NTI Data Analysis track. This is not official NTI material; use it as a study reference.

---

## Folder layout

| Path | Purpose |
|------|--------|
| `task.py` | **Script solution:** run the full pipeline from the terminal (`python task.py`). |
| `notebooks/final_project_walkthrough.ipynb` | **Notebook solution:** standalone pipeline (does not import `task.py`); reads `data/raw` directly; run cells in order. |
| `requirements.txt` | Python packages for this project (install into a venv). |
| `data/raw/` | Place the source file `Sales (1).csv` here (not always committed; see below). |
| `data/processed/` | Generated CSVs after you run the script or notebook. |
| `figures/` | **PNG charts** from `python task.py` (15 files, numbered `01_`–`15_`). |
| `sql/` | Sample SQL you can run in SSMS / your DB tool (optional for the Python track). |
| `docs/` | **Not in git** (see `.gitignore`): optional local notes — e.g. Power BI build steps, layout specs, executive summary. Cloners will not receive this folder. |
| `assets/` | Optional images for dashboards (if you add a `.pbix`). |

```
06-Final-Project/
├── README.md
├── requirements.txt
├── task.py
├── notebooks/
│   └── final_project_walkthrough.ipynb
├── data/
│   ├── raw/
│   │   └── Sales (1).csv      # source dataset
│   └── processed/             # outputs from task.py / notebook
├── figures/                   # PNGs from `python task.py`
├── sql/
├── docs/                    # local only — ignored by git
└── assets/                    # optional
```

---

## Quick start (beginners)

1. **Create a virtual environment** (recommended), from the repo root or this folder:
   - `python -m venv .venv`
   - Windows: `.venv\Scripts\activate`
   - macOS/Linux: `source .venv/bin/activate`

2. **Install dependencies:**
   - `pip install -r requirements.txt`

3. **Run the script (fastest):**
   - `cd 06-Final-Project`
   - `python task.py`
   - Check `data/processed/` for CSVs and `figures/` for PNG charts.

4. **Run the notebook (guided):**
   - `cd 06-Final-Project`
   - `jupyter lab` or `jupyter notebook`
   - Open `notebooks/final_project_walkthrough.ipynb` and run all cells top to bottom.

---

## Dataset

Default path: `data/raw/Sales (1).csv` (superstore-style retail line items: orders, customers, geography, product, sales, profit, discount).

If the raw file is missing, add it under `data/raw/` with that name, or change `DATA_PATH` in `task.py` to match your file.

---

## What the analysis does

1. **Clean** — Parse dates, fix known issues, drop bad rows, add time and customer flags.
2. **KPIs** — Totals, AOV, simple LTV proxy, monthly sales/profit, active vs new customers by month.
3. **RFM + clustering** — Recency, frequency, monetary value per customer; K-means with four clusters.
4. **Churn** — Label “churned” if recency > 90 days; Random Forest for illustration; feature importance exported.

---

## Outputs (`data/processed/`)

Regenerate everything with **`python task.py`** or by running the notebook to the last cell.

| File | Contents |
|------|----------|
| `sales_cleaned.csv` | Cleaned line-level rows |
| `kpi_monthly.csv` | Monthly sales, profit, active/new customers |
| `category_performance.csv`, `subcategory_performance.csv` | Rollups by category / sub-category |
| `region_performance.csv`, `segment_performance.csv` | Region and customer segment |
| `weekly_sales.csv` | Sales by week |
| `cohort_retention.csv` | Cohort retention matrix (rates by cohort month × period index) |
| `top_products.csv` | Top products by sales |
| `discount_impact.csv` | Sales/profit/orders by discount band |
| `rfm_segments.csv` | RFM + cluster per customer |
| `churn_feature_importance.csv` | Model feature weights |
| `churn_model_report.txt`, `churn_model_classification_report.txt` | Same classification report (two filenames for compatibility) |
| `data_quality_report.json` | Row count, columns, date range, null counts |

---

## Figures (`figures/`)

Created only when you run **`python task.py`** (Matplotlib + Seaborn, non-interactive backend).

| PNG | What it shows |
|-----|----------------|
| `01_monthly_kpis.png` | Monthly sales/profit + active vs new customers |
| `02_rfm_clusters.png` | RFM scatter + cluster means |
| `03_churn_feature_importance_rfm.png` | RFM churn model importances |
| `04_category_sales.png` | Sales by category |
| `05_region_sales.png` | Sales by region |
| `06_top_subcategories.png` | Top 12 sub-categories |
| `07_weekly_sales.png` | Weekly sales trend |
| `08_segment_sales.png` | Sales by segment |
| `09_discount_band_sales.png` | Sales by discount band |
| `10_cohort_retention_heatmap.png` | Cohort retention (18 periods) |
| `11_operations_overview.png` | Ship-mode pie, top cities, monthly profit, profit by category |
| `12_boxplot_sales_profit.png` | Sales & profit boxplots |
| `13_discount_vs_profit_scatter.png` | Discount vs profit scatter |
| `14_top10_products.png` | Top 10 products |
| `15_churn_extended_feature_importance.png` | Extended churn model (ROC-AUC in title) |

---

## Related course folders

This capstone sits **after** the numbered modules in the repo (`01`–`05`). The Power BI labs under `04-Power Bi/` are a different assignment; you can connect Power BI to the **processed** CSVs here if you extend the project.

---

## SQL scripts

Files under `sql/` are for optional database practice. Read each script before running it on a shared server; some examples may assume a specific schema.

---

**Parent:** [`../README.md`](../README.md)
