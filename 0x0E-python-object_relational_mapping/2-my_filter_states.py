#!/usr/bin/python3
import MySQLdb
import sys

db = MySQLdb.connect(host="localhost",
                     port=3306,
                     user="{:s}".format(sys.argv[1]),
                     passwd="{:s}".format(sys.argv[2]),
                     db="{:s}".format(sys.argv[3]))

cursor = db.cursor()
cursor.execute(""" SELECT * FROM states WHERE name=%s
ORDER BY states.id ASC """, (sys.argv[4],))

for data in cursor.fetchall():
    print(data)

cursor.close()
db.close()
