import logging
import os
<<<<<<< Updated upstream
from pathlib import Path
import pandas as pd
from sqlalchemy import MetaData, Table, create_engine
from sqlalchemy.exc import SQLAlchemyError
from schema import schema_creator


def engine_creator():
    user = '****'
    password = '****'
    host = '*****'
    database = 'FincityData'
    engine = create_engine(f'mysql+mysqlconnector://{user}:{password}@{host}/{database}')
    return engine

def create_table(csv_file_path, table_name, engine):
    sample_chunk = pd.read_csv(csv_file_path, nrows=1000)
    metadata = MetaData()
    columns = schema_creator(sample_chunk)
=======
import pandas as pd
from sqlalchemy import MetaData, Table
from sqlalchemy.exc import SQLAlchemyError
from schema import schemaCreator


def create_table(csv_file_path, table_name, engine):
    sample_chunk = pd.read_csv(csv_file_path, nrows=1000)
    metadata = MetaData()
    columns = schemaCreator(sample_chunk)
>>>>>>> Stashed changes
    table = Table(table_name, metadata, *columns)
    try:
        metadata.create_all(engine)
        logging.info(f"Table '{table_name}' is created or already exists.")
<<<<<<< Updated upstream
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
=======
    except SQLAlchemyError as e:
        logging.error(f"Error creating table: {e}")
    return table

def insert_data(csv_file_path, table_name, engine, chunk_size=15000):
    i = 0
    for chunk in pd.read_csv(csv_file_path, chunksize=chunk_size):
        try:
            chunk.to_sql(name=table_name, con=engine, if_exists='append', index=False)
            logging.info(f'Inserted chunk {i} with {len(chunk)} rows')
            i += 1
        except SQLAlchemyError as e:
            logging.error(f"Error inserting data: {e}")
            break

def get_table_name():
    main_folder = 'phase1\\amisha\\Databases'
    folders = [name for name in os.listdir(main_folder) if os.path.isdir(os.path.join(main_folder, name))]
 
    database=folders[0]
    database_path=main_folder+"\\"+database
    files=[database_path+"\\"+name for name in os.listdir(database_path)]
>>>>>>> Stashed changes
    return files
    