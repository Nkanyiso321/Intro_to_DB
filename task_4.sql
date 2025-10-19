-- Script that prints the full description of the table books
-- from the database alx_book_store in the MySQL server.
-- The DESCRIBE or EXPLAIN statements are not allowed.

SELECT
    COLUMN_NAME AS Field,
    COLUMN_TYPE AS Type,
    IS_NULLABLE AS Null,
    COLUMN_KEY AS Key,
    COLUMN_DEFAULT AS Default,
    EXTRA AS Extra
FROM
    INFORMATION_SCHEMA.COLUMNS
WHERE
    TABLE_SCHEMA = (SELECT DATABASE())
    AND TABLE_NAME = 'books'
ORDER BY
    ORDINAL_POSITION;
