"""E-Commerce Marketplace Analysis — Technical Assessment. Run: python task.py"""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split

try:
    BASE_DIR = Path(__file__).resolve().parent
except NameError:
    BASE_DIR = Path.cwd()

DATA_PATH = BASE_DIR / "Sales (1).csv"
OUT_CLEAN = BASE_DIR / "data_clean"
OUT_FIG = BASE_DIR / "outputs" / "figures"
SQL_DIR = BASE_DIR / "sql"

# Part A -> load_and_clean | Part B -> monthly_kpis_and_cohort, rfm_and_cluster
# Part C -> plot_dashboard_style | Bonus -> churn_model | Part D -> write_executive_summary


def load_and_clean() -> tuple[pd.DataFrame, dict]:
    """Part A — Data preparation: load, quality checks, derived flags."""
    raw_n = len(pd.read_csv(DATA_PATH))
    df = pd.read_csv(DATA_PATH)
    print("Rows loaded:", len(df))

    df["Order Date"] = pd.to_datetime(df["Order Date"], dayfirst=True, errors="coerce")
    df["Ship Date"] = pd.to_datetime(df["Ship Date"], dayfirst=True, errors="coerce")

    for col in ["Sales", "Profit", "Quantity", "Discount"]:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    dup_before = df.duplicated().sum()
    df = df.dropna(subset=["Order ID", "Customer ID", "Order Date"])
    df = df.drop_duplicates()
    df = df[df["Sales"] >= 0]

    valid_regions = {"West", "East", "Central", "South"}
    bad_region = ~df["Region"].isin(valid_regions)
    if bad_region.any():
        print("Dropping rows with invalid Region:", df.loc[bad_region, "Region"].unique().tolist())
        df = df[df["Region"].isin(valid_regions)]

    postal_missing = int(df["Postal Code"].isna().sum())
    print("Missing Postal Code (reported, not auto-filled):", postal_missing)

    def postal_to_text(x: object) -> str:
        if pd.isna(x):
            return ""
        try:
            return f"{int(round(float(x))):05d}"
        except (ValueError, TypeError):
            return ""

    df["Postal_Code_Text"] = df["Postal Code"].apply(postal_to_text)

    df["Order Month"] = df["Order Date"].dt.to_period("M")
    df["Order Week"] = df["Order Date"].dt.to_period("W")
    df["Profit Margin"] = df["Profit"] / df["Sales"].replace(0, np.nan)
    df["Shipping Delay Days"] = (df["Ship Date"] - df["Order Date"]).dt.days

    repeat_counts = df.groupby("Customer ID")["Order ID"].nunique()
    df["Repeat Customer"] = df["Customer ID"].map(repeat_counts).gt(1).astype(int)

    first_order = df.groupby("Customer ID")["Order Date"].transform("min")
    df["First Order Month"] = first_order.dt.to_period("M")
    df["Is New Customer"] = (df["Order Month"] == df["First Order Month"]).astype(int)

    latest_date = df["Order Date"].max()
    active_ids = df[df["Order Date"] >= latest_date - pd.Timedelta(days=90)]["Customer ID"].unique()
    df["Active Customer"] = df["Customer ID"].isin(active_ids).astype(int)

    quality = {
        "rows_in_file": int(raw_n),
        "rows_after_cleaning": int(len(df)),
        "duplicate_rows_removed": int(dup_before),
        "postal_codes_missing": postal_missing,
    }
    return df, quality


def monthly_kpis_and_cohort(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """Part B — KPIs (monthly active, new, churn, retention, AOV, LTV). Part C — cohort retention matrix."""
    orders = (
        df.groupby("Order ID")
        .agg({"Sales": "sum", "Profit": "sum", "Customer ID": "first", "Order Date": "first"})
        .reset_index()
    )
    orders["Order Month"] = orders["Order Date"].dt.to_period("M")

    aov_monthly = orders.groupby("Order Month")["Sales"].mean()
    active_monthly = df.groupby("Order Month")["Customer ID"].nunique()
    new_monthly = df[df["Is New Customer"] == 1].groupby("Order Month")["Customer ID"].nunique()

    monthly_customers = df.groupby("Order Month")["Customer ID"].apply(lambda x: set(x.unique()))
    months = sorted(monthly_customers.index)

    retention_monthly = []
    churn_monthly = []
    churned_counts = []
    for i in range(1, len(months)):
        prev, curr = set(monthly_customers[months[i - 1]]), set(monthly_customers[months[i]])
        retained = prev & curr
        churned = prev - curr
        retention_monthly.append(len(retained) / len(prev) if prev else np.nan)
        churn_monthly.append(len(churned) / len(prev) if prev else np.nan)
        churned_counts.append(len(churned))

    month_keys = list(months[1:])
    kpi = pd.DataFrame(
        {
            "month": month_keys,
            "retention_rate": retention_monthly,
            "churn_rate": churn_monthly,
            "churned_customers": churned_counts,
        }
    )
    kpi["AOV"] = kpi["month"].map(aov_monthly)
    kpi["active_customers"] = kpi["month"].map(active_monthly)
    kpi["new_customers"] = kpi["month"].map(new_monthly)

    print("Overall AOV (order level):", orders["Sales"].mean())
    print("LTV (avg revenue per customer):", df.groupby("Customer ID")["Sales"].sum().mean())

    cohort = df.copy()
    cohort["Cohort Month"] = cohort.groupby("Customer ID")["Order Date"].transform("min").dt.to_period("M")
    cohort["cohort_index"] = (cohort["Order Month"] - cohort["Cohort Month"]).apply(lambda x: x.n)
    cohort_table = cohort.pivot_table(
        index="Cohort Month", columns="cohort_index", values="Customer ID", aggfunc="nunique"
    )
    cohort_size = cohort_table.iloc[:, 0].replace(0, np.nan)
    retention_table = cohort_table.div(cohort_size, axis=0)

    return kpi, retention_table, orders


def rfm_and_cluster(df: pd.DataFrame) -> pd.DataFrame:
    """Part B — RFM + KMeans (optional clustering per assessment)."""
    snapshot = df["Order Date"].max()
    rfm = df.groupby("Customer ID").agg(
        Recency=("Order Date", lambda x: (snapshot - x.max()).days),
        Frequency=("Order ID", "nunique"),
        Monetary=("Sales", "sum"),
    )
    km = KMeans(n_clusters=4, random_state=42, n_init=10)
    rfm["Cluster"] = km.fit_predict(rfm)
    return rfm


def churn_model(rfm: pd.DataFrame) -> tuple[RandomForestClassifier, float, pd.Series, str]:
    """Bonus — Churn prediction: Random Forest, feature importance, classification report."""
    rfm = rfm.copy()
    rfm["Churn"] = (rfm["Recency"] > 90).astype(int)
    X = rfm[["Recency", "Frequency", "Monetary"]]
    y = rfm["Churn"]
    split_kw: dict = {"test_size": 0.2, "random_state": 42}
    if y.nunique() > 1:
        split_kw["stratify"] = y
    X_train, X_test, y_train, y_test = train_test_split(X, y, **split_kw)
    model = RandomForestClassifier(
        n_estimators=200,
        random_state=42,
        max_depth=8,
        min_samples_leaf=5,
        class_weight="balanced",
    )
    model.fit(X_train, y_train)
    acc = model.score(X_test, y_test)
    importance = pd.Series(model.feature_importances_, index=X.columns).sort_values(ascending=False)
    report = classification_report(y_test, model.predict(X_test), zero_division=0)
    print("Churn model accuracy:", acc)
    return model, acc, importance, report


def save_outputs(
    df: pd.DataFrame,
    kpi: pd.DataFrame,
    retention_table: pd.DataFrame,
    rfm: pd.DataFrame,
    rfm_imp: pd.Series,
    top_products: pd.Series,
    category_perf: pd.DataFrame,
    subcat_perf: pd.DataFrame,
    region_perf: pd.DataFrame,
    segment_perf: pd.DataFrame,
    weekly_sales: pd.Series,
    discount_impact: pd.DataFrame,
    quality: dict,
    churn_report: str,
) -> None:
    """Deliverables — CSV exports for dashboards and marking."""
    OUT_CLEAN.mkdir(parents=True, exist_ok=True)
    OUT_FIG.mkdir(parents=True, exist_ok=True)

    df.to_csv(OUT_CLEAN / "sales_cleaned.csv", index=False)
    kpi.to_csv(OUT_CLEAN / "kpi_monthly.csv", index=False)
    retention_table.to_csv(OUT_CLEAN / "cohort_retention.csv")
    rfm.to_csv(OUT_CLEAN / "rfm_segments.csv")
    rfm_imp.to_csv(OUT_CLEAN / "churn_feature_importance.csv", header=["importance"])
    top_products.to_csv(OUT_CLEAN / "top_products.csv", header=["Sales"])
    category_perf.to_csv(OUT_CLEAN / "category_performance.csv")
    subcat_perf.to_csv(OUT_CLEAN / "subcategory_performance.csv")
    region_perf.to_csv(OUT_CLEAN / "region_performance.csv")
    segment_perf.to_csv(OUT_CLEAN / "segment_performance.csv")
    weekly_sales.to_csv(OUT_CLEAN / "weekly_sales.csv", header=["Sales"])
    discount_impact.to_csv(OUT_CLEAN / "discount_impact.csv")
    with open(OUT_CLEAN / "data_quality_report.json", "w", encoding="utf-8") as f:
        json.dump(quality, f, indent=2)
    with open(OUT_CLEAN / "churn_model_classification_report.txt", "w", encoding="utf-8") as f:
        f.write(churn_report)

    print("Saved CSVs to:", OUT_CLEAN)


def plot_dashboard_style(df: pd.DataFrame, kpi: pd.DataFrame, retention_table: pd.DataFrame) -> None:
    """Part C — Charts (trends, cohort, products, region, shipping, profitability)."""
    OUT_FIG.mkdir(parents=True, exist_ok=True)
    try:
        plt.style.use("seaborn-v0_8-whitegrid")
    except OSError:
        plt.style.use("ggplot")

    fig, ax = plt.subplots(figsize=(10, 4))
    df.groupby("Order Month")["Sales"].sum().plot(ax=ax, title="Monthly Sales Trend")
    ax.set_ylabel("Sales")
    fig.tight_layout()
    fig.savefig(OUT_FIG / "01_monthly_sales.png", dpi=150)
    plt.close()

    fig, ax = plt.subplots(figsize=(10, 4))
    df.groupby("Order Month")["Profit"].sum().plot(ax=ax, color="green", title="Monthly Profit")
    ax.set_ylabel("Profit")
    fig.tight_layout()
    fig.savefig(OUT_FIG / "02_monthly_profit.png", dpi=150)
    plt.close()

    fig, ax = plt.subplots(figsize=(8, 5))
    df.groupby("Ship Mode")["Order ID"].nunique().plot(kind="bar", ax=ax, title="Orders by Ship Mode")
    fig.tight_layout()
    fig.savefig(OUT_FIG / "03_ship_mode.png", dpi=150)
    plt.close()

    fig, ax = plt.subplots(figsize=(10, 6))
    im = ax.imshow(retention_table.fillna(0).values, aspect="auto", cmap="Blues")
    ax.set_title("Cohort Retention (share of cohort size)")
    ax.set_xlabel("Periods since first purchase")
    ax.set_ylabel("Cohort month")
    plt.colorbar(im, ax=ax)
    fig.tight_layout()
    fig.savefig(OUT_FIG / "04_cohort_retention.png", dpi=150)
    plt.close()

    fig, ax = plt.subplots(figsize=(10, 4))
    df.groupby("Region")["Sales"].sum().plot(kind="bar", ax=ax, title="Sales by Region")
    fig.tight_layout()
    fig.savefig(OUT_FIG / "05_sales_by_region.png", dpi=150)
    plt.close()

    fig, ax = plt.subplots(figsize=(10, 5))
    subcat_sales = df.groupby("Sub-Category")["Sales"].sum().nlargest(12)
    subcat_sales.plot(kind="barh", ax=ax, title="Top Sub-Categories by Sales")
    fig.tight_layout()
    fig.savefig(OUT_FIG / "06_top_subcategories.png", dpi=150)
    plt.close()

    fig, ax = plt.subplots(figsize=(8, 4))
    df.groupby("Segment")["Sales"].sum().plot(kind="bar", ax=ax, title="Sales by Customer Segment", color="steelblue")
    fig.tight_layout()
    fig.savefig(OUT_FIG / "07_sales_by_segment.png", dpi=150)
    plt.close()

    fig, ax = plt.subplots(figsize=(11, 4))
    kpi_plot = kpi.copy()
    kpi_plot["month"] = kpi_plot["month"].astype(str)
    kpi_plot.plot(x="month", y=["retention_rate", "churn_rate"], ax=ax, title="Monthly Retention vs Churn Rate")
    ax.set_ylabel("Rate")
    plt.setp(ax.xaxis.get_majorticklabels(), rotation=45, ha="right")
    fig.tight_layout()
    fig.savefig(OUT_FIG / "08_retention_churn_trend.png", dpi=150)
    plt.close()

    fig, ax = plt.subplots(figsize=(8, 5))
    category_perf = df.groupby("Category").agg(Sales=("Sales", "sum"), Profit=("Profit", "sum"))
    category_perf["Margin"] = category_perf["Profit"] / category_perf["Sales"].replace(0, np.nan)
    category_perf["Margin"].plot(kind="bar", ax=ax, title="Profit Margin by Category", color="darkgreen")
    ax.set_ylabel("Margin")
    fig.tight_layout()
    fig.savefig(OUT_FIG / "09_margin_by_category.png", dpi=150)
    plt.close()

    print("Saved figures to:", OUT_FIG)


def write_executive_summary(
    df: pd.DataFrame,
    kpi: pd.DataFrame,
    category_perf: pd.DataFrame,
    region_perf: pd.DataFrame,
    top_products: pd.Series,
    model_acc: float,
    rfm_imp: pd.Series,
    quality: dict,
) -> None:
    """Part D — Business recommendations (written report)."""
    total_sales = df["Sales"].sum()
    total_profit = df["Profit"].sum()
    overall_margin = total_profit / total_sales if total_sales else 0
    avg_churn = kpi["churn_rate"].mean()
    avg_retention = kpi["retention_rate"].mean()
    worst_cat = category_perf["Margin"].idxmin()
    best_cat = category_perf["Margin"].idxmax()
    worst_margin = category_perf.loc[worst_cat, "Margin"]
    best_region_sales = region_perf["Sales"].idxmax()
    worst_region_profit = region_perf["Profit"].idxmin()
    top_product = top_products.index[0]

    lines = [
        "# Executive Summary — E-Commerce Marketplace Analysis",
        "",
        "*Auto-generated from `task.py`. Numbers reflect the cleaned dataset.*",
        "",
        "## 1. Snapshot",
        "",
        f"- **Total sales:** ${total_sales:,.2f}",
        f"- **Total profit:** ${total_profit:,.2f}",
        f"- **Overall profit margin:** {overall_margin:.1%}",
        f"- **Average monthly churn rate (customers who bought in month t-1 but not in t):** {avg_churn:.1%}",
        f"- **Average monthly retention (overlap of customers vs previous month):** {avg_retention:.1%}",
        f"- **Rows:** {quality['rows_after_cleaning']:,} (after cleaning; {quality['duplicate_rows_removed']:,} duplicates removed)",
        "",
        "## 2. Key findings",
        "",
        f"- **Highest margin category:** {best_cat} ({category_perf.loc[best_cat, 'Margin']:.1%}).",
        f"- **Lowest margin category:** {worst_cat} ({worst_margin:.1%}) — review pricing, discounts, and freight for this group.",
        f"- **Top region by sales:** {best_region_sales}. **Region with weakest profit:** {worst_region_profit} (investigate returns, discounts, or mix).",
        f"- **Top product by revenue:** {top_product[:80]}{'…' if len(top_product) > 80 else ''}",
        f"- **Churn model (Random Forest, Recency>90d proxy):** test accuracy ≈ {model_acc:.1%}. **Most important feature:** {rfm_imp.index[0]} ({rfm_imp.iloc[0]:.2f}).",
        "",
        "## 3. Business recommendations (Part D)",
        "",
        "### Churn and retention",
        "- Monthly churn between customer cohorts is high; many customers do not repeat in the next month. Run **email/SMS win-back** for one-time buyers and **loyalty points** for repeat buyers.",
        "- Prioritize **fast follow-up** after first purchase (day 7 / day 30) with related products and support.",
        "",
        "### Categories and products",
        f"- **Promote** high-margin categories ({best_cat}) and bundles that combine them with Furniture.",
        f"- **Review Furniture** profitability ({worst_margin:.1%} margin): reduce heavy discounts, negotiate supplier costs, or charge shipping transparently.",
        "- Use **top products** list in `data_clean/top_products.csv` for cross-sell on the site and in campaigns.",
        "",
        "### Pricing, bundling, discounts",
        "- **Heavy discount** rows often destroy profit; cap discounts on low-margin categories and test minimum order value for free shipping.",
        "- **Bundle** slow movers with best sellers to lift AOV (see `discount_impact.csv`).",
        "",
        "### Regions and segments",
        "- Compare **Region** and **Segment** in Power BI using `region_performance.csv` and `segment_performance.csv`; allocate marketing budget to high-profit regions and under-served segments.",
        "",
        "### Shipping and delivery",
        "- Analyze **Ship Mode** vs **Shipping Delay Days** in `sales_cleaned.csv`; if delays are long, communicate ETAs and offer expedited options where margin allows.",
        "",
        "## 4. Deliverables checklist",
        "",
        "- [x] Data preparation & quality (`data_quality_report.json`, `sales_cleaned.csv`)",
        "- [x] KPIs & cohorts (`kpi_monthly.csv`, `cohort_retention.csv`)",
        "- [x] RFM & clustering (`rfm_segments.csv`)",
        "- [x] Churn model (`churn_feature_importance.csv`, `churn_model_classification_report.txt`)",
        "- [x] Visuals (`outputs/figures/*.png`)",
        "- [x] SQL examples (`sql/sample_queries.sql`)",
        "- [x] This executive summary",
        "",
        "## Author",
        "",
        "Karam Yaseen",
        "",
    ]
    (BASE_DIR / "EXECUTIVE_SUMMARY.md").write_text("\n".join(lines), encoding="utf-8")
    print("Wrote:", BASE_DIR / "EXECUTIVE_SUMMARY.md")


def run_all() -> None:
    """Runs Parts A–D, bonus churn model, exports, charts, SQL sample file."""
    df, quality = load_and_clean()
    kpi, retention_table, _ = monthly_kpis_and_cohort(df)

    top_products = df.groupby("Product Name")["Sales"].sum().nlargest(15)
    category_perf = df.groupby("Category").agg(Sales=("Sales", "sum"), Profit=("Profit", "sum"))
    category_perf["Margin"] = category_perf["Profit"] / category_perf["Sales"].replace(0, np.nan)

    subcat_perf = df.groupby(["Category", "Sub-Category"]).agg(
        Sales=("Sales", "sum"), Profit=("Profit", "sum")
    )
    subcat_perf["Margin"] = subcat_perf["Profit"] / subcat_perf["Sales"].replace(0, np.nan)

    region_perf = df.groupby("Region").agg(Sales=("Sales", "sum"), Profit=("Profit", "sum"))
    segment_perf = df.groupby("Segment").agg(Sales=("Sales", "sum"), Profit=("Profit", "sum"))

    weekly_sales = df.groupby(df["Order Date"].dt.to_period("W"))["Sales"].sum()
    weekly_sales.index = weekly_sales.index.astype(str)

    discount_impact = df.groupby(pd.cut(df["Discount"], bins=[0, 0.2, 0.4, 0.6, 0.8, 1.0], include_lowest=True)).agg(
        Sales=("Sales", "mean"), Profit=("Profit", "mean"), Orders=("Order ID", "nunique")
    )

    rfm = rfm_and_cluster(df)
    _, model_acc, rfm_imp, churn_report = churn_model(rfm)

    save_outputs(
        df,
        kpi,
        retention_table,
        rfm,
        rfm_imp,
        top_products,
        category_perf,
        subcat_perf,
        region_perf,
        segment_perf,
        weekly_sales,
        discount_impact,
        quality,
        churn_report,
    )

    plot_dashboard_style(df, kpi, retention_table)
    write_executive_summary(df, kpi, category_perf, region_perf, top_products, model_acc, rfm_imp, quality)

    SQL_DIR.mkdir(parents=True, exist_ok=True)
    sql = """-- Sample SQL (PostgreSQL-style) — mirror of Python logic; load from sales_cleaned.csv into a table first
SELECT COUNT(*) AS row_count FROM sales;
SELECT SUM(CASE WHEN postal_code IS NULL THEN 1 ELSE 0 END) AS missing_postal FROM sales;

SELECT DATE_TRUNC('month', order_date) AS m, SUM(sales) AS sales, SUM(profit) AS profit
FROM sales GROUP BY 1 ORDER BY 1;

SELECT product_name, SUM(sales) AS sales FROM sales GROUP BY product_name ORDER BY sales DESC LIMIT 15;

SELECT category, SUM(sales) AS sales, SUM(profit) AS profit,
       SUM(profit) / NULLIF(SUM(sales), 0) AS margin
FROM sales GROUP BY category;
"""
    (SQL_DIR / "sample_queries.sql").write_text(sql, encoding="utf-8")

    print("Done. See EXECUTIVE_SUMMARY.md, data_clean/, outputs/figures/, sql/sample_queries.sql")


if __name__ == "__main__":
    run_all()
