/*
create table customers(
 customer_id int generated always as identity primary key,
 name varchar(100),
 city varchar(100)
); */

/*
insert into customers(name,city) values
 ('Aman','Mumbai'),
  ('Priya','Delhi'),
  ('Rahul','Mumbai'),
  ('Sneha','Pune'),
  ('Vikram','Delhi'),
  ('Neha','Kolkata'); */

/* select * from customers; */

/*
create table orders(
 order_id int primary key,
 customer_id int,
 amount int,
 status varchar(100),

 foreign key (customer_id) references customers(customer_id)
);
*/

/*
insert into orders values
	(101,1,500,'Delivered'),
	(102,2,1200,'Delivered'),
	(103,1,800,'Cancelled'),
	(104,3,1500,'Delivered'),
	(105,2,450,NULL),
	(106,5,2000,'Delivered'),
	(107,4,700,'Cancelled'),
	(108,3,850,'Delivered');
	*/

/* B1	*/
/*
SELECT c.city, SUM(o.amount) AS total_order_amount
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id
GROUP BY c.city
HAVING SUM(o.amount) > 1000
ORDER BY total_order_amount DESC; */

/* output :
mumbai 3650
delhi 3650 */

/* C1 */
/*
WITH cust_total AS (
    SELECT
        c.customer_id,
        c.name,
        SUM(o.amount) AS total_amount
    FROM customers c
    JOIN orders o
        ON c.customer_id = o.customer_id
    WHERE o.status <> 'Cancelled'
       OR o.status IS NULL
    GROUP BY c.customer_id, c.name
)
SELECT *
FROM cust_total
WHERE total_amount > (
    SELECT AVG(total_amount)
    FROM cust_total
)
ORDER BY total_amount ASC;
*/

/* output :
3 , rahul , 2350
5, vikram , 2000
2,priya,1650 */