#!/usr/bin/python3
"""
This script list all states from the database hbtn_0e_0_usa
"""
import MySQLdb
from sys import argv


def main():
    """
    The main function
    """
    db = MySQLdb.connect(user=argv[1], password=argv[2],
                         host='localhost', port=3306, database=argv[3])
    cursor = db.cursor()
    sql = "SELECT * FROM states ORDER BY states.id ASC"
    cursor.execute(sql)
    rows = cursor.fetchall()
    for row in rows:
        print(row)


if __name__ == "__main__":
    main()
