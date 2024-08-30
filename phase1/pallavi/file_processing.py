import logging
from pathlib import Path
from urllib.parse import quote
import pandas as pd
from database import get_engine, create_table
import os
from sqlalchemy import Column, Integer, String, Float, BigInteger, DateTime, TEXT
from sqlalchemy.exc import SQLAlchemyError

def list_files(directory_path):
    return [file for file in directory_path.iterdir() if file.is_file()]

def infer_table_schema(sample_chunk):
    columns = []
    for col_name in sample_chunk.columns:
        col_data = sample_chunk[col_name]
        if col_name in ['phone_number', 'whatsapp_number', 'alternate_phone_number']:
            columns.append(Column(col_name, String(150)))
        elif col_name in ['created_at_epoch', 'updated_at_epoch']:
            columns.append(Column(col_name, BigInteger))
        elif col_name in ['comment', 'latest_comment', 'metadata']:
            columns.append(Column(col_name, TEXT))
        elif pd.api.types.is_integer_dtype(col_data) and not col_data.isna().all():
            columns.append(Column(col_name, Integer))
        elif pd.api.types.is_float_dtype(col_data) and not col_data.isna().all():
            columns.append(Column(col_name, Float))
        elif pd.api.types.is_datetime64_any_dtype(col_data) and not col_data.isna().all():
            columns.append(Column(col_name, DateTime))
        else:
            columns.append(Column(col_name, String(255)))
    return columns

def load_file_to_db(engine, file_path, table_name):
    chunk_size = 15000
    for i, chunk in enumerate(pd.read_csv(file_path, chunksize=chunk_size)):
        try:
            chunk.to_sql(name=table_name, con=engine, if_exists='append', index=False)
            logging.info(f'Inserted chunk {i + 1} with {len(chunk)} rows into {table_name}')
        except SQLAlchemyError as e:
            logging.error(f"Error inserting data: {e}")
            raise

def check_directory_structure(directory_path):
    if not directory_path.is_dir():
        raise NotADirectoryError(f"{directory_path} is not a directory.")
    if not any(directory_path.iterdir()):
        raise FileNotFoundError(f"Directory '{directory_path}' is empty.")
try:
        cwd = Path(os.getcwd())
        logging.info(f"Current working directory: {cwd}")
        directory_path = cwd / 'venv'/ 'data'
        if not directory_path.exists():
            raise FileNotFoundError(f"Directory '{directory_path}' does not exist.")
        
        database = directory_path.name
        user = 'root'
        password = quote('A1b2c3@123')
        host = 'localhost'
        engine = get_engine(user, password, host, database)
        check_directory_structure(directory_path)
        csv_files = list_files(directory_path)
        for index, file_path in enumerate(csv_files):
            file_path = Path(file_path)
            table_name = file_path.stem.replace('.', '_')
            sample_chunk = pd.read_csv(file_path, nrows=1000)
            columns = infer_table_schema(sample_chunk)
            
            create_table(engine, table_name, columns)
            load_file_to_db(engine, file_path, table_name)
            
            logging.info(f'Processed file {index + 1}/{len(csv_files)}: {file_path.name}')

            logging.info(f"Finished loading {len(csv_files)} files into the MySQL database '{database}'.")
    
except Exception as e:
         logging.error(f"An error occurred: {e}")
         raise