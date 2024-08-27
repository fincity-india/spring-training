from urllib.parse import quote
import pandas as pd
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Float, DateTime, TEXT
from sqlalchemy.exc import SQLAlchemyError
 
def LatestActivityImporter(csv_file_path,table_name,engine):
    

 
# Read a small chunk of the CSV to infer column types
   sample_chunk = pd.read_csv(csv_file_path, nrows=2000)
 
# Define table schema based on the CSV columns
   metadata = MetaData()
 
# Define the columns based on the provided schema
   columns = [
       Column('id', Integer),
       Column('opportunity_id', String(255)),
       Column('is_verified', Integer),
       Column('activity_id', String(255)),
       Column('activity_date', DateTime),
       Column('status', String(255)),
       Column('status_date', DateTime),
       Column('sub_status', String(255)),
       Column('sub_status_date', DateTime),
       Column('first_activity', String(255)),
       Column('first_activity_date', DateTime),
       Column('follow_up', String(255)),
       Column('follow_up_date', DateTime),
       Column('next_follow_up', String(255)),
       Column('next_follow_up_date', DateTime),
       Column('visit_proposed', String(255)),
       Column('visit_proposed_date', DateTime),
       Column('visit_confirmed', String(255)),
       Column('visit_confirmed_date', DateTime),
       Column('visit_done', String(255)),
       Column('visit_done_date', DateTime),
       Column('meeting_proposed', String(255)),
       Column('meeting_proposed_date', DateTime),
       Column('meeting_done', String(255)),
       Column('meeting_done_date', DateTime),
       Column('booking_done', String(255)),
       Column('booking_done_date', DateTime),
       Column('reassigned', String(255)),
       Column('reassigned_date', DateTime),
       Column('latest_comment', TEXT),
       Column('lost', String(255)),
       Column('opportunity_lost_reason', String(255)),
       Column('non_contactable', String(255)),
       Column('opportunity_non_contactable_reason', String(255)),
       Column('customer_called_count', Integer),
       Column('called_customer_count', Integer),
       Column('created_at', DateTime),
       Column('updated_at', DateTime),
       Column('is_active', Integer),
     ]
 
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
          i += 1
       except SQLAlchemyError as e:
          print(f"Error inserting data: {e}")
          break
 
   print("Finished loading the latest Activity Opportunity CSV file into the MySQL database.")