#!/usr/bin/python3
"""Module to list all cities belonging to state from db hbtn_0e_4_usa"""
import sys
import MySQLdb


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state = sys.argv[4]

    conn = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database,
            charset="utf8"
        )
    cur = conn.cursor()
    cur.execute("""
            SELECT c.name
            FROM cities c
            INNER JOIN states s
            ON s.id = c.state_id
            WHERE s.name = BINARY %s
            ORDER BY c.id ASC
            """, (state,))
    query_rows = cur.fetchall()
    cities_list = [row[0] for row in query_rows]
    cities = ', '.join(cities_list)
    print(cities)
    cur.close()
    conn.close()
