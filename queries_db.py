# queries_db.py
import connect_db

def select(conn, *args):
    with conn.cursor() as cursor:
        cursor.execute(*args)
        return cursor.fetchall()

def insert(conn, *args):
    with conn.cursor() as cursor:
        cursor.execute(*args)

def update(conn, *args):
    with conn.cursor() as cursor:
        cursor.execute(*args)

def delete(conn, *args):
    with conn.cursor() as cursor:
        cursor.execute(*args)

def create_table(conn, *args):
    with conn.cursor() as cursor:
        cursor.execute(*args)

def alter_table(conn, *args):
    with conn.cursor() as cursor:
        cursor.execute(*args)

def drop_table(conn, *args):
    with conn.cursor() as cursor:
        cursor.execute(*args)

def truncate_table(conn, *args):
    with conn.cursor() as cursor:
        cursor.execute(*args)

def create_index(conn, *args):
    with conn.cursor() as cursor:
        cursor.execute(*args)

def drop_index(conn, *args):
    with conn.cursor() as cursor:
        cursor.execute(*args)

def create_view(conn, *args):
    with conn.cursor() as cursor:
        cursor.execute(*args)

def drop_view(conn, *args):
    with conn.cursor() as cursor:
        cursor.execute(*args)

