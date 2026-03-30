# E-Commerce Marketplace Analysis — Final Project

Technical assessment: **prepare data**, compute **KPIs**, **visualize**, and write **recommendations** from a marketplace-style sales extract.

---

## Quick start

1. Add **`Sales (1).csv`** in this folder next to **`task.py`**.
2. Install dependencies:  
   `pip install -r requirements.txt`
3. Run:  
   `python task.py`

**Optional:** open **`final_project.ipynb`** and run cells top to bottom (start Jupyter with this folder as the working directory so `import task` works).

One run produces:

- **`data_clean/`** — cleaned fact table + KPI/segment CSVs for Excel or Power BI  
- **`outputs/figures/`** — PNG charts  
- **`EXECUTIVE_SUMMARY.md`** — auto summary with key numbers and Part D recommendations  
- **`sql/`** — sample SQL aligned with the analysis  

---

## Scenario

You analyze an online marketplace: orders, customers, products, and geography. Goals: measure performance, find weak spots, and suggest actions.

---

## Dataset (`Sales (1).csv`)

| Area | Columns |
|------|---------|
| Order | Row ID, Order ID, Order Date, Ship Date, Ship Mode |
| Customer | Customer ID, Name, Segment |
| Geography | Country/Region, City, State, Postal Code, Region |
| Product | Product ID, Category, Sub-Category, Product Name |
| Measures | Sales, Quantity, Discount, Profit |

---

## Assessment mapping

| Part | Delivered in this project |
|------|---------------------------|
| **A — Data prep** | Cleaning, duplicates, invalid regions, missing postal reported, quality JSON, customer flags |
| **B — KPIs** | Monthly metrics, AOV, LTV, retention/churn, RFM + clustering, churn model + report |
| **C — Visualization** | PNGs in `outputs/figures/`, dashboard-ready CSVs |
| **D — Recommendations** | `EXECUTIVE_SUMMARY.md` |

---

## Outputs (reference)

**Reports:** `EXECUTIVE_SUMMARY.md` · `sql/sample_queries.sql` · `sql/orders_project_analysis.sql` (SSMS / SQL Server — **back up DB first**; script may alter data).

**`data_clean/`** (main files for BI):

`sales_cleaned.csv` · `kpi_monthly.csv` · `cohort_retention.csv` · `weekly_sales.csv` · `category_performance.csv` · `subcategory_performance.csv` · `region_performance.csv` · `segment_performance.csv` · `top_products.csv` · `rfm_segments.csv` · `discount_impact.csv` · `churn_feature_importance.csv` · `churn_model_classification_report.txt` · `data_quality_report.json`

**`outputs/figures/`:** Monthly sales/profit, ship mode, cohort heatmap, region, sub-categories, segment, retention vs churn, margin by category.

---

## Deliverables checklist

- [x] Python (`task.py`) + SQL samples under `sql/`  
- [x] Exported CSVs and figures  
- [x] Executive summary (`EXECUTIVE_SUMMARY.md`)  
- [ ] Optional: your own `.pbix` or slides using `data_clean/`  

---

**Author:** Karam Yaseen
