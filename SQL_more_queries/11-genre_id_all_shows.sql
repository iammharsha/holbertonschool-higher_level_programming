-- List all shows and it's genre
-- If it's not linked to a genre, it must be displayed as NULL
-- List must be shown in ascending order of tv_shows.title and tv_show_genres.genre_id
SELECT 
    tv_shows.title,
    tv_show_genres.genre_id
FROM
    tv_shows
LEFT JOIN
    tv_show_genres ON tv_show_genres.show_id = tv_shows.id
ORDER BY
    tv_shows.title, tv_show_genres.genre_id
ASC;
