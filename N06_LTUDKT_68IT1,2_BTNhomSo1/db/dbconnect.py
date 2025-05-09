import mysql.connector
from mysql.connector import Error

try:
    mydb = mysql.connector.connect(
        host="localhost",      
        port=3306,
        database="lttkud",
        user="root",
        password="123456"
    )

    if mydb.is_connected():
        print("Kết nối tới MySQL thành công!")
    else:
        print("Kết nối thất bại.")

except Error as e:
    print("Lỗi khi kết nối:", e)

finally:
    if 'mydb' in locals() and mydb.is_connected():
        mydb.close()
        print("Đóng kết nối.")

def get_connection():
    return mysql.connector.connect(
        host="localhost",      
        port=3306,
        database="lttkud",
        user="root",
        password="123456"
    )