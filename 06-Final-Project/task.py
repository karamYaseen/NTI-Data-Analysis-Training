"""
E-Commerce Marketplace Analysis — Simple Solution
KISS Principle: Keep It Simple Stupid
"""

import json
from datetime import timedelta

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pathlib import Path
from sklearn.cluster import KMeans
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, roc_auc_score

DATA_PATH = Path(__file__).parent / "data" / "raw" / "Sales (1).csv"
OUTPUT_DIR = Path(__file__).parent / "data" / "processed"
FIGURES_DIR = Path(__file__).parent / "figures"

def load_and_clean_data():
    """Load and clean the sales data"""
    df = pd.read_csv(DATA_PATH)

    # Parse dates
    df['Order Date'] = pd.to_datetime(df['Order Date'], dayfirst=True, errors='coerce')
    df['Ship Date'] = pd.to_datetime(df['Ship Date'], dayfirst=True, errors='coerce')

    # Convert numeric columns
    for col in ['Sales', 'Profit', 'Quantity', 'Discount']:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    # Fix Burlington postal code
    df.loc[(df['City'] == 'Burlington') & (df['Postal Code'].isnull()), 'Postal Code'] = 5401
    df['Postal Code'] = df['Postal Code'].astype(int)

    # Fix Ship Mode
    df['Ship Mode'] = df['Ship Mode'].replace('sas', 'Standard Class')

    # Remove duplicates and invalid data
    df = df.drop_duplicates()
    df = df.dropna(subset=['Order ID', 'Customer ID', 'Order Date'])
    df = df[df['Sales'] >= 0]
    df = df[df['Region'].isin(['West', 'East', 'Central', 'South'])]

    # Drop first row
    df = df.drop(df.index[0]).reset_index(drop=True)

    # Add features
    df['Order Month'] = df['Order Date'].dt.to_period('M')
    df['Profit Margin'] = df['Profit'] / df['Sales']

    # Customer flags
    repeat_counts = df.groupby('Customer ID')['Order ID'].nunique()
    df['Repeat Customer'] = df['Customer ID'].map(repeat_counts).gt(1).astype(int)

    first_order = df.groupby('Customer ID')['Order Date'].transform('min')
    df['First Order Month'] = first_order.dt.to_period('M')
    df['Is New Customer'] = (df['Order Month'] == df['First Order Month']).astype(int)

    return df

def calculate_kpis(df):
    """Calculate key performance indicators"""
    # Aggregate to order level
    orders = df.groupby('Order ID').agg({
        'Sales': 'sum',
        'Profit': 'sum',
        'Customer ID': 'first',
        'Order Date': 'first'
    }).reset_index()
    orders['Order Month'] = orders['Order Date'].dt.to_period('M')

    # Monthly metrics - ensure all have same index
    all_months = df['Order Month'].unique()
    all_months = sorted(all_months)

    monthly_sales = df.groupby('Order Month')['Sales'].sum().reindex(all_months, fill_value=0)
    monthly_profit = df.groupby('Order Month')['Profit'].sum().reindex(all_months, fill_value=0)
    active_customers = df.groupby('Order Month')['Customer ID'].nunique().reindex(all_months, fill_value=0)
    new_customers = df[df['Is New Customer'] == 1].groupby('Order Month')['Customer ID'].nunique().reindex(all_months, fill_value=0)

    # Overall KPIs
    total_sales = df['Sales'].sum()
    total_profit = df['Profit'].sum()
    total_orders = len(orders)
    aov = total_sales / total_orders
    ltv = df.groupby('Customer ID')['Sales'].sum().mean()

    return {
        'total_sales': total_sales,
        'total_profit': total_profit,
        'total_orders': total_orders,
        'aov': aov,
        'ltv': ltv,
        'monthly_sales': monthly_sales,
        'monthly_profit': monthly_profit,
        'active_customers': active_customers,
        'new_customers': new_customers
    }

def create_rfm_segments(df):
    """Create RFM segments using K-means clustering"""
    snapshot_date = df['Order Date'].max()

    rfm = df.groupby('Customer ID').agg({
        'Order Date': lambda x: (snapshot_date - x.max()).days,  # Recency
        'Order ID': 'nunique',  # Frequency
        'Sales': 'sum'  # Monetary
    }).reset_index()

    rfm.columns = ['Customer ID', 'Recency', 'Frequency', 'Monetary']

    # K-means clustering
    kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
    rfm['Cluster'] = kmeans.fit_predict(rfm[['Recency', 'Frequency', 'Monetary']])

    return rfm

def predict_churn(rfm):
    """Predict customer churn using Random Forest"""
    rfm['Churn'] = (rfm['Recency'] > 90).astype(int)

    X = rfm[['Recency', 'Frequency', 'Monetary']]
    y = rfm['Churn']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

    model = RandomForestClassifier(n_estimators=200, max_depth=8, random_state=42, class_weight='balanced')
    model.fit(X_train, y_train)

    accuracy = model.score(X_test, y_test)
    predictions = model.predict(X_test)

    return {
        'model': model,
        'accuracy': accuracy,
        'feature_importance': pd.Series(model.feature_importances_, index=X.columns),
        'report': classification_report(y_test, predictions, target_names=['Active', 'Churned'])
    }

def _cohort_retention_table(df):
    d = df.copy()
    first = d.groupby('Customer ID')['Order Date'].min().dt.to_period('M')
    d['CohortGroup'] = d['Customer ID'].map(first)
    d['OrderMonth'] = d['Order Date'].dt.to_period('M')
    d['PeriodIndex'] = (d['OrderMonth'] - d['CohortGroup']).apply(lambda x: x.n)
    cohort = d.groupby(['CohortGroup', 'PeriodIndex'])['Customer ID'].nunique().reset_index()
    cohort = cohort.rename(columns={'Customer ID': 'Customers'})
    sizes = cohort[cohort['PeriodIndex'] == 0].set_index('CohortGroup')['Customers']
    wide = cohort.pivot(index='CohortGroup', columns='PeriodIndex', values='Customers')
    rate = wide.div(sizes, axis=0).round(4)
    rate = rate.reset_index().rename(columns={'CohortGroup': 'cohort_month'})
    return rate


def _weekly_sales(df):
    w = df.copy()
    w['Order Week'] = w['Order Date'].dt.to_period('W').apply(lambda p: p.start_time.date())
    return w.groupby('Order Week', as_index=False)['Sales'].sum()


def _discount_impact(df):
    x = df.copy()
    x['Discount Bin'] = pd.cut(
        x['Discount'],
        bins=[-0.001, 0, 0.2, 0.4, 1.0],
        labels=['None', '1-20%', '21-40%', '41-100%'],
    )
    return x.groupby('Discount Bin', observed=False).agg(
        Sales=('Sales', 'sum'),
        Profit=('Profit', 'sum'),
        Orders=('Order ID', 'nunique'),
    ).reset_index()


def _data_quality_report(df):
    return {
        'rows': len(df),
        'columns': list(df.columns),
        'date_range': {
            'order_date_min': str(df['Order Date'].min()),
            'order_date_max': str(df['Order Date'].max()),
        },
        'numeric_nulls': {c: int(df[c].isna().sum()) for c in ['Sales', 'Profit', 'Quantity', 'Discount']},
    }


def _export_frames(df, kpis, rfm, churn_results):
    kpi_df = pd.DataFrame({
        'Month': kpis['monthly_sales'].index.astype(str),
        'Sales': kpis['monthly_sales'].values,
        'Profit': kpis['monthly_profit'].values,
        'Active_Customers': kpis['active_customers'].values,
        'New_Customers': kpis['new_customers'].values
    })
    category_perf = df.groupby('Category').agg({
        'Sales': 'sum',
        'Profit': 'sum',
        'Quantity': 'sum'
    }).reset_index()
    subcat = df.groupby('Sub-Category').agg({
        'Sales': 'sum',
        'Profit': 'sum',
        'Quantity': 'sum'
    }).reset_index()
    region_perf = df.groupby('Region').agg({
        'Sales': 'sum',
        'Profit': 'sum'
    }).reset_index()
    seg = df.groupby('Segment').agg({
        'Sales': 'sum',
        'Profit': 'sum',
        'Customer ID': 'nunique'
    }).reset_index().rename(columns={'Customer ID': 'Unique_Customers'})
    top_p = df.groupby('Product Name').agg({'Sales': 'sum', 'Profit': 'sum'}).reset_index()
    top_p = top_p.sort_values('Sales', ascending=False).head(25)
    weekly = _weekly_sales(df)
    cohort_rate = _cohort_retention_table(df)
    discount_impact = _discount_impact(df)
    return {
        'kpi_df': kpi_df,
        'category_perf': category_perf,
        'subcategory_perf': subcat,
        'region_perf': region_perf,
        'segment_perf': seg,
        'top_products': top_p,
        'weekly_sales': weekly,
        'cohort_rate': cohort_rate,
        'discount_impact': discount_impact,
    }


def save_analysis_outputs(df, kpis, rfm, churn_results, frames=None):
    if frames is None:
        frames = _export_frames(df, kpis, rfm, churn_results)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    df.to_csv(OUTPUT_DIR / 'sales_cleaned.csv', index=False)
    rfm.to_csv(OUTPUT_DIR / 'rfm_segments.csv', index=False)
    frames['kpi_df'].to_csv(OUTPUT_DIR / 'kpi_monthly.csv', index=False)
    frames['category_perf'].to_csv(OUTPUT_DIR / 'category_performance.csv', index=False)
    frames['subcategory_perf'].to_csv(OUTPUT_DIR / 'subcategory_performance.csv', index=False)
    frames['region_perf'].to_csv(OUTPUT_DIR / 'region_performance.csv', index=False)
    frames['segment_perf'].to_csv(OUTPUT_DIR / 'segment_performance.csv', index=False)
    frames['top_products'].to_csv(OUTPUT_DIR / 'top_products.csv', index=False)
    frames['weekly_sales'].to_csv(OUTPUT_DIR / 'weekly_sales.csv', index=False)
    frames['cohort_rate'].to_csv(OUTPUT_DIR / 'cohort_retention.csv', index=False)
    frames['discount_impact'].to_csv(OUTPUT_DIR / 'discount_impact.csv', index=False)

    churn_results['feature_importance'].rename('importance').to_frame().to_csv(
        OUTPUT_DIR / 'churn_feature_importance.csv'
    )

    with open(OUTPUT_DIR / 'churn_model_report.txt', 'w', encoding='utf-8') as f:
        f.write(churn_results['report'])
    with open(OUTPUT_DIR / 'churn_model_classification_report.txt', 'w', encoding='utf-8') as f:
        f.write(churn_results['report'])

    with open(OUTPUT_DIR / 'data_quality_report.json', 'w', encoding='utf-8') as f:
        json.dump(_data_quality_report(df), f, indent=2)

    return OUTPUT_DIR


def save_all_figures(df, kpis, rfm, churn_results, frames):
    FIGURES_DIR.mkdir(parents=True, exist_ok=True)
    sns.set_theme(style='whitegrid', context='notebook')
    dpi = 150

    months = kpis['monthly_sales'].index.astype(str)
    fig, axes = plt.subplots(2, 1, figsize=(11, 7), sharex=True)
    axes[0].plot(months, kpis['monthly_sales'].values / 1e3, color='#2ecc71', linewidth=2, label='Sales ($k)')
    axes[0].plot(months, kpis['monthly_profit'].values / 1e3, color='#3498db', linewidth=2, label='Profit ($k)')
    axes[0].set_ylabel('Amount ($ thousands)')
    axes[0].legend(loc='upper left')
    axes[0].set_title('Monthly sales and profit')
    x = range(len(months))
    w = 0.35
    axes[1].bar([i - w / 2 for i in x], kpis['active_customers'].values, width=w, label='Active', color='#9b59b6')
    axes[1].bar([i + w / 2 for i in x], kpis['new_customers'].values, width=w, label='New', color='#e67e22')
    step = max(1, len(x) // 12)
    axes[1].set_xticks(x[::step])
    axes[1].set_xticklabels([months[i] for i in x[::step]], rotation=45, ha='right')
    axes[1].set_ylabel('Customers')
    axes[1].legend()
    axes[1].set_title('Active vs new customers by month')
    plt.tight_layout()
    fig.savefig(FIGURES_DIR / '01_monthly_kpis.png', dpi=dpi, bbox_inches='tight')
    plt.close(fig)

    rfm_plot = rfm.drop(columns=['Churn'], errors='ignore')
    fig, axes = plt.subplots(1, 2, figsize=(12, 4.5))
    sc = axes[0].scatter(
        rfm_plot['Recency'], rfm_plot['Monetary'] / 1e3, c=rfm_plot['Cluster'],
        cmap='viridis', alpha=0.65, s=18, edgecolors='k', linewidths=0.2,
    )
    axes[0].set_xlabel('Recency (days)')
    axes[0].set_ylabel('Monetary ($ thousands)')
    axes[0].set_title('RFM: recency vs monetary (color=cluster)')
    plt.colorbar(sc, ax=axes[0], label='Cluster')
    cm = rfm_plot.groupby('Cluster')[['Recency', 'Frequency', 'Monetary']].mean()
    cm.plot(kind='bar', ax=axes[1], rot=0, color=['#e74c3c', '#3498db', '#2ecc71'])
    axes[1].set_title('Average RFM by cluster')
    axes[1].set_xlabel('Cluster')
    axes[1].legend(loc='upper right')
    plt.tight_layout()
    fig.savefig(FIGURES_DIR / '02_rfm_clusters.png', dpi=dpi, bbox_inches='tight')
    plt.close(fig)

    fi = churn_results['feature_importance'].sort_values()
    fig, ax = plt.subplots(figsize=(7, 3.5))
    fi.plot(kind='barh', ax=ax, color=sns.color_palette('muted', n_colors=len(fi)))
    ax.set_xlabel('Importance')
    ax.set_title('Churn (RFM model): feature importance')
    plt.tight_layout()
    fig.savefig(FIGURES_DIR / '03_churn_feature_importance_rfm.png', dpi=dpi, bbox_inches='tight')
    plt.close(fig)

    cat = frames['category_perf'].sort_values('Sales', ascending=True)
    fig, ax = plt.subplots(figsize=(7, 4))
    ax.barh(cat['Category'], cat['Sales'] / 1e3, color='#16a085')
    ax.set_xlabel('Sales ($ thousands)')
    ax.set_title('Sales by category')
    plt.tight_layout()
    fig.savefig(FIGURES_DIR / '04_category_sales.png', dpi=dpi, bbox_inches='tight')
    plt.close(fig)

    reg = frames['region_perf'].sort_values('Sales', ascending=True)
    fig, ax = plt.subplots(figsize=(6, 3.5))
    ax.barh(reg['Region'], reg['Sales'] / 1e3, color='#2980b9')
    ax.set_xlabel('Sales ($ thousands)')
    ax.set_title('Sales by region')
    plt.tight_layout()
    fig.savefig(FIGURES_DIR / '05_region_sales.png', dpi=dpi, bbox_inches='tight')
    plt.close(fig)

    sub = frames['subcategory_perf'].nlargest(12, 'Sales').sort_values('Sales')
    fig, ax = plt.subplots(figsize=(7, 5))
    ax.barh(sub['Sub-Category'], sub['Sales'] / 1e3, color='#8e44ad')
    ax.set_xlabel('Sales ($ thousands)')
    ax.set_title('Top 12 sub-categories by sales')
    plt.tight_layout()
    fig.savefig(FIGURES_DIR / '06_top_subcategories.png', dpi=dpi, bbox_inches='tight')
    plt.close(fig)

    ws = frames['weekly_sales']
    fig, ax = plt.subplots(figsize=(11, 4))
    ax.plot(ws['Order Week'], ws['Sales'] / 1e3, color='#c0392b', linewidth=1.2)
    ax.set_xlabel('Week')
    ax.set_ylabel('Sales ($ thousands)')
    ax.set_title('Weekly sales trend')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    fig.savefig(FIGURES_DIR / '07_weekly_sales.png', dpi=dpi, bbox_inches='tight')
    plt.close(fig)

    seg = frames['segment_perf'].sort_values('Sales', ascending=True)
    fig, ax = plt.subplots(figsize=(6, 3.5))
    ax.barh(seg['Segment'], seg['Sales'] / 1e3, color='#d35400')
    ax.set_xlabel('Sales ($ thousands)')
    ax.set_title('Sales by customer segment')
    plt.tight_layout()
    fig.savefig(FIGURES_DIR / '08_segment_sales.png', dpi=dpi, bbox_inches='tight')
    plt.close(fig)

    di = frames['discount_impact']
    fig, ax = plt.subplots(figsize=(7, 4))
    xpos = range(len(di))
    ax.bar(xpos, di['Sales'] / 1e3, color='#7f8c8d')
    ax.set_xticks(xpos)
    ax.set_xticklabels([str(x) for x in di['Discount Bin']], rotation=15)
    ax.set_ylabel('Sales ($ thousands)')
    ax.set_title('Sales by discount band')
    plt.tight_layout()
    fig.savefig(FIGURES_DIR / '09_discount_band_sales.png', dpi=dpi, bbox_inches='tight')
    plt.close(fig)

    coh = frames['cohort_rate'].set_index('cohort_month').iloc[:, :18]
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.heatmap(coh, cmap='YlOrRd', vmin=0, vmax=1, linewidths=0.3, ax=ax, cbar_kws={'label': 'Retention'})
    ax.set_title('Cohort retention (first 18 periods)')
    ax.set_xlabel('Periods since first order')
    ax.set_ylabel('Cohort month')
    plt.tight_layout()
    fig.savefig(FIGURES_DIR / '10_cohort_retention_heatmap.png', dpi=dpi, bbox_inches='tight')
    plt.close(fig)

    fig, axes = plt.subplots(2, 2, figsize=(12, 9))
    sm = df['Ship Mode'].value_counts()
    axes[0, 0].pie(sm.values, labels=sm.index, autopct='%1.1f%%', startangle=90)
    axes[0, 0].set_title('Shipping mode mix')
    tc = df.groupby('City')['Sales'].sum().nlargest(10)
    tc.plot(kind='bar', ax=axes[0, 1], color='#8e44ad', rot=45)
    axes[0, 1].set_title('Top 10 cities by sales')
    axes[0, 1].set_xlabel('')
    mp = df.groupby('Order Month')['Profit'].sum()
    axes[1, 0].plot(range(len(mp)), mp.values, color='green', marker='o', markersize=3)
    st = max(1, len(mp) // 12)
    axes[1, 0].set_xticks(range(0, len(mp), st))
    axes[1, 0].set_xticklabels([str(mp.index[i]) for i in range(0, len(mp), st)], rotation=45, ha='right')
    axes[1, 0].set_title('Monthly profit trend')
    axes[1, 0].set_ylabel('Profit')
    cp = df.groupby('Category')['Profit'].sum()
    sns.barplot(x=cp.index, y=cp.values, ax=axes[1, 1], hue=cp.index, palette='muted', legend=False)
    axes[1, 1].set_title('Profit by category')
    axes[1, 1].tick_params(axis='x', rotation=20)
    plt.tight_layout()
    fig.savefig(FIGURES_DIR / '11_operations_overview.png', dpi=dpi, bbox_inches='tight')
    plt.close(fig)

    fig, axes = plt.subplots(1, 2, figsize=(10, 4))
    sns.boxplot(data=df, y='Sales', ax=axes[0], color='#3498db')
    axes[0].set_title('Sales distribution')
    sns.boxplot(data=df, y='Profit', ax=axes[1], color='#e74c3c')
    axes[1].set_title('Profit distribution')
    plt.tight_layout()
    fig.savefig(FIGURES_DIR / '12_boxplot_sales_profit.png', dpi=dpi, bbox_inches='tight')
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.scatter(df['Discount'], df['Profit'], alpha=0.2, s=8, c='#34495e')
    ax.set_xlabel('Discount')
    ax.set_ylabel('Profit')
    ax.set_title('Discount vs profit (line items)')
    plt.tight_layout()
    fig.savefig(FIGURES_DIR / '13_discount_vs_profit_scatter.png', dpi=dpi, bbox_inches='tight')
    plt.close(fig)

    tp = frames['top_products'].head(10).set_index('Product Name')['Sales'].sort_values()
    fig, ax = plt.subplots(figsize=(8, 5))
    tp.plot(kind='barh', ax=ax, color='#2980b9')
    ax.set_xlabel('Sales')
    ax.set_title('Top 10 products by sales')
    plt.tight_layout()
    fig.savefig(FIGURES_DIR / '14_top10_products.png', dpi=dpi, bbox_inches='tight')
    plt.close(fig)

    last_dt = df['Order Date'].max()
    cutoff_dt = last_dt - timedelta(days=90)
    last_buy = df.groupby('Customer ID')['Order Date'].max()
    churn_y = last_buy.apply(lambda d: 1 if d < cutoff_dt else 0).rename('Churn')
    cust_x = df.groupby('Customer ID').agg(
        Total_Sales=('Sales', 'sum'),
        Total_Profit=('Profit', 'sum'),
        Order_Count=('Order ID', 'nunique'),
        Avg_Discount=('Discount', 'mean'),
        Avg_Quantity=('Quantity', 'mean'),
        Recency=('Order Date', lambda s: (last_dt - s.max()).days),
    )
    churn_ext = cust_x.join(churn_y)
    Xe = churn_ext.drop(columns=['Churn'])
    ye = churn_ext['Churn']
    if ye.nunique() > 1 and len(ye) >= 10:
        Xtr, Xte, ytr, yte = train_test_split(
            Xe, ye, test_size=0.2, random_state=42, stratify=ye
        )
        rf_e = RandomForestClassifier(
            n_estimators=200, max_depth=8, random_state=42, class_weight='balanced'
        )
        rf_e.fit(Xtr, ytr)
        prob_e = rf_e.predict_proba(Xte)[:, 1]
        roc = roc_auc_score(yte, prob_e)
        fi_e = pd.Series(rf_e.feature_importances_, index=Xe.columns).sort_values()
        fig, ax = plt.subplots(figsize=(7, 3.8))
        fi_e.plot(kind='barh', ax=ax, color='#27ae60')
        ax.set_title(f'Extended churn model: feature importance (ROC-AUC={roc:.3f})')
        plt.tight_layout()
        fig.savefig(FIGURES_DIR / '15_churn_extended_feature_importance.png', dpi=dpi, bbox_inches='tight')
        plt.close(fig)

    return FIGURES_DIR


def run_analysis():
    print("Starting E-Commerce Analysis...")

    print("Loading and cleaning data...")
    df = load_and_clean_data()
    print(f"  Loaded {len(df):,} rows")

    print("Calculating KPIs...")
    kpis = calculate_kpis(df)
    print(f"  Total Sales: ${kpis['total_sales']:,.2f}")
    print(f"  Total Profit: ${kpis['total_profit']:,.2f}")

    print("Creating RFM segments...")
    rfm = create_rfm_segments(df)
    print(f"  Segmented {len(rfm)} customers")

    print("Predicting churn...")
    churn_results = predict_churn(rfm)
    print(f"  Model accuracy: {churn_results['accuracy']:.1%}")

    print("Saving results...")
    frames = _export_frames(df, kpis, rfm, churn_results)
    out = save_analysis_outputs(df, kpis, rfm, churn_results, frames)
    print("Generating figures...")
    fig_out = save_all_figures(df, kpis, rfm, churn_results, frames)
    print("Analysis complete.")
    print(f"CSV outputs: {out}")
    print(f"Figures: {fig_out}")

    return df, kpis, rfm, churn_results

if __name__ == "__main__":
    run_analysis()