#!/usr/bin/python3
"""
script that takes in the name of a state as an argument and lists all cities of that state
the script takes 4 argument : mysql username, mysql password, database name, state name 
"""
# import libraries
import MySQLdb
from sys import argv
# create connection
db = MySQLdb.connect(user=argv[1], password=argv[2],
                     host='localhost', port=3306, database=argv[3])
cursor = db.cursor()
sql = "SELECT cities.name FROM cities INNER JOIN states ON cities.state_id = states.id WHERE states.name = %s ORDER BY cities.id ASC"
val = (argv[4],)
cursor.execute(sql, val)
rows = cursor.fetchall()
result = sum(rows, ())
results = ', '.join(result)
print(results)
