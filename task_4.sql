SELECT 
    COLUMN_NAME AS 'COLUMN NAME', 
    COLUMN_TYPE AS 'COLUMN TYPE', 
    IS_NULLABLE AS 'IS NULLABLE', 
    COLUMN_KEY AS 'COLUMN KEY', 
    COLUMN_DEFAULT AS 'COLUMN DEFAULT', 
    EXTRA AS 'EXTRA'
FROM 
    INFORMATION_SCHEMA.COLUMNS
WHERE 
    TABLE_SCHEMA = 'alx_book_store'
    AND TABLE_NAME = 'Books';