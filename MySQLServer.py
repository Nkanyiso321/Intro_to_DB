import mysql.connector
from mysql.connector import Error

try:
    # Establish connection to MySQL server
    connection = mysql.connector.connect(
        host='localhost',    # Replace with your host
        user='your_username',  # Replace with your MySQL username
        password='your_password'  # Replace with your MySQL password
    )
    
    if connection.is_connected():
        cursor = connection.cursor()
        
        # Create database if it doesn't exist
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        
        print("Database 'alx_book_store' created successfully!")
        
except Error as e:
    # Enhanced exception handling with specific error message
    print(f"Error connecting to MySQL or creating database: {str(e)}")

finally:
    # Ensure connection and cursor are closed properly
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection closed.")
