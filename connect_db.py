'''import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='Electronics',
                                         user='pynative',
                                         password='pynative@#29')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")'''



'''# connect_db.py 
import utils
import config_db

os = utils.import_module('os')
sql_conn = utils.import_module('mysql.connector')

try:
    # Create a connection pool
    connection = sql_conn.connect(
        host = os.environ['DB_HOST'],
        user = os.environ['DB_USER'],
        password = os.environ['DB_PASSWORD'],
        database = os.environ['DB_DATABASE'],
        autocommit = True,
    )
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")'''

