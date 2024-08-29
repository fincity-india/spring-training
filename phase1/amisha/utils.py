import logging
import os
import pandas as pd
from sqlalchemy import MetaData, Table
from sqlalchemy.exc import SQLAlchemyError
from schema import schemaCreator


def create_table(csv_file_path, table_name, engine):
    sample_chunk = pd.read_csv(csv_file_path, nrows=1000)
    metadata = MetaData()
    columns = schemaCreator(sample_chunk)
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
    main_folder = 'phase1\\amisha\\Databases'
    folders = [name for name in os.listdir(main_folder) if os.path.isdir(os.path.join(main_folder, name))]
 
    database=folders[0]
    database_path=main_folder+"\\"+database
    files=[database_path+"\\"+name for name in os.listdir(database_path)]
    return files
    