-- lists all genres from database hbtn_0d_tvshows and displays the number of show linked to each
SELECT tv_genres.name AS genre, COUNT(tv_show_genres.genre_id) AS number_of_shows FROM tv_shows JOIN tv_show_genres ON tv_shows.id=tv_show_genres.show_id JOIN tv_genres ON tv_show_genres.genre_id=tv_genres.id GROUP BY tv_genres.name HAVING number_of_shows > 0 ORDER BY number_of_shows DESC;
