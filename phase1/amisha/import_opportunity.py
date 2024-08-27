from urllib.parse import quote
import pandas as pd
from sqlalchemy import MetaData, Table, Column, Integer, String, Float, BigInteger, \
  DateTime, TEXT
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.exc import SQLAlchemyError
 
# MySQL database credentials

def OpportunityImporter(csv_file_path,table_name,engine):
   sample_chunk = pd.read_csv(csv_file_path, nrows=1000)
 
# Define table schema based on the CSV columns
   metadata = MetaData()
   columns = []
   for col_name in sample_chunk.columns:
      col_data = sample_chunk[col_name]
      if col_name == 'phone_number' or col_name == 'whatsapp_number' or col_name=='alternate_phone_number':
         columns.append(Column(col_name, String(150)))
      elif col_name == 'metadata':
         columns.append(Column(col_name, TEXT))
      elif pd.api.types.is_integer_dtype(col_data) and not col_data.isna().all():
         columns.append(Column(col_name, Integer))
      elif pd.api.types.is_float_dtype(col_data) and not col_data.isna().all():
         columns.append(Column(col_name, Float))
      elif pd.api.types.is_datetime64_any_dtype(col_data) and not col_data.isna().all():
         columns.append(Column(col_name, DateTime))
      else:
    # Default to String for other types
        columns.append(Column(col_name, String(255)))
 
# Create the table
   table = Table(table_name, metadata, *columns)
 
# Create the table in the database if it doesn't exist
   try:
      metadata.create_all(engine)
      print(f"Table '{table_name}' is created or already exists.")
   except SQLAlchemyError as e:
      print(f"Error creating table: {e}")
 
# Specify the chunk size (number of rows per chunk)
   chunk_size = 15000
   i = 0
# Load CSV in chunks and insert into the MySQL table
   for chunk in pd.read_csv(csv_file_path, chunksize=chunk_size):
      try:
         chunk.to_sql(name=table_name, con=engine, if_exists='append', index=False)
         print(f'Inserted {i} chunk with {len(chunk)} rows')
         i = i + 1
      except SQLAlchemyError as e:
         print(f"Error inserting data: {e}")
         break
 
   print("Finished loading the CSV file into the MySQL database.")