#!/usr/bin/python3
"""
This script lists all cities of a state given as an argument
from the DB hbtn_0e_4_usa.
"""
import MySQLdb


if __name__ == "__main__":
    from sys import argv
    dbconn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                             passwd=argv[2], database=argv[3])

    cursor = dbconn.cursor()

    cursor.execute("""
        SELECT cities.name FROM states
        JOIN cities ON states.id = cities.state_id
        WHERE states.name = '{}'
        ORDER BY cities.id""".format(argv[4].split()[0]))

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    dbconn.close()
