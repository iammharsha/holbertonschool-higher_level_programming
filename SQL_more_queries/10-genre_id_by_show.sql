-- List all shows that have at least one genre linked
-- List must be shown in ascending order of tv_shows.title and tv_show_genres.genre_id
SELECT 
    tv_shows.title,
    tv_show_genres.genre_id
FROM
    tv_shows
INNER JOIN
    tv_show_genres ON tv_show_genres.show_id = tv_shows.id
ORDER BY
    tv_shows.title, tv_show_genres.genre_id
ASC;
