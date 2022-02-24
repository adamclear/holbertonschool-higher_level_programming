#!usr/bin/python3
"""
This module contains the method: select_states.
"""
import MySQLdb


def select_states():
    """
    This script lists all states from the DB hbtn_0e_0_usa.
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
    select_states()
