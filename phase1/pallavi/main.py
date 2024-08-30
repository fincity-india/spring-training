import logging
from urllib.parse import quote
import os
from pathlib import Path
from database import get_engine, create_table
logging.basicConfig(level=logging.INFO)
from file_processing import list_files,infer_table_schema,load_file_to_db
from file_processing import check_directory_structure

def main():
        database = 'data'
        user = '****'
        password = quote('******')
        host = '********'
        cwd = Path(os.getcwd())
        directory_path = cwd / 'data'
        engine = get_engine(user, password, host, database)