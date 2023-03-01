from tkinter import *
from functools import partial
import sqlite3
from sqlite3 import Error
import os
import login_manager as lm
import home_page
import customtkinter


conn = None
tb_name = "safte_owner"


def register(conn, username, password):
    username = username.get()
    password = password.get()

    conn = sqlite3.connect(username + '_safet.db')

    sql_tb = f''' CREATE TABLE IF NOT EXISTS {tb_name} 
                    ( id INT PRIMARY KEY,
                      username TEXT NOT NULL,
                      password TEXT NOT NULL ); '''

    lm.connect_table(conn, sql_tb, tb_name)

    add_owner = f''' INSERT INTO {tb_name} 
                    ( id, username, password ) VALUES 
                    ( 1, ?, ? ) '''

    owner = (username, password)

    c = conn.cursor()
    c.execute(add_owner, owner)
    conn.commit()

    c.execute(f'SELECT * FROM {tb_name}')
    owner_name = c.fetchall()
    print(owner_name)

    print("Owner Registered")


def validate_login(conn, username, password):
    username = username.get()
    password = password.get()

    db_file_path = f'{username}_safet.db'

    if not os.path.exists(db_file_path):
        raise ValueError("Database file not found.")

    conn = sqlite3.connect(db_file_path)

    c = conn.cursor()
    c.execute(f'SELECT * FROM {tb_name} WHERE username=?', (username,))
    owner_pswd = c.fetchone()[2]
    conn.commit()

    print(owner_pswd)

    if password == owner_pswd:
        print("You're Validated")

        username_entry.configure(state='disabled')
        password_entry.configure(state='disabled')
        login_button.configure(state=DISABLED)
        register_button.configure(state='disabled')

        ctkWindow.destroy()

        print("window destroyed")

        home_page.run_app()

    else:
        print("username or password is wrong")


# window
customtkinter.set_appearance_mode('System')
customtkinter.set_default_color_theme('dark-blue')

ctkWindow = customtkinter.CTk()
ctkWindow.geometry('400x250')
ctkWindow.title('Login Form')

# username label and text enter box
Username_label = customtkinter.CTkLabel(ctkWindow, text="Username")
Username_label.place(relx=0.31, rely=0.25, anchor=customtkinter.CENTER)
username = StringVar()
username_entry = customtkinter.CTkEntry(ctkWindow, textvariable=username)
username_entry.place(relx=0.65, rely=0.25, anchor=customtkinter.CENTER)

# pasword label and password entry box
password_label = customtkinter.CTkLabel(ctkWindow, text="Password")
password_label.place(relx=0.31, rely=0.45, anchor=customtkinter.CENTER)
password = StringVar()
password_entry = customtkinter.CTkEntry(
    ctkWindow, textvariable=password, show="*")
password_entry.place(relx=0.65, rely=0.45, anchor=customtkinter.CENTER)

login_validation = partial(validate_login, conn, username, password)
register_owner = partial(register, conn, username, password)

# login button
login_button = customtkinter.CTkButton(
    ctkWindow, text="Login", command=login_validation)
login_button.place(relx=0.3, rely=0.7, anchor=customtkinter.CENTER)

# register button
register_button = customtkinter.CTkButton(
    ctkWindow, text="Register", command=register_owner)
register_button.place(relx=0.7, rely=0.7, anchor=customtkinter.CENTER)

ctkWindow.mainloop()
