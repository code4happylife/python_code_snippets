SELECT 
    last_name, first_name, points, (points + 10 )* 100 AS 'discount factor'
FROM
    customers;

SELECT DISTINCT state 
FROM customers;

SELECT 
    name, unit_price, (unit_price * 1.1) AS 'new_price'
FROM
    products;

SELECT *
FROM customers 
WHERE points > 3000;

SELECT *
FROM customers 
WHERE state = 'VA';

SELECT *
FROM customers 
WHERE state <> 'VA';

SELECT *
FROM customers 
WHERE state != 'VA';

SELECT *
FROM customers 
WHERE birth_date > '1990-01-01';

SELECT 
    *
FROM
    sql_store.orders
WHERE
    order_date >= '2019-01-01';


SELECT 
    *
FROM
    sql_store.customers
WHERE
    birth_date > '1990-01-01' AND points > 1000;


SELECT 
    *
FROM
    sql_store.customers
WHERE
    birth_date > '1990-01-01' OR (points > 1000 AND state='VA');


SELECT 
    *
FROM
    sql_store.customers
WHERE
    NOT (birth_date > '1990-01-01'
        OR points > 1000);

SELECT 
    *
FROM
    sql_store.order_items
WHERE
    order_id = 6
        AND quantity * unit_price > 30;


SELECT * 
FROM customers 
WHERE state = 'VA' OR state='GA' OR state = 'FL';


SELECT * 
FROM customers 
WHERE state IN ('VA','GA','FL');



SELECT * 
FROM customers 
WHERE state NOT IN ('VA','GA','FL');
