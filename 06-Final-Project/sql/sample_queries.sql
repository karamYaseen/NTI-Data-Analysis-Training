-- Sample SQL Queries for E-Commerce Analysis

-- Basic data exploration
SELECT COUNT(*) as Total_Orders FROM sales_cleaned;
SELECT DISTINCT Category FROM sales_cleaned;
SELECT DISTINCT Sub_Category FROM sales_cleaned;

-- Sales performance
SELECT 
    Region,
    SUM(Sales) as Total_Sales,
    AVG(Sales) as Avg_Order_Value
FROM sales_cleaned
GROUP BY Region
ORDER BY Total_Sales DESC;

-- Customer analysis
SELECT 
    Customer_ID,
    COUNT(*) as Order_Count,
    SUM(Sales) as Total_Spent,
    MAX(Order_Date) as Last_Order_Date
FROM sales_cleaned
GROUP BY Customer_ID
ORDER BY Total_Spent DESC
LIMIT 20;

-- Product analysis
SELECT 
    Product_ID,
    Product_Name,
    SUM(Sales) as Total_Sales,
    SUM(Profit) as Total_Profit,
    SUM(Quantity) as Total_Quantity
FROM sales_cleaned
GROUP BY Product_ID, Product_Name
ORDER BY Total_Sales DESC
LIMIT 10;