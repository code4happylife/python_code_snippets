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
