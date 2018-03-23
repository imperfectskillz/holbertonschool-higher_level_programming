#!/usr/bin/python3
"""
script listing all states
"""
from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    curse = db.cursor()
    curse.execute("SELECT * FROM states ORDER BY id ASC")
    for row in curse.fetchall():
        print(row)
    curse.close()
    db.close()
