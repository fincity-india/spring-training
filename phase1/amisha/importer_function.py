import logging
import pandas as pd
from sqlalchemy import MetaData, Table
from sqlalchemy.exc import SQLAlchemyError

def importer_function(csv_file_path, table_name, engine, schema_func):
    sample_chunk = pd.read_csv(csv_file_path, nrows=1000)
    metadata = MetaData()
    columns = schema_func(sample_chunk)
    table = Table(table_name, metadata, *columns)
    try:
        metadata.create_all(engine)
        logging.info(f"Table '{table_name}' is created or already exists.")
    except SQLAlchemyError as e:
        logging.error(f"Error creating table: {e}")

    chunk_size = 15000
    i = 0
    for chunk in pd.read_csv(csv_file_path, chunksize=chunk_size):
        try:
            chunk.to_sql(name=table_name, con=engine, if_exists='append', index=False)
            logging.info(f'Inserted {i} chunk with {len(chunk)} rows')
            i+1
        except SQLAlchemyError as e:
            logging.Error(f"Error inserting data: {e}")
            break

