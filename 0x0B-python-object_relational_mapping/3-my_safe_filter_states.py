#!/usr/bin/python3
"""
This script displays all values in the states table of DB
hbtn_0e_0_usa where name matches the argument given.
"""
import MySQLdb


if __name__ == "__main__":
    from sys import argv
    dbconn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                             passwd=argv[2], database=argv[3])

    cursor = dbconn.cursor()

    for char in argv[4]:
        if char.isalpha is False:
            statename = argv[4].split(char)[0]

    cursor.execute("""
        SELECT * FROM states
        WHERE name LIKE BINARY '{}'
        ORDER BY states.id ASC
        """.format(statename))

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    dbconn.close()
