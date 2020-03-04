--  uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.
-- Requirements:
--  The tv_shows table contains only one record where title = Dexter (but the id can be different)
--  Each record should display: tv_genres.name
--  Results must be sorted in ascending order by the genre name
--  You can use only one SELECT statement
-- cat 14-my_genres.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows

SELECT tv_genres.name AS name
FROM tv_genres 
LEFT JOIN tv_show_genres
ON tv_show_genres.genre_id = tv_genres.id
LEFT JOIN tv_shows
ON tv_show_genres.show_id = tv_shows.id
WHERE title = 'Dexter'
ORDER BY name;
