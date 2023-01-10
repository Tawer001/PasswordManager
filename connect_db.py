# connect_db.py
import os
import sqlite3
from sqlite3 import Error
#import config_db


def create_connection(db_file):

    conn = None
    
    try:
        conn = sqlite3.connect(db_file)
        
        return conn

    except Error as e:
        print(e)

    return conn


def create_table(conn, db_table):
    try:
        cur = conn.cursor()
        cur.execute(db_table)

    except Error as e:
        print(e)


def main():
    '''db_dir = os.path.dirname(os.path.abspath(__file__))

    if not os.path.exists(db_dir):
        try:
            os.makedirs(db_dir)
        except OSError as e:
            # directory already exists
            pass'''

    db = "pm.db"


    tb_pwd_mngr = ''' CREATE TABLE IF NOT EXISTS password_manager (
                            pm_id integer PRIMARY KEY,
                            username text NOT NULL,
                            password text NOT NULL ); '''
    
    tb_autofill = ''' CREATE TABLE IF NOT EXISTS autofill (
                            af_id integer PRIMARY KEY,
                            first_name text,
                            last_name text,
                            mobile integer,
                            city text ); '''

    # conn = create_connection(db_dir)
    conn = create_connection(db)


    if conn is not None:
        create_table(conn, tb_pwd_mngr)
        create_table(conn, tb_autofill)

    else:
        print("Error! Cannot create database connection.")



if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)


