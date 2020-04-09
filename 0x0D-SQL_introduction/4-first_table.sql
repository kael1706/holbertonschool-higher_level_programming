-- Creates a table called first_table in the current database in your
-- MySQL server.
-- cat 4-first_table.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
-- see changes:
-- cat 3-list_tables.sql | mysql -hlocalhost -uroot -p hbtn_0c_0

CREATE TABLE IF NOT EXISTS first_table(id INT, name VARCHAR(256));