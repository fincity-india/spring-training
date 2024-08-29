import logging
from urllib.parse import quote
import os
from pathlib import Path
import pandas as pd
from database import get_engine, create_table
from file_processing import list_csv_files, infer_table_schema, load_csv_to_db
logging.basicConfig(level=logging.INFO)

def main():
    user = '****'
    password = quote('********')
    host = '*******'
    directory_path = Path('venv\modlixdata1')
    database = directory_path.name
    engine = get_engine(user, password, host, database)
    csv_files = list_csv_files(directory_path)
    
    for index, file_path in enumerate(csv_files):
        file_path = Path(file_path) 
        table_name = file_path.stem.replace('.', '_')

        sample_chunk = pd.read_csv(file_path, nrows=1000)
        columns = infer_table_schema(sample_chunk)
        
        create_table(engine, table_name, columns)
        load_csv_to_db(engine, file_path, table_name)
        
        logging.info(f'Processed file {index + 1}/{len(csv_files)}: {file_path.name}')

    logging.info(f"Finished loading {len(csv_files)} CSV files into the MySQL database '{database}'.")

if __name__ == "__main__":
    main()
