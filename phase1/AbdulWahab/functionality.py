from sqlalchemy import Table, Column, Integer, String, Float, BigInteger, \
  DateTime, TEXT
from sqlalchemy.exc import SQLAlchemyError
import logging
import pandas as pd


def load_data(file):

    sample_chunk = pd.read_csv(file, nrows=1000)
    columns = []
    for col_name in sample_chunk.columns:
        col_data = sample_chunk[col_name]
        if col_name == 'phone_number' or col_name == 'whatsapp_number' or col_name=='alternate_phone_number':
            columns.append(Column(col_name, String(150)))
        elif col_name == 'created_at_epoch' or col_name == 'updated_at_epoch':
            columns.append(Column(col_name, BigInteger))
        elif col_name == 'comment':
            columns.append(Column(col_name, TEXT))
        elif col_name == 'latest_comment':
            columns.append(Column(col_name, TEXT))
        elif col_name == 'metadata':
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
        
def create_table(engine,metadata,table_name,columns):
    table=Table(table_name,metadata,*columns)
    try:
        metadata.create_all(engine)
        logging.info(f"Table '{table_name}' is created or already exists.")
    except SQLAlchemyError as error:
        logging.error(f"Error creating table: {TypeError}")

def add_chunks_to_sql(engine,file,table_name,chunk_size):
    
    for count,chunk in enumerate(pd.read_csv(file, chunksize=chunk_size),start=1):
        try:
            chunk.to_sql(name=table_name, con=engine, if_exists='append', index=False)
            print(f'Inserted {count} chunk with {len(chunk)} rows')
        except SQLAlchemyError as error:
            logging.error(f"Error inserting data: {error}")
            break