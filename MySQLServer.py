#!/usr/bin/python3
"""
A script that connects to a MySQL server and creates the database
hbtn_0c_0.
"""

import mysql.connector
from mysql.connector import Error
import sys

def create_database():
    """
    Connects to MySQL server and creates the alx_book_store database.
    Handles connection errors and ensures the script doesn't fail if
    the database already exists.
    """
    db_connection = None
    cursor = None
    
    try:
        # Attempt to connect to the MySQL server
        # *** Update with your MySQL credentials ***
        db_connection = mysql.connector.connect(
            host="localhost",
            user="your_username",    # e.g., 'root'
            password="your_password" # Your MySQL password
        )
        
        cursor = db_connection.cursor()
        
        # Create the database using "IF NOT EXISTS" to satisfy the requirement
        # that the script should not fail if the DB already exists.
        # This command avoids using "SELECT" or "SHOW".
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        
        # Print the required success message
        print("Database 'alx_book_store' created successfully!")

    except Error as err:
        # Handle errors, such as connection failures
        print(f"Error: {err}")
        
    finally:
        # Ensure the database connection is properly closed
        if cursor:
            cursor.close()
        if db_connection and db_connection.is_connected():
            db_connection.close()

if __name__ == "__main__":
    create_database()
