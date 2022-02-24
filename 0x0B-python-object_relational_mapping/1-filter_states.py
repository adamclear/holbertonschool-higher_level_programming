#!/usr/bin/python3
"""
This script lists all states with a name that starts with 'N'
from the DB hbtn_0e_0_usa.
"""
import MySQLdb


if __name__ == "__main__":
    from sys import argv
    dbconn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                             passwd=argv[2], database=argv[3])

    cursor = dbconn.cursor()

    cursor.execute("""SELECT * FROM states
    WHERE name LIKE 'N%' ORDER BY id""")
    for row in cursor.fetchall():
        print(row)

    cursor.close()
    dbconn.close()
