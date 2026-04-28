-- Total Revenue by Region
create database sales;
use sales;

show tables;

describe sales_data;

SELECT Region, SUM(Sales) AS Total_Sales
FROM sales_data
GROUP BY Region;

-- Top 5 Customers
SELECT CustomerName, SUM(Sales) AS Total_Sales
FROM sales_data
GROUP BY CustomerName
ORDER BY Revenue DESC
LIMIT 5;

-- Profit by Category
SELECT Category, SUM(Profit) AS Profit
FROM sales_data
GROUP BY Category;