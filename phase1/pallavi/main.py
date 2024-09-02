import logging
import os
from urllib.parse import quote
from pathlib import Path
from database import setup_database, create_table
from file_processing import list_files, infer_table_schema, load_file_to_db
logging.basicConfig(level=logging.INFO)

def main():
    user, password, host = '****', quote('********'), '*******'
    directory_path = Path.cwd() / 'data1'
    database_name = os.path.basename(directory_path)
    engine = setup_database(user, password, host, database_name)
    file_paths = list_files(directory_path)
    
    for index, file_path in enumerate(file_paths):
        table_name = file_path.stem.replace('.', '_')
        columns = infer_table_schema(file_path)
        create_table(engine, table_name, columns)
        load_file_to_db(engine, file_path, table_name)
        logging.info(f'Processed {index + 1}/{len(file_paths)}: {file_path.name}')

    logging.info(f"Loaded all files into the MySQL database '{database_name}'.")

if __name__ == "__main__":
    main()
