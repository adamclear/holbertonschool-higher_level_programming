#!usr/bin/python3
"""
This script lists all states from the DB hbtn_0e_0_usa.
"""
import MySQLdb


def select_states():
    from sys import argv
    dbconn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                             passwd=argv[2], database=argv[3])

    cursor = dbconn.cursor()

    cursor.execute("SELECT * FROM states")
    for states in cursor.fetchall():
        print(states)

    cursor.close()
    dbconn.close()


if __name__ == "__main__":
    select_states()
