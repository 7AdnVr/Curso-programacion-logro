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

UPDATE Customers
SET country = 'España'
WHERE customer_id = 4 OR first_name = 'Juan';

DELETE FROM Shippings
WHERE status = 'Delivered' and shipping_id > 200;

SELECT name, price, stock
FROM Products
ORDER BY stock DESC, price ASC;