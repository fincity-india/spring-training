import logging
from urllib.parse import quote
from pathlib import Path
from database import get_engine, create_table
from file_processing import list_files, infer_table_schema, load_file_to_db, check_directory_structure
import pandas as pd
import sys

logging.basicConfig(level=logging.INFO)

def main():
    user = '****'
    password = quote('******') 
    host = '********'
    current_path = Path.cwd()
    logging.info(f"Current working directory: {current_path}")
    directory_path = current_path / 'venv/modlixdata1'
    if not directory_path.exists() or not directory_path.is_dir():
        logging.error(f"Directory '{directory_path}' does not exist or is not a directory.")
        sys.exit(1)
    
    if not check_directory_structure(directory_path):
        logging.error(f"Directory '{directory_path}' does not have the proper structure.")
        sys.exit(1)
    
    database = directory_path.name
    engine = get_engine(user, password, host, database)
    files = list_files(directory_path)
    
    if not files:
        logging.error("No files found in the directory.")
        sys.exit(1)
    for index, file_path in enumerate(files):
        file_path = Path(file_path)
        table_name = file_path.stem.replace('.', '_')
        sample_chunk = pd.read_csv(file_path, nrows=1000)
        columns = infer_table_schema(sample_chunk)
        create_table(engine, table_name, columns)
        load_file_to_db(engine, file_path, table_name)
        
        logging.info(f'Processed file {index + 1}/{len(files)}: {file_path.name}')

    logging.info(f"Finished loading {len(files)} files into the MySQL database '{database}'.")

if __name__ == "__main__":
    main()