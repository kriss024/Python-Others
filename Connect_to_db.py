import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode

try:
    connection = mysql.connector.connect(
                                        host="127.0.0.1",
                                        port=3306,
                                        user="user",
                                        password="userpassword",
                                        database="database"
                                    )
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("-- Connected to MySQL Server version ", db_Info)

        cursor = connection.cursor()

        cursor.execute("select database()")
        record = cursor.fetchone()
        print(f"You're connected to database: {record[0]}")

        cursor.execute("select curdate()")
        record = cursor.fetchone()
        print(f"Current date is: {record[0]}")

        cursor.close()

except Error as error:
    if error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("-- Something is wrong with your user name or password")
    elif error.errno == errorcode.ER_BAD_DB_ERROR:
        print("-- Database does not exist")
    else:
        print(error)

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("-- MySQL connection is closed")
