#!/usr/bin/python3
"""
This script list all state wth a name starting
where name matches arguement provided
"""
import MySQLdb
from sys import argv


def main():
    """
    Program Entrance for the.
    The program will not work if imported directly
    """
    db = MySQLdb.connect(user=argv[1], password=argv[2],
                         host='localhost', port=3306, database=argv[3])
    cursor = db.cursor()
    sql = "SELECT * FROM states WHERE REGEXP_LIKE(name, '{}', 'c')\
        ORDER BY states.id ASC".format(argv[4])
    cursor.execute(sql)
    rows = cursor.fetchall()
    for row in rows:
        print(row)


if __name__ == "__main__":
    main()
