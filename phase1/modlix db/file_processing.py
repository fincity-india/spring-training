import os
from pathlib import Path
import pandas as pd 
from sqlalchemy import Column, Integer, String, Float, BigInteger, DateTime, TEXT 
from sqlalchemy.exc import SQLAlchemyError
import logging

def list_csv_files(directory_path):
    supported_extensions = ('.csv', '.data.csv')
    return [file for file in directory_path.iterdir() if file.is_file() and file.suffix in supported_extensions]

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

def load_csv_to_db(engine, file_path, table_name):
    chunk_size = 15000
    i = 0
    for chunk in pd.read_csv(file_path, chunksize=chunk_size):
        try:
            chunk.to_sql(name=table_name, con=engine, if_exists='append', index=False)
            logging.info(f'Inserted chunk {i + 1} with {len(chunk)} rows into {table_name}')
            i += 1
        except SQLAlchemyError as e:
            logging.error(f"Error inserting data: {e}")
            break