#!/usr/bin/python3
"""
This script list all state wth a name
starting where name matches arguement provided
"""
import MySQLdb
from sys import argv


def main():
    """
    The main entrance to the program
    """
    db = MySQLdb.connect(user=argv[1], password=argv[2],
                         host='localhost', port=3306,
                         database=argv[3])
    cursor = db.cursor()
    sql = "SELECT * FROM states WHERE REGEXP_LIKE(name, %s, 'c')\
          ORDER BY states.id ASC"
    val = (argv[4],)
    cursor.execute(sql, val)
    rows = cursor.fetchall()
    for row in rows:
        print(row)


if __name__ == "__main__":
    main()
