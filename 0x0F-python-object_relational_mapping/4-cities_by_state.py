#!/usr/bin/python3
"""
a script that lists all cities from the database
the script takes 3 argument : mysql username, mysql password and database name
"""
# import libraries
import MySQLdb
from sys import argv


def main():
    """
    Main Entraince of the program
    """
    # create connection
    db = MySQLdb.connect(user=argv[1], password=argv[2],
                         host='localhost', port=3306, database=argv[3])
    cursor = db.cursor()
    sql = "SELECT cities.id, cities.name, states.name\
          FROM cities INNER JOIN states ON cities.state_id = states.id\
          ORDER BY cities.id ASC"
    cursor.execute(sql)
    rows = cursor.fetchall()
    for row in rows:
        print(row)


if __name__ == "__main__":
    main()
