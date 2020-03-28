#!/usr/bin/python3
# print cities related with a specific name of state.

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
            "SELECT cities.name FROM cities " +
            "JOIN states ON cities.state_id = states.id "
            "WHERE states.name = %s ORDER BY cities.id;"
            )
    c.execute(query, (name,))
    records = c.fetchall()
    print(", ".join([row[0] for row in records]))
    c.close()
    db.close()
