import mysql.connector
from mysql.connector import errorcode


def create_database():
    try:
        # Connect to MySQL server
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password=112121
        )
        cursor = conn.cursor()

        # Attempt to create the database
        try:
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_DB_CREATE_EXISTS:
                print("Database 'alx_book_store' already exists.")
            else:
                print(f"Failed to create database: {err}")
        finally:
            cursor.close()
            conn.close()
    except mysql.connector.Error as err:
        print(f"Error: {err}")


if __name__ == "__main__":
    create_database()