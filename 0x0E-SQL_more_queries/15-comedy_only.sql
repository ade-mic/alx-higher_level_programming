-- lists all comedy shows in the database hbtn_0d_tvshows
SELECT tv_shows.title FROM tv_genres  JOIN tv_show_genres ON tv_genres.id=genre_id INNER JOIN tv_shows ON tv_show_genres.show_id=tv_shows.id WHERE tv_genres.name='Comedy' ORDER BY tv_shows.title ASC;
