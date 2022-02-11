-- lists all genres from DB hbtn_0d_tvshows and the # of shows linked to each
SELECT tv_genres.name, COUNT(tv_show_genres.genre_id) number_of_shows
    FROM tv_genres
        INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
    GROUP BY tv_genres.name, tv_show_genres.genre_id
ORDER BY number_of_shows DESC;
