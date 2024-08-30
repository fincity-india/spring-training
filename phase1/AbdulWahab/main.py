from urllib.parse import quote
from sqlalchemy import MetaData,create_engine 
from functionality import load_data,create_table,add_chunks_to_sql
import os
import logging
from pathlib import Path


def main():
    user = 'root'
    password = quote("Abdul@954")
    host = 'localhost' 
    main_folder = 'DatabaseFile'
    main_folder_path = Path(main_folder)
    if not main_folder_path.exists():
        raise FileNotFoundError
    folders = [folder for folder in main_folder_path.iterdir() if folder.is_dir()]
    if not folders:
        raise FileNotFoundError  
    database = os.path.basename(folders[0])
    files = [str(file) for file in folders[0].iterdir() if file.is_file()]
    engine = create_engine(f'mysql+mysqlconnector://{user}:{password}@{host}/{database}')
    metadata = MetaData()
    chunk_size=15000

    for file in files:
        table_name = os.path.splitext(os.path.basename(file))[0]
        columns=load_data(file)
        create_table(engine,metadata,table_name,columns)
        add_chunks_to_sql(engine,file,table_name,chunk_size)

if __name__ == "__main__":
    main()