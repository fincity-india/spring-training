import mysql.connector
from mysql.connector import Error

databaseCredentials = {
    "user" : 'root',
    "password" : 'Syedimmu&97',
    "host" : 'localhost'
}

def create_database(database_name):
    try:
        connection = mysql.connector.connect(
            host= databaseCredentials['host'],
            user=databaseCredentials['user'], 
            password= databaseCredentials['password'] 
            )
        
        if connection.is_connected():
            print('Connected to MySQL server')

            cursor = connection.cursor()
            create_db_query = f"CREATE DATABASE {database_name}"
            cursor.execute(create_db_query)
            print(f"Database `{database_name}` created successfully")

    except Error as e:
        print(f"Error: {e}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

