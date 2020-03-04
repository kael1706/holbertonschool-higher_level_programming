-- lists all Comedy shows in the database hbtn_0d_tvshows.
-- Requirements:
-- The tv_genres table contains only one record where name = Comedy (but the id can be different)
-- Each record should display: tv_shows.title
-- Results must be sorted in ascending order by the show title
-- You can use only one SELECT statement
-- cat 15-comedy_only.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows

SELECT title
FROM tv_genres
LEFT JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id
LEFT JOIN tv_shows
ON tv_shows.id = tv_show_genres.show_id
WHERE name = "Comedy"
ORDER BY title;
