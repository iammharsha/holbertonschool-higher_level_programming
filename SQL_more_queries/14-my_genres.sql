-- List all genres of the show Dexter
-- Each record should display: tv_genres.name
-- Results must be sorted in ascending order by the genre name
SELECT
    g.name
FROM
    tv_genres g
INNER JOIN
    tv_show_genres sg
ON
    sg.genre_id = g.id
INNER JOIN
    tv_shows s
ON
    s.id = sg.show_id
WHERE
    s.title = "Dexter"
ORDER BY
    g.name
ASC;
