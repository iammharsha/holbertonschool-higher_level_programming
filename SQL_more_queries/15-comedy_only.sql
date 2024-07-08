-- List all comedy shows
-- Each record should display: tv_shows.title
-- Results must be sorted in ascending order by the show title
SELECT
    s.title
FROM
    tv_shows s
INNER JOIN
    tv_show_genres sg
ON
    s.id = sg.show_id
INNER JOIN
    tv_genres g
ON
    g.id = sg.genre_id
WHERE
    g.name = "Comedy"
ORDER BY
    s.title
ASC;
