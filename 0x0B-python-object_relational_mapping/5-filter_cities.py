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
        JOIN cities ON cities.state_id = states.id
        WHERE states.name = '{}'
        ORDER BY cities.id ASC
        """.format(argv[4].split()[0]))

    citylist = []
    for row in cursor.fetchall():
        citylist.append(row)
    citystring = ', '.join(citylist)
    print(citystring)

    cursor.close()
    dbconn.close()
