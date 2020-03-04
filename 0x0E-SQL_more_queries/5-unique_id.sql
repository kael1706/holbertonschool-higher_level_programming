-- creates the table unique_id on your MySQL server.
-- unique_id description:
--  id INT with the default value 1 and must be unique.
--  name VARCHAR(256)
-- cat 5-unique_id.sql | mysql -hlocalhost -uroot -p hbtn_0d_2

CREATE TABLE IF NOT EXISTS unique_id(
    id INT UNIQUE DEFAULT 1,
    name VARCHAR(256)
);
