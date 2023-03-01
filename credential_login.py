# test.py
import sys
import sqlite3
from sqlite3 import Error
import login_manager as lm


conn = None

def create_user(conn, tb_name, add_user):
    try:
        c = conn.cursor()
        c.execute(f"SELECT id FROM {tb_name} ORDER BY id DESC LIMIT 1;")
        last_user = c.fetchone()
        print(last_user, type(last_user))

        if last_user is None: 
            user_id = 1 
        else: 
            user_id = last_user[0] + 1 

        username = str(input("Add a username: "))
        password = str(input("Add a password: "))
        hashed_password = ''
        if password != '': 
            hashed_password = lm.hashpass(password)
        
        user_att = (user_id, username, hashed_password)
        
        if '' not in user_att: 
            c.execute(add_user, user_att); 
            print("New user added successfully!")
        conn.commit()

    except Error as e:
        print(e)

def sql_queries(conn):
    c = conn.cursor()
    c.execute()

def main():
    while True:
        selection = str(input("choose '0 to exit', '1 to connect': "))
        if selection == "1":
            conn = sqlite3.connect('user_info.db')
            
            tb_name = "login_info_tb"

            sql_tb = f''' CREATE TABLE IF NOT EXISTS {tb_name} 
                            ( id INTERGER PRIMARY KEY UNIQUE,
                              username TEXT NOT NULL,
                              password_hash TEXT NOT NULL ); '''
                        
            table = lm.connect_table(conn, sql_tb, tb_name)

            add_user = f''' INSERT INTO {tb_name} 
                        (id, username, password_hash) VALUES 
                        (?, ?, ?) '''

            user = create_user(conn, tb_name, add_user)

            c = conn.cursor()

            c.execute(f"SELECT * FROM {tb_name}")
            columns = [i[0] for i in c.description]

            rows = c.fetchall()
            for row in rows:
                print(row)

            username = input("Enter your username: ")
            password = input("Enter your password: ")

            credentials = lm.login(conn, tb_name, username, password)

            if credentials != '': 
                c.execute(f"SELECT * FROM {tb_name} where username = '{username}'")
                slctd = c.fetchall()
                print(f"you selected: \n{columns} \n{slctd}")
                user_id = slctd[0][0]
                username = slctd[0][1]
                hashed_password = slctd[0][2]
                
                print(f"{user_id}  |  {username}  |  {hashed_password}")

            else:
                print("You didn't enter anything!")

        elif selection == '0':
            exit()
            
        else:
            print("error")

if __name__ == '__main__':
    main()
                

