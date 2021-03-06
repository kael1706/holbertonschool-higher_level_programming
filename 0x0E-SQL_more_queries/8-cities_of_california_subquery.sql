-- show the cities of California that can be found
-- in the database hbtn_0d_usa.
-- Requirements:
--  The states table contains only one record where name = California
--  (but the id can be different, as per the example)
--  Results must be sorted in ascending order by cities.id
--  You are not allowed to use the JOIN keyword
--  cat 8-cities_of_california_subquery.sql | mysql -hlocalhost -uroot -p hbtn_0d_usa

SELECT id, name
FROM cities
WHERE state_id = (
    SELECT id 
    FROM states
    WHERE name = 'California'
)
ORDER BY id;
