#!/usr/bin/python3
# print all states from the database hbtn_0e_0_usa

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
    query = "SELECT * FROM states ORDER BY id ASC"
    c.execute(query)
    records = c.fetchall()

    if records:
        for row in records:
            print(row)

    c.close()
    db.close()
