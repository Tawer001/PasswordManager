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
        print("Error when connecting to database! \n", e)

    return conn


def create_table(conn, db_table):
    try:
        cur = conn.cursor()
        cur.execute(db_table)

    except Error as e:
        print("Error when creating a table! \n", e)


def main():
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

    query = str(input("Type in your query from the following list [ SELECT = INSERT - UPDATE - DELETE]: "))
    column = str(input("Please select the conlumn name you want to edit from the following list [ username - password ]: "))
    row = str(input("Please select the id value you want to edit: "))


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


