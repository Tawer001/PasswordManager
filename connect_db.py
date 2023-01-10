# connect_db.py
import os
import sqlite3
from sqlite3 import Error
import config_db


def create_connection(database):
    """ create a database connection to a database that resides
        in the memory
    """
    conn = None;
    
    try:
        conn = sqlite3.connect(database))

        print(f"SQLite3 version is {sqlite3.version}.")

        while True:
            break

    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


def main():
    