

SELECT Top 10*
FROM dbo.clean_superstore;

SELECT COUNT(*) AS Total_Rows
FROM dbo.clean_superstore;

SELECT SUM(Sales) AS Total_Sales
FROM dbo.clean_superstore;

SELECT SUM(Profit) AS Total_Profit
FROM dbo.clean_superstore;


SELECT Region, SUM(Sales) AS Total_Sales_Data
FROM dbo.clean_superstore
GROUP BY Region;
