#!/usr/bin/python3
"""
This script list all state wth a name starting with N from the database
"""
import MySQLdb
from sys import argv


def main():
    """
    Entrance of the programme, the main function
    """
    db = MySQLdb.connect(user=argv[1], password=argv[2],
                         host='localhost', port=3306, database=argv[3])
    cursor = db.cursor()
    sql = "SELECT * FROM states WHERE REGEXP_LIKE(name, '^N', 'c')\
          ORDER BY states.id ASC"
    cursor.execute(sql,)
    rows = cursor.fetchall()
    for row in rows:
        print(row)


if __name__ == "__main__":
    main()
