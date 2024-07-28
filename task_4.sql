USE alx_book_store;
SELECT 
    COLUMN_NAME AS 'Column Name', 
    COLUMN_TYPE AS 'Column Type', 
    IS_NULLABLE AS 'Is Nullable', 
    COLUMN_KEY AS 'Key', 
    COLUMN_DEFAULT AS 'Default', 
    EXTRA AS 'Extra'
FROM 
    INFORMATION_SCHEMA.COLUMNS
WHERE 
    TABLE_SCHEMA = DATABASE() 
    AND TABLE_NAME = 'books';

-- Print the table constraints for books table
SELECT 
    CONSTRAINT_NAME AS 'Constraint Name', 
    CONSTRAINT_TYPE AS 'Constraint Type'
FROM 
    INFORMATION_SCHEMA.TABLE_CONSTRAINTS
WHERE 
    TABLE_SCHEMA = DATABASE() 
    AND TABLE_NAME = 'books';

-- Print the foreign key constraints for books table
SELECT 
    COLUMN_NAME AS 'Column Name', 
    REFERENCED_TABLE_NAME AS 'Referenced Table', 
    REFERENCED_COLUMN_NAME AS 'Referenced Column'
FROM 
    INFORMATION_SCHEMA.KEY_COLUMN_USAGE
WHERE 
    TABLE_SCHEMA = DATABASE() 
    AND TABLE_NAME = 'books' 
    AND REFERENCED_TABLE_NAME IS NOT NULL;