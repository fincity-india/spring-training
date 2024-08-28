from sqlalchemy import MetaData, Table, Column, Integer, String, Float, BigInteger, \
  DateTime, TEXT
#from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.exc import SQLAlchemyError
import pandas as pd
def loadData(engine):
    # Specify the paths of files you want to iterate over
    files=['Archive/activity.csv','Archive/opportunity.csv','Archive/opportunity_latest_activities.csv']
    #Specify the table names
    tables=['activity','opportunity','opportunity_latest_activity']
    # Iterate over the files in the directory
    count=0
    for file in files:
        # Define the name of the table in MySQL
        table_name = tables[count]
        count+=1
 
        # Read a small chunk of the CSV to infer column types
        sample_chunk = pd.read_csv(file, nrows=1000)
                # Define table schema based on the CSV columns
        metadata = MetaData()
 
        # You can customize the columns as needed
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
        chunk_size = 20000
        i = 0
        # Load CSV in chunks and insert into the MySQL table
        for chunk in pd.read_csv(file, chunksize=chunk_size):
            try:
                chunk.to_sql(name=table_name, con=engine, if_exists='append', index=False)
                print(f'Inserted {i} chunk with {len(chunk)} rows')
                i = i + 1
            except SQLAlchemyError as e:
                print(f"Error inserting data: {e}")
                break
 
    print("Finished loading the all CSV files into the MySQL database.")
