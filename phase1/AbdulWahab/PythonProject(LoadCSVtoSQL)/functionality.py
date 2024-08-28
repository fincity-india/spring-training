from sqlalchemy import MetaData, Table, Column, Integer, String, Float, BigInteger, \
  DateTime, TEXT
from sqlalchemy.exc import SQLAlchemyError
import pandas as pd
def loadData(engine):
    files=['Archive/activity.csv','Archive/opportunity.csv','Archive/opportunity_latest_activities.csv']
    tables=['activity','opportunity','opportunity_latest_activity']
    count=0
    for file in files:
        table_name = tables[count]
        count+=1
 
        sample_chunk = pd.read_csv(file, nrows=1000)
            
        metadata = MetaData()
 
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
       
        table = Table(table_name, metadata, *columns)
       
        try:
            metadata.create_all(engine)
            print(f"Table '{table_name}' is created or already exists.")
        except SQLAlchemyError as e:
            print(f"Error creating table: {e}")
       

        chunk_size = 20000
        i = 0

        for chunk in pd.read_csv(file, chunksize=chunk_size):
            try:
                chunk.to_sql(name=table_name, con=engine, if_exists='append', index=False)
                print(f'Inserted {i} chunk with {len(chunk)} rows')
                i = i + 1
            except SQLAlchemyError as e:
                print(f"Error inserting data: {e}")
                break
 
