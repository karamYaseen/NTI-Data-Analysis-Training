# E-Commerce Marketplace Analysis — Final Project

## Simplest way

1. Put `Sales (1).csv` next to `task.py`, install `pip install -r requirements.txt`.
2. **One command:** `python task.py` → creates `data_clean/`, `outputs/figures/`, `EXECUTIVE_SUMMARY.md`.
3. **Or** open `final_project.ipynb`, run all cells (start Jupyter **from the `Final Project` folder** so imports work).

## Scenario

Your company operates an online marketplace. You have a sales dataset with customer transactions, product details, and orders. The goal is to analyze metrics, spot issues, and recommend actions.

## Dataset (`Sales (1).csv`)

| Column | Description |
|--------|-------------|
| Row ID | Row identifier |
| Order ID | Unique order |
| Order Date / Ship Date | Order and ship dates |
| Ship Mode | e.g. Standard Class, Second Class |
| Customer ID / Customer Name | Customer |
| Segment | Consumer, Corporate, Home Office |
| Country/Region, City, **State**, Postal Code, Region | Geography |
| Product ID, Category, Sub-Category, Product Name | Product |
| Sales, Quantity, Discount, Profit | Measures |

## Assessment mapping

| Part | What is covered |
|------|------------------|
| **A — Data prep** | Cleaning, duplicates, invalid region, missing postal reported, `data_quality_report.json`, active/repeat/new flags |
| **B — KPIs** | Monthly KPIs, AOV, LTV, churned customer counts, retention/churn, RFM + KMeans, churn Random Forest + report |
| **C — Visualization** | PNG charts in `outputs/figures/`, plus CSVs for Power BI / Tableau |
| **D — Recommendations** | `EXECUTIVE_SUMMARY.md` (auto-generated with numbers) |

## How to run

1. Place `Sales (1).csv` next to `task.py`.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the analysis:

```bash
python task.py
```

This writes **cleaned data**, **KPI tables**, **figures**, **`EXECUTIVE_SUMMARY.md`**, and SQL helpers under **`sql/`**.

## Outputs

### Reports

| File | Purpose |
|------|---------|
| `EXECUTIVE_SUMMARY.md` | Snapshot + findings + Part D recommendations (re-run `task.py` to refresh numbers) |
| `sql/sample_queries.sql` | Short generic examples (PostgreSQL-style `DATE_TRUNC` notes) |
| `sql/orders_project_analysis.sql` | **Your SSMS work:** `OrdersProject` — missing checks, dates, dedupe, active/new/churn, Part B KPIs, RFM base |

Run **`orders_project_analysis.sql`** on your database (backup first; contains `ALTER` / `UPDATE` / `DELETE` / `SELECT INTO`).

### `data_clean/` (for dashboards)

| File | Purpose |
|------|---------|
| `sales_cleaned.csv` | Main fact table |
| `kpi_monthly.csv` | Monthly AOV, active, new, retention, churn rate, **churned_customers** |
| `cohort_retention.csv` | Cohort retention matrix |
| `weekly_sales.csv` | Weekly sales totals |
| `category_performance.csv` | Sales, profit, margin by category |
| `subcategory_performance.csv` | By category + sub-category |
| `region_performance.csv` | Region sales & profit |
| `segment_performance.csv` | Segment sales & profit |
| `top_products.csv` | Top products |
| `rfm_segments.csv` | RFM + cluster |
| `discount_impact.csv` | Avg sales/profit by discount band |
| `churn_feature_importance.csv` | Model feature weights |
| `churn_model_classification_report.txt` | Precision/recall/F1 |
| `data_quality_report.json` | Row counts, duplicate removal, missing postal count |

### `outputs/figures/`

Charts: monthly sales/profit, ship mode, cohort heatmap, region, top sub-categories, segment, retention vs churn trend, margin by category.

## Deliverables checklist

- [x] Python script (`task.py`) — SQL-style samples in `sql/`
- [x] CSVs + PNGs for dashboards / KPIs
- [x] Executive summary & recommendations (`EXECUTIVE_SUMMARY.md`)
- [ ] Optional: your own `.pbix` or slide deck using `data_clean/`

## Author

Karam Yaseen
