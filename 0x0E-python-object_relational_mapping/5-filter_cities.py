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
cursor.execute(""" SELECT cities.name FROM cities LEFT JOIN states
ON cities.state_id = states.id WHERE states.name=%s
ORDER BY cities.id ASC """, (cmd[0], ))

for data in cursor.fetchall():
    print(data)

cursor.close()
db.close()
