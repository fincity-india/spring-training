import logging
import os
from pathlib import Path
import pandas as pd
from sqlalchemy import MetaData, Table
from sqlalchemy.exc import SQLAlchemyError
from schema import schema_creator


def create_table(csv_file_path, table_name, engine):
    sample_chunk = pd.read_csv(csv_file_path, nrows=1000)
    metadata = MetaData()
    columns = schema_creator(sample_chunk)
    table = Table(table_name, metadata, *columns)
    try:
        metadata.create_all(engine)
        logging.info(f"Table '{table_name}' is created or already exists.")
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
    main_folder = 'phase1/amisha/Databases'
    main_folder_path = Path(main_folder)
    if not main_folder_path.exists():
        logging.error(f"The directory '{main_folder}' does not exist.")
    folders = [folder for folder in main_folder_path.iterdir() if folder.is_dir()]
    if not folders:
        logging.error("No subdirectories found in the specified main folder.")  
    database = folders[0] 
    files = [str(file) for file in database.iterdir() if file.is_file()]
    return files
    