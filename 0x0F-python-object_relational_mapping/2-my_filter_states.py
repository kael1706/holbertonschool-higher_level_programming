#!/usr/bin/python3
# print all registers that have the name value.
# use: <script> <user> <password> <db> <name>
# example: ./2-my_filter_states.py root root hbtn_0e_0_usa 'Arizona'

import MySQLdb
import sys

if __name__ == '__main__':
    u = sys.argv[1]
    p = sys.argv[2]
    mydb = sys.argv[3]
    name = sys.argv[4]

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
            "SELECT * FROM states WHERE BINARY "
            "name='{}' ORDER BY 'states.id' ASC;"
            )
    c.execute(query.format(name))
    records = c.fetchall()

    if records:
        for row in records:
            print(row)

    c.close()
    db.close()
