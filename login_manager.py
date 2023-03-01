import sqlite3
from sqlite3 import Error
import argon2


ph = argon2.PasswordHasher()


def connect_table(conn, sql_tb, tb_name):
    try:
        c = conn.cursor()
        c.execute(sql_tb)
        c.execute(f"SELECT * FROM {tb_name}")
        conn.commit()

        rows = c.fetchall()
        for row in rows:
            print(row)

    except Error as e:
        print(e)

# password hashing function


def hashpass(password):
    hashed_password = ph.hash(password)
    if ph.verify(hashed_password, password) is True:
        print(f"Hashed successfully! \n{hashed_password}")
    else:
        print("Hashing failed!")

    return hashed_password

# login


def login(conn, tb_name, username, password):
    c = conn.cursor()
    try:
        c.execute(
            f"SELECT password_hash FROM {tb_name} WHERE username = '{username}'")
        hashed_password = c.fetchone()[1]
        conn.commit()

        print(f"Logged in successfully! \n{hashed_password}")

        try:
            ph.verify(hashed_password, password)
        except argon2.exceptions.VerifyMismatchError:
            raise ValueError("Invalid username or password.")

    except argon2.exceptions.VerifyMismatchError:
        raise ValueError("Invalid username or password.")

    if ph.check_needs_rehash(hashed_password):
        c.execute(
            f"UPDATE tb SET password_hash = '{ph.hash(password)}' WHERE username = '{username}'")
        conn.commit()
        print(f"Rehashed successfully! \n{hashed_password}")

    elif not ph.check_needs_rehash(hashed_password):
        print("No need to rehash!")

    else:
        print("Failed to rehash!")

    c.close()
    # conn.close()


def login_page(conn, tb_name, username, password):
    pass
