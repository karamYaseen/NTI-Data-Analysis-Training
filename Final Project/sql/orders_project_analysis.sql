/*
  E-Commerce Final Project — SQL Server (SSMS)
  Table: dbo.OrdersProject

  WARNING: Scripts below include ALTER / UPDATE / DELETE / SELECT INTO.
  Run on a copy or backup first. Adjust database/schema names if yours differ.
*/

-- =============================================================================
-- Preview: latest orders by fixed order date
-- =============================================================================
SELECT *
FROM dbo.OrdersProject
ORDER BY OrderDateFixed DESC;

-- =============================================================================
-- Check missing values (one row = counts per column)
-- =============================================================================
SELECT
    SUM(CASE WHEN Row_ID IS NULL THEN 1 ELSE 0 END) AS Missing_RowID,
    SUM(CASE WHEN Order_ID IS NULL THEN 1 ELSE 0 END) AS Missing_OrderID,
    SUM(CASE WHEN Order_Date IS NULL THEN 1 ELSE 0 END) AS Missing_OrderDate,
    SUM(CASE WHEN Ship_Date IS NULL THEN 1 ELSE 0 END) AS Missing_ShipDate,
    SUM(CASE WHEN Ship_Mode IS NULL THEN 1 ELSE 0 END) AS Missing_ShipMode,
    SUM(CASE WHEN Customer_ID IS NULL THEN 1 ELSE 0 END) AS Missing_CustomerID,
    SUM(CASE WHEN Customer_Name IS NULL THEN 1 ELSE 0 END) AS Missing_CustomerName,
    SUM(CASE WHEN Segment IS NULL THEN 1 ELSE 0 END) AS Missing_Segment,
    SUM(CASE WHEN Country_Region IS NULL THEN 1 ELSE 0 END) AS Missing_Country,
    SUM(CASE WHEN City IS NULL THEN 1 ELSE 0 END) AS Missing_City,
    SUM(CASE WHEN State IS NULL THEN 1 ELSE 0 END) AS Missing_State,
    SUM(CASE WHEN Postal_Code IS NULL THEN 1 ELSE 0 END) AS Missing_PostalCode,
    SUM(CASE WHEN Region IS NULL THEN 1 ELSE 0 END) AS Missing_Region,
    SUM(CASE WHEN Product_ID IS NULL THEN 1 ELSE 0 END) AS Missing_ProductID,
    SUM(CASE WHEN Category IS NULL THEN 1 ELSE 0 END) AS Missing_Category,
    SUM(CASE WHEN Sub_Category IS NULL THEN 1 ELSE 0 END) AS Missing_SubCategory,
    SUM(CASE WHEN Product_Name IS NULL THEN 1 ELSE 0 END) AS Missing_ProductName,
    SUM(CASE WHEN Sales IS NULL THEN 1 ELSE 0 END) AS Missing_Sales,
    SUM(CASE WHEN Quantity IS NULL THEN 1 ELSE 0 END) AS Missing_Quantity,
    SUM(CASE WHEN Discount IS NULL THEN 1 ELSE 0 END) AS Missing_Discount,
    SUM(CASE WHEN Profit IS NULL THEN 1 ELSE 0 END) AS Missing_Profit
FROM dbo.OrdersProject;

-- =============================================================================
-- Check duplicates by Order_ID
-- =============================================================================
SELECT Order_ID, COUNT(*) AS cnt
FROM dbo.OrdersProject
GROUP BY Order_ID
HAVING COUNT(*) > 1;

-- =============================================================================
-- Preview: parsed dates (dd/mm/yyyy style = 103)
-- =============================================================================
SELECT *,
       TRY_CONVERT(DATE, Order_Date, 103) AS OrderDateFixed,
       TRY_CONVERT(DATE, Ship_Date, 103) AS ShipDateFixed
FROM dbo.OrdersProject;

-- =============================================================================
-- Add fixed date columns (run once)
-- =============================================================================
ALTER TABLE dbo.OrdersProject
ADD OrderDateFixed DATE NULL,
    ShipDateFixed DATE NULL;

-- =============================================================================
-- Populate fixed dates
-- =============================================================================
UPDATE dbo.OrdersProject
SET OrderDateFixed = TRY_CONVERT(DATE, Order_Date, 103),
    ShipDateFixed = TRY_CONVERT(DATE, Ship_Date, 103);

-- =============================================================================
-- Repeat customer flag (query only)
-- =============================================================================
SELECT Customer_ID,
       COUNT(DISTINCT Order_ID) AS OrdersCount,
       CASE WHEN COUNT(DISTINCT Order_ID) > 1 THEN 1 ELSE 0 END AS IsRepeatCustomer
FROM dbo.OrdersProject
GROUP BY Customer_ID;

-- =============================================================================
-- Remove duplicate order rows (keep one row per Order_ID — review logic first)
-- =============================================================================
WITH CTE AS (
    SELECT *,
           ROW_NUMBER() OVER (PARTITION BY Order_ID ORDER BY Order_Date) AS rn
    FROM dbo.OrdersProject
)
DELETE FROM CTE
WHERE rn > 1;

-- =============================================================================
-- Active customer (last 90 days vs fixed anchor date)
-- =============================================================================
SELECT Customer_ID,
       CASE WHEN MAX(OrderDateFixed) >= DATEADD(DAY, -90, '2021-12-31') THEN 1 ELSE 0 END AS IsActive
INTO dbo.ActiveCustomer
FROM dbo.OrdersProject
GROUP BY Customer_ID;

-- =============================================================================
-- New customer flag (first order in Dec 2021)
-- =============================================================================
SELECT Customer_ID,
       MIN(OrderDateFixed) AS FirstOrder,
       CASE WHEN MONTH(MIN(OrderDateFixed)) = 12 AND YEAR(MIN(OrderDateFixed)) = 2021 THEN 1 ELSE 0 END AS IsNewCustomer
INTO dbo.NewCustomer
FROM dbo.OrdersProject
GROUP BY Customer_ID;

-- =============================================================================
-- Churned (bought Nov 2021, not Dec 2021) — simplified monthly definition
-- =============================================================================
SELECT Customer_ID,
       CASE
           WHEN MAX(CASE WHEN MONTH(OrderDateFixed) = 11 AND YEAR(OrderDateFixed) = 2021 THEN 1 ELSE 0 END) = 1
                AND MAX(CASE WHEN MONTH(OrderDateFixed) = 12 AND YEAR(OrderDateFixed) = 2021 THEN 1 ELSE 0 END) = 0
           THEN 1
           ELSE 0
       END AS IsChurned
INTO dbo.ChurnedCustomer
FROM dbo.OrdersProject
GROUP BY Customer_ID;

-- =============================================================================
-- Part B — KPIs
-- =============================================================================

-- Active customers (December 2021)
SELECT COUNT(DISTINCT Customer_ID) AS ActiveCustomers
FROM dbo.OrdersProject
WHERE MONTH(OrderDateFixed) = 12
  AND YEAR(OrderDateFixed) = 2021;

-- New customers (December 2021)
SELECT COUNT(*) AS NewCustomers
FROM (
    SELECT Customer_ID, MIN(OrderDateFixed) AS FirstOrderDate
    FROM dbo.OrdersProject
    GROUP BY Customer_ID
) AS FirstOrders
WHERE MONTH(FirstOrderDate) = 12
  AND YEAR(FirstOrderDate) = 2021;

-- Churn rate: Nov 2021 customers who did not buy in Dec 2021
SELECT CAST(COUNT(*) AS FLOAT) /
       NULLIF((
           SELECT COUNT(DISTINCT Customer_ID)
           FROM dbo.OrdersProject
           WHERE MONTH(OrderDateFixed) = 11
             AND YEAR(OrderDateFixed) = 2021
       ), 0) AS ChurnRate
FROM (
    SELECT DISTINCT Customer_ID
    FROM dbo.OrdersProject
    WHERE MONTH(OrderDateFixed) = 11
      AND YEAR(OrderDateFixed) = 2021
      AND Customer_ID NOT IN (
          SELECT DISTINCT Customer_ID
          FROM dbo.OrdersProject
          WHERE MONTH(OrderDateFixed) = 12
            AND YEAR(OrderDateFixed) = 2021
      )
) AS Churned;

-- Retention rate (share of customers with more than one order — definition per your brief)
SELECT CAST(SUM(CASE WHEN OrderCount > 1 THEN 1 ELSE 0 END) AS FLOAT) / NULLIF(COUNT(*), 0) AS RetentionRate
FROM (
    SELECT Customer_ID, COUNT(DISTINCT Order_ID) AS OrderCount
    FROM dbo.OrdersProject
    GROUP BY Customer_ID
) AS CustomerOrders;

-- Average order value (AOV)
SELECT SUM(Sales) / NULLIF(COUNT(DISTINCT Order_ID), 0) AS AverageOrderValue
FROM dbo.OrdersProject;

-- Customer lifetime value (average revenue per customer)
SELECT AVG(TotalRevenue) AS AvgCustomerLTV
FROM (
    SELECT Customer_ID, SUM(Sales) AS TotalRevenue
    FROM dbo.OrdersProject
    GROUP BY Customer_ID
) AS CustomerRevenue;

-- =============================================================================
-- Product & category performance
-- =============================================================================

-- Top 10 products
SELECT TOP 10
    Product_Name,
    SUM(Sales) AS TotalSales
FROM dbo.OrdersProject
GROUP BY Product_Name
ORDER BY TotalSales DESC;

-- Categories
SELECT Category, SUM(Sales) AS TotalSales
FROM dbo.OrdersProject
GROUP BY Category
ORDER BY TotalSales DESC;

-- Sub-categories
SELECT Sub_Category, SUM(Sales) AS TotalSales
FROM dbo.OrdersProject
GROUP BY Sub_Category
ORDER BY TotalSales DESC;

-- =============================================================================
-- RFM base (Frequency, Monetary, last purchase — add Recency in app layer or CTE)
-- =============================================================================
SELECT Customer_ID,
       COUNT(DISTINCT Order_ID) AS Frequency,
       SUM(Sales) AS Monetary,
       MAX(OrderDateFixed) AS LastPurchaseDate
FROM dbo.OrdersProject
GROUP BY Customer_ID;

-- Part C — build dashboards in Power BI / Metabase using these aggregates or linked tables
