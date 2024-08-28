import pandas as pd
from sqlalchemy import engine, MetaData, Table, Column, Integer, String, Float, BigInteger, \
  DateTime, TEXT
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.exc import SQLAlchemyError

def runEngine(engine):
    csv_file_names = ['E:\\NXTWAVE\\databases\\activity.csv', 'E:\\NXTWAVE\\databases\\opportunity.csv', 'E:\\NXTWAVE\\databases\\opportunity_latest_activities.csv']
    for filename in csv_file_names:
            csv_file_path = filename
            table_name = filename[21:len(filename)-4]
            sample_chunk = pd.read_csv(csv_file_path, nrows=1000)
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
            
            chunk_size = 15000
            i = 0
            for chunk in pd.read_csv(csv_file_path, chunksize=chunk_size):
                try:
                    chunk.to_sql(name=table_name, con=engine, if_exists='append', index=False)
                    print(f'Inserted {i} chunk with {len(chunk)} rows')
                    i = i + 1
                except SQLAlchemyError as e:
                    print(f"Error inserting data: {e}")
                    break
    print("Finished loading the all CSV files into the MySQL database.")