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
cursor.execute(""" SELECT * FROM states WHERE name=%s
ORDER BY states.id ASC""", (cmd[0],))

for data in cursor.fetchall():
    print(data)

cursor.close()
db.close()
