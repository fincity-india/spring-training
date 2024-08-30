import logging
import os
from pathlib import Path
import mysql.connector
from mysql.connector import Error
import pandas as pd
from sqlalchemy import MetaData, Table, create_engine
from sqlalchemy.exc import SQLAlchemyError
from schema import schema_creator
import os
from dotenv import load_dotenv

load_dotenv()

user = os.getenv('USER')
password = os.getenv('PASSWORD')
host = os.getenv('HOST')
database = 'databasename'


def engine_creator():
    engine = create_engine(f'mysql+mysqlconnector://{user}:{password}@{host}/{database}')
    return engine

def create_table(csv_file_path, table_name, engine):
    sample_chunk = pd.read_csv(csv_file_path, nrows=1000)
    metadata = MetaData()
    columns = schema_creator(sample_chunk)
    table = Table(table_name, metadata, *columns)
    try:
        metadata.create_all(engine)
        logging.info(f"Table '{table_name}' is created or already exists.")
    except SQLAlchemyError as sql_alchemy_exception:
        logging.error(f"Error creating table: {sql_alchemy_exception}")
    return table

def insert_data(csv_file_path, table_name, engine, chunk_size=15000):
    for entries,chunk in enumerate(pd.read_csv(csv_file_path, chunksize=chunk_size)):
        try:
            chunk.to_sql(name=table_name, con=engine, if_exists='append', index=False)
            logging.info(f'Inserted chunk {entries} with {len(chunk)} rows')
        except SQLAlchemyError as sql_alchemy_exception:
            logging.error(f"Error inserting data: {sql_alchemy_exception}")
            break

def get_table_name():
    current_directory = Path(os.getcwd())
    main_folder_path = None
    for path in current_directory.rglob("*"):
        if path.is_dir() and path.name == "Databases":
            main_folder_path = path
            break  
    if not main_folder_path.exists():
        raise FileNotFoundError(f"The directory does not exist.")
    folders = [folder for folder in main_folder_path.iterdir() if folder.is_dir()]
    if not folders:
        raise FileNotFoundError("No subdirectories found in the specified main folder.")
    database = folders[0] 
    files = [str(file) for file in database.iterdir() if file.is_file()]
    # database_name = database.name.split('\\')
    # return database_name[0]
    return files


# def create_database(database_name):
#     try:
#         connection = mysql.connector.connect(
#             host= host,
#             user= user, 
#             password= password 
#             )
        
#         if connection.is_connected():
#             logging.info('Connected to MySQL server')

#             cursor = connection.cursor()
#             create_db_query = f"CREATE DATABASE {database_name}"
#             cursor.execute(create_db_query)
#             logging.info(f"Database `{database_name}` created successfully")

#     except Error as e:
#         logging.error(f"Error: {e}")

#     finally:
#         if connection.is_connected():
#             cursor.close()
#             connection.close()
#             logging.info("MySQL connection is closed")

    