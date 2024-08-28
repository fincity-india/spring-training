import mysql.connector
from mysql.connector import Error

databaseCredentials = {
    "user" : 'root',
    "password" : 'Syedimmu&97',
    "host" : 'localhost'
}

def create_database(db_name):
    try:
        connection = mysql.connector.connect(
            host= databaseCredentials['host'],
            user=databaseCredentials['user'], 
            password= databaseCredentials['password'] 
            )
        
        if connection.is_connected():
            print('Connected to MySQL server')

            cursor = connection.cursor()
            create_db_query = f"CREATE DATABASE {db_name}"
            cursor.execute(create_db_query)
            print(f"Database `{db_name}` created successfully")

    except Error as e:
        print(f"Error: {e}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

