-- SQL script to insert multiple rows into the 'customer' table of the alx_book_store database.

-- The database name is expected to be passed as an argument to the mysql command.
-- Example: mysql -u username -p alx_book_store < task_6.sql

INSERT INTO customer (
customer_id,
customer_name,
email,
address
) VALUES
(
2,
'Blessing Malik',
'bmalik@sandtech.com',
'124 Happiness Ave.'
),
(
3,
'Obed Ehoneah',
'eobed@sandtech.com',
'125 Happiness Ave.'
),
(
4,
'Nehemial Kamolu',
'nkamolu@sandtech.com',
'126 Happiness Ave.'
);
