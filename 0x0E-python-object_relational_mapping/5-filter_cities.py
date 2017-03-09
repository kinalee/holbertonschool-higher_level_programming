#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])

    cmd = sys.argv[4].split(";")
    cursor = db.cursor()
    cursor.execute(""" SELECT * FROM cities JOIN states
    ON states.id = cities.state_id ORDER BY cities.id ASC """)

    state = list()
    for data in cursor.fetchall():
        if data[4] == cmd[0]:
            state.append(data[2])

    print(", ".join(state))
    cursor.close()
    db.close()
