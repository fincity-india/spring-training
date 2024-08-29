from urllib.parse import quote
from sqlalchemy import MetaData,create_engine 
from functionality import loadData,createTable,addChunksToSql
import os

main_folder = 'files'
folders = [name for name in os.listdir(main_folder) if os.path.isdir(os.path.join(main_folder, name))]

user = 'root'
password = quote("Abdul@954")
host = 'localhost'  
database=folders[0]
database_path=main_folder+"/"+database
files=[database_path+"/"+name for name in os.listdir(database_path)]
engine = create_engine(f'mysql+mysqlconnector://{user}:{password}@{host}/{database}')
metadata = MetaData()
chunk_size=15000

for file in files:
    table_name=file.split("/")[-1].split(".")[0]
    loadData(file,table_name,metadata)
    createTable(engine,metadata,table_name)
    addChunksToSql(engine,file,table_name,chunk_size)
