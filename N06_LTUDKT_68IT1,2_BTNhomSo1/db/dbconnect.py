import mysql.connector
from mysql.connector import Error

def get_connection():
    return mysql.connector.connect(
        host="localhost",      
        port=3306,
        database="lttkud",
        user="root",
        password="123456"
    )
