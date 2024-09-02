import mysql.connector
from mysql.connector import Error
import logging
import os
from dotenv import load_dotenv

load_dotenv()

databaseCredentials = {
    "user" : os.getenv('USER'),
    "password" : os.getenv('PASSWORD'),
    "host" : os.getenv('HOST')
}

def create_database(database_name):
    try:
        connection = mysql.connector.connect(
            host= databaseCredentials['host'],
            user=databaseCredentials['user'], 
            password= databaseCredentials['password'] 
            )
        
        if connection.is_connected():
            logging.info('Connected to MySQL server')

            cursor = connection.cursor()
            create_db_query = f"CREATE DATABASE {database_name}"
            cursor.execute(create_db_query)
            logging.info(f"Database `{database_name}` created successfully")

    except Error as e:
        logging.error(f"Error: {e}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            logging.info("MySQL connection is closed")
