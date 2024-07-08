-- List all shows and genre linked to the show
-- If a show doesn't have a genre, display NULL in the genre column
-- Each record should display: tv_shows.title - tv_genres.name
-- Results must be sorted in ascending order by the show title and genre name
SELECT
    s.title,
    g.name
FROM
    tv_shows s
LEFT JOIN
    tv_show_genres sg
ON
    s.id = sg.show_id
LEFT JOIN
    tv_genres g
ON
    g.id = sg.genre_id
ORDER BY
    s.title,
    g.name
ASC;
