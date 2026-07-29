-- ==========================================
-- TASK 3: SQL DATA ANALYSIS
-- Author: Eman Iqbal
-- Database: ecommerce_data.db (Table: orders)
-- ==========================================

-- Query 1: Referral Source Performance (Combined Aggregations)
SELECT 
    ReferralSource,
    COUNT(OrderID) AS Total_Orders,
    SUM(Quantity) AS Total_Units_Sold,
    SUM(TotalPrice) AS Total_Revenue,
    ROUND(AVG(TotalPrice), 2) AS Avg_Order_Value
FROM orders
WHERE TotalPrice > 100 
GROUP BY ReferralSource
ORDER BY Total_Revenue DESC;

-- Query 2: Total Orders by Order Status
SELECT OrderStatus, COUNT(OrderID) AS Total_Orders
FROM orders
GROUP BY OrderStatus
ORDER BY Total_Orders DESC;

-- Query 3: Total Revenue by Product
SELECT Product, SUM(Quantity) AS Units_Sold, SUM(TotalPrice) AS Total_Revenue
FROM orders
GROUP BY Product
ORDER BY Total_Revenue DESC;

-- Query 4: Average Order Value by Payment Method
SELECT PaymentMethod, ROUND(AVG(TotalPrice), 2) AS Avg_Order_Value, COUNT(OrderID) AS Total_Transactions
FROM orders
GROUP BY PaymentMethod
ORDER BY Avg_Order_Value DESC;

-- Query 5: Lost Revenue Analysis (Cancelled & Returned)
SELECT Product, OrderStatus, COUNT(OrderID) AS Affected_Orders, SUM(TotalPrice) AS Lost_Revenue
FROM orders
WHERE OrderStatus IN ('Cancelled', 'Returned')
GROUP BY Product, OrderStatus
ORDER BY Lost_Revenue DESC;

-- Query 6: High-Value Delivered Orders
SELECT OrderID, Product, TotalPrice, OrderStatus
FROM orders
WHERE TotalPrice > 1000 AND OrderStatus = 'Delivered'
ORDER BY TotalPrice DESC;
