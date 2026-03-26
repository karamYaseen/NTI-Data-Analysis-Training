-- Sample SQL (PostgreSQL-style) — mirror of Python logic; load from sales_cleaned.csv into a table first
SELECT COUNT(*) AS row_count FROM sales;
SELECT SUM(CASE WHEN postal_code IS NULL THEN 1 ELSE 0 END) AS missing_postal FROM sales;

SELECT DATE_TRUNC('month', order_date) AS m, SUM(sales) AS sales, SUM(profit) AS profit
FROM sales GROUP BY 1 ORDER BY 1;

SELECT product_name, SUM(sales) AS sales FROM sales GROUP BY product_name ORDER BY sales DESC LIMIT 15;

SELECT category, SUM(sales) AS sales, SUM(profit) AS profit,
       SUM(profit) / NULLIF(SUM(sales), 0) AS margin
FROM sales GROUP BY category;
