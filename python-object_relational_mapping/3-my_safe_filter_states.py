#!/usr/bin/python3
"""Module to list states passed as argv from db hbtn_0e_0_usa"""
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
        SELECT * FROM states
        WHERE name = BINARY %s
        ORDER BY id ASC
    """, (state,))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
