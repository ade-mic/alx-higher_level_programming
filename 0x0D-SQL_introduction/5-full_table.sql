-- prints the full description of the table first_table from database
-- hbrn_0c_0 in MYSQL server
SELECT * FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = 'hbtn_0c_0' AND TABLE_NAME = 'first_table';
