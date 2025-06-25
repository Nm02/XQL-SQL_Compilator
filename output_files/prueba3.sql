DROP TABLE old_orders;
UPDATE orders SET customer = 'archived' WHERE created_at < '2023-01-01';
SELECT order_id, customer FROM orders WHERE created_at > '2024-01-01';
CREATE TABLE orders (order_id INT, customer VARCHAR, total INT, created_at DATETIME);