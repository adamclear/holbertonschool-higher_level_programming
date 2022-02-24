#!usr/bin/python3
"""
This module contains the method: filter_states.
"""
import MySQLdb


def filter_states():
    """
    This script lists all states with a name that starts with 'N'
    from the DB hbtn_0e_0_usa.
    """
    from sys import argv
    dbconn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                             passwd=argv[2], database=argv[3])

    cursor = dbconn.cursor()

    cursor.execute("SELECT * FROM states")
    for row in cursor.fetchall():
        print(row)

    cursor.close()
    dbconn.close()

if __name__ == "__main__":
    filter_states()