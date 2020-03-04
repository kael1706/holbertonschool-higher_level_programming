-- shows contained in hbtn_0d_tvshows that have at least one genre linked.
-- Requirements:
--  Each record should display: tv_shows.title - tv_show_genres.genre_id
--  Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
--  You can use only one SELECT statement.
-- cat 10-genre_id_by_show.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows

SELECT title, genre_id
FROM tv_shows
JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
ORDER BY title, genre_id;
