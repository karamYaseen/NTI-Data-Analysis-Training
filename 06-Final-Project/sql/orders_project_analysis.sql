-- E-Commerce Marketplace Analysis - SQL Queries
-- Generated for project analysis

-- 1. Total Sales by Category
SELECT 
    Category,
    SUM(Sales) as Total_Sales,
    SUM(Profit) as Total_Profit,
    COUNT(*) as Order_Count
FROM sales_cleaned
GROUP BY Category
ORDER BY Total_Sales DESC;

-- 2. Monthly Sales Trend
SELECT 
    YEAR(Order_Date) as Year,
    MONTH(Order_Date) as Month,
    SUM(Sales) as Monthly_Sales,
    SUM(Profit) as Monthly_Profit
FROM sales_cleaned
GROUP BY YEAR(Order_Date), MONTH(Order_Date)
ORDER BY Year, Month;

-- 3. Top 10 Products by Sales
SELECT 
    Product_Name,
    SUM(Sales) as Total_Sales,
    SUM(Quantity) as Total_Quantity
FROM sales_cleaned
GROUP BY Product_Name
ORDER BY Total_Sales DESC
LIMIT 10;

-- 4. Customer Segmentation Analysis
SELECT 
    Segment,
    COUNT(*) as Customer_Count,
    AVG(Monetary_Value) as Avg_Order_Value,
    SUM(Monetary_Value) as Total_Value
FROM rfm_segments
GROUP BY Segment
ORDER BY Total_Value DESC;