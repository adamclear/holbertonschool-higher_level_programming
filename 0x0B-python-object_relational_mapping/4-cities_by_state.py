#!/usr/bin/python3
"""
This script lists all cities in the DB hbtn_0e_4_usa along with
their corresponding state.
"""
import MySQLdb


if __name__ == "__main__":
    from sys import argv
    dbconn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                             passwd=argv[2], database=argv[3])

    cursor = dbconn.cursor()

    cursor.execute("""
        SELECT cities.id, cities.name, states.name
        FROM cities JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC""")

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    dbconn.close()
