CREATE TABLE Products (
  product_id INT PRIMARY KEY,
  name VARCHAR(150),
  price INT,
  stock INT
);

ALTER TABLE Products
ADD COLUMN category VARCHAR(100);

ALTER TABLE Products
MODIFY COLUMN name VARCHAR(255);

INSERT INTO Products (product_id, name, price, stock, category)
VALUES
(1, 'Laptop', 1200, 10, 'Electronicos'),
(2, 'Mouse', 25, 50, 'Electronicos'),
(3, 'Teclado', 45, 30, 'Electronicos'),
(4, 'Silla', 150, 15, 'Muebles'),
(5, 'Escritorio', 300, 5, 'Muebles');

SELECT *
FROM Customers
WHERE age > 30
AND country != 'Mexico'
AND country != 'Colombia';

SELECT name, price, stock
FROM Products
ORDER BY stock DESC, price ASC;

SELECT SUM(amount)
FROM Orders
WHERE amount >= 2;

SELECT MAX(age), MIN(age)
FROM Customers;

SELECT COUNT(*)
FROM Orders
WHERE customer_id = 1
OR customer_id = 3
OR customer_id = 5;