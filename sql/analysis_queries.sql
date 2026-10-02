-- this file contains the queries that will be used for the analysis part of the project

-- =====================
-- for sales table:
-- =====================

-- calculate the number of sales lines and the total revenue:
select count(*) as total_sales,
       round(sum("Quantity" * "UnitPrice")::numeric, 2) as total_revenue
from sales;

-- calculate the total revenue for each country:
select "Country", round(sum("Quantity" * "UnitPrice")::numeric, 2) as total_revenue
from sales
group by "Country"
order by total_revenue desc;

-- select the 10 first sales sorting by total_price in descending order:
with tmp as (
    select "InvoiceNo", "StockCode", "Description", "Quantity", "UnitPrice", "Quantity"*"UnitPrice" as total_price
    from sales
)
select * from tmp
order by total_price desc
limit 10;

-- show the average basket (average invoice total) for each country:
with tmp as (
    select "InvoiceNo", "Country", sum("Quantity" * "UnitPrice") as basket
    from sales
    group by "InvoiceNo", "Country"
)
select "Country", round(avg(basket)::numeric, 2) as average_basket
from tmp
group by "Country"
order by average_basket desc;

-- count the nbr of unique customers:
select count(distinct "CustomerID") as unique_customers
from sales;

-- top 10 customers by revenue, with their number of orders:
with tmp as (
    select "CustomerID",
           sum("Quantity" * "UnitPrice") as total_ca,
           count(distinct "InvoiceNo") as nb_commandes
    from sales
    group by "CustomerID"
)
select * from tmp
order by total_ca desc
limit 10;

-- calculate the total revenue for each year and month:
select extract(year from "InvoiceDate") as year,
       extract(month from "InvoiceDate") as month,
       round(sum("Quantity" * "UnitPrice")::numeric, 2) as total_revenue
from sales
group by year, month
order by year, month;


-- =====================
-- for returns table (revenues):
-- =====================

-- count the number of returned sales:
select count(*) as total_returned_products
from revenues;

-- calculate the total of returned sales for each year and month:
select extract(year from "InvoiceDate") as year,
       extract(month from "InvoiceDate") as month,
       count(*) as total_returned_sales_year_month
from revenues
group by year, month
order by year, month;

-- calculate the product with the highest returned sales:
select "StockCode", count(*) as total_returned_sales_product
from revenues
group by "StockCode"
order by total_returned_sales_product desc
limit 1;

-- calculate the total of returned sales for each customer:
select "CustomerID", count(*) as total_returned_sales_customer
from revenues
group by "CustomerID"
order by total_returned_sales_customer desc;

-- calculate the total of returned sales for each country:
select "Country", count(*) as total_returned_sales_country
from revenues
group by "Country"
order by total_returned_sales_country desc;