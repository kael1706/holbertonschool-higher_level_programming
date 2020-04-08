#!/usr/bin/python3
# print cities with the states.

import MySQLdb
import sys

if __name__ == '__main__':
    u = sys.argv[1]
    p = sys.argv[2]
    mydb = sys.argv[3]

    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=u,
        password=p,
        db=mydb,
        charset='utf8'
    )

    c = db.cursor()
    query = (
            "SELECT cities.id, cities.name, states.name "
            "FROM cities LEFT JOIN states "
            "ON cities.state_id = states.id"
            )
    c.execute(query)
    records = c.fetchall()

    if records:
        for row in records:
            print(row)

    c.close()
    db.close()
