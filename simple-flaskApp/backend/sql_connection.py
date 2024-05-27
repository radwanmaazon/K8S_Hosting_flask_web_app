import configparser
import mysql.connector
import os

__mydb = None
def get_sql_connection():
    global __mydb

    if __mydb is None:
        __mydb = mysql.connector.connect(
            host=os.getenv('DB_HOST'),
            port=os.getenv('DB_PORT'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            database=os.getenv('DB_NAME')
        )
        
    return __mydb
