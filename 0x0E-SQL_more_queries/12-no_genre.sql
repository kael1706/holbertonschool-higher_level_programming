-- lists all shows contained in hbtn_0d_tvshows without a genre linked.
-- Requirements:
-- Each record should display: tv_shows.title - tv_show_genres.genre_id
-- Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
-- You can use only one SELECT statement
-- cat 12-no_genre.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
WHERE genre_id IS NULL
ORDER BY title;
