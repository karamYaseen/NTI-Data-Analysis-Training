# Executive Summary — E-Commerce Marketplace Analysis

*Auto-generated from `task.py`. Numbers reflect the cleaned dataset.*

## 1. Snapshot

- **Total sales:** $2,296,938.90
- **Total profit:** $286,355.11
- **Overall profit margin:** 12.5%
- **Average monthly churn rate (customers who bought in month t-1 but not in t):** 87.9%
- **Average monthly retention (overlap of customers vs previous month):** 12.1%
- **Rows:** 9,993 (after cleaning; 0 duplicates removed)

## 2. Key findings

- **Highest margin category:** Technology (17.4%).
- **Lowest margin category:** Furniture (2.5%) — review pricing, discounts, and freight for this group.
- **Top region by sales:** West. **Region with weakest profit:** Central (investigate returns, discounts, or mix).
- **Top product by revenue:** Canon imageCLASS 2200 Advanced Copier
- **Churn model (Random Forest, Recency>90d proxy):** test accuracy ≈ 98.1%. **Most important feature:** Recency (0.90).

## 3. Business recommendations (Part D)

### Churn and retention
- Monthly churn between customer cohorts is high; many customers do not repeat in the next month. Run **email/SMS win-back** for one-time buyers and **loyalty points** for repeat buyers.
- Prioritize **fast follow-up** after first purchase (day 7 / day 30) with related products and support.

### Categories and products
- **Promote** high-margin categories (Technology) and bundles that combine them with Furniture.
- **Review Furniture** profitability (2.5% margin): reduce heavy discounts, negotiate supplier costs, or charge shipping transparently.
- Use **top products** list in `data_clean/top_products.csv` for cross-sell on the site and in campaigns.

### Pricing, bundling, discounts
- **Heavy discount** rows often destroy profit; cap discounts on low-margin categories and test minimum order value for free shipping.
- **Bundle** slow movers with best sellers to lift AOV (see `discount_impact.csv`).

### Regions and segments
- Compare **Region** and **Segment** in Power BI using `region_performance.csv` and `segment_performance.csv`; allocate marketing budget to high-profit regions and under-served segments.

### Shipping and delivery
- Analyze **Ship Mode** vs **Shipping Delay Days** in `sales_cleaned.csv`; if delays are long, communicate ETAs and offer expedited options where margin allows.

## 4. Deliverables checklist

- [x] Data preparation & quality (`data_quality_report.json`, `sales_cleaned.csv`)
- [x] KPIs & cohorts (`kpi_monthly.csv`, `cohort_retention.csv`)
- [x] RFM & clustering (`rfm_segments.csv`)
- [x] Churn model (`churn_feature_importance.csv`, `churn_model_classification_report.txt`)
- [x] Visuals (`outputs/figures/*.png`)
- [x] SQL examples (`sql/sample_queries.sql`)
- [x] This executive summary

## Author

Karam Yaseen
