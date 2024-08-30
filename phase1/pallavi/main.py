import logging
from urllib.parse import quote
import pandas as pd
from pathlib import Path
from database import get_engine, create_table
from file_processing import list_files, infer_table_schema, load_file_to_db, check_directory_structure
logging.basicConfig(level=logging.INFO)

def main():
    try:
        user = '****'
        password = quote('********')
        host = '**********'
        cwd = Path.cwd()
        logging.info(f"Current working directory: {cwd}")
        directory_path = cwd / 'venv' / 'data'
        
        if not directory_path.exists():
            raise FileNotFoundError(f"Directory '{directory_path}' does not exist.")

        check_directory_structure(directory_path)
        database = directory_path.name
        engine = get_engine(user, password, host, database)
        files = list_files(directory_path)
        
        for index, file_path in enumerate(files):
            table_name = file_path.stem.replace('.', '_')
            sample_chunk = pd.read_csv(file_path, nrows=1000)
            columns = infer_table_schema(sample_chunk)

            create_table(engine, table_name, columns)
            load_file_to_db(engine, file_path, table_name)
            
            logging.info(f'Processed file {index + 1}/{len(files)}: {file_path.name}')

        logging.info(f"Finished loading {len(files)} files into the MySQL database '{database}'.")

    except Exception as e:
        logging.error(f"An error occurred: {e}")
        raise

if __name__ == "__main__":
    main()
