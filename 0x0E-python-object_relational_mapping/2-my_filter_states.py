#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user="{:s}".format(sys.argv[1]),
                         passwd="{:s}".format(sys.argv[2]),
                         db="{:s}".format(sys.argv[3]))

    cursor = db.cursor()
    cursor.execute(""" SELECT * FROM states
    ORDER BY states.id ASC """)

    for data in cursor.fetchall():
        if data[1] == sys.argv[4]:
            print(data)

    cursor.close()
    db.close()
