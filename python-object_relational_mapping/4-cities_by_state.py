#!/usr/bin/python3
"""Module to list all cities from db hbtn_0e_4_usa"""
import sys
import MySQLdb


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

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
            SELECT c.id, c.name, s.name
            FROM cities c
            INNER JOIN states s
            ON s.id = c.state_id
            ORDER BY c.id ASC
            """)
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
