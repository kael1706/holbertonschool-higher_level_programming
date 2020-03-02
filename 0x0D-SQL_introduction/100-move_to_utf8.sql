-- converts hbtn_0c_0 database to UTF8 (utf8mb4, collate utf8mb4_unicode_ci) in your MySQL server.
--  convert all of the following to UTF8:
--   Database hbtn_0c_0
--   Table first_table
--   Field name in first_table
-- cat 100-move_to_utf8.sql | mysql -hlocalhost -uroot -p
-- see changes:
-- cat 5-full_table.sql | mysql -hlocalhost -uroot -p hbtn_0c_0

USE hbtn_0c_0; 
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;