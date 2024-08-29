from urllib.parse import quote
from sqlalchemy import MetaData,create_engine 
from functionality import load_data,create_table,add_chunks_to_sql
import os
import logging
from pathlib import Path


def main():
    user = '********'
    password = quote("********")
    host = '********' 
    main_folder = 'files'
    main_folder_path = Path(main_folder)
    if not main_folder_path.exists():
        logging.error(f"The directory '{main_folder}' does not exist.")
    folders = [folder for folder in main_folder_path.iterdir() if folder.is_dir()]
    if not folders:
        logging.error("No subdirectories found in the specified main folder.")  
    database = os.path.basename(folders[0])
    files = [str(file) for file in folders[0].iterdir() if file.is_file()]
    engine = create_engine(f'mysql+mysqlconnector://{user}:{password}@{host}/{database}')
    metadata = MetaData()
    chunk_size=15000

    for file in files:
        table_name = os.path.splitext(os.path.basename(file))[0]
        load_data(file,table_name,metadata)
        create_table(engine,metadata,table_name)
        add_chunks_to_sql(engine,file,table_name,chunk_size)

if __name__ == "__main__":
    main()
