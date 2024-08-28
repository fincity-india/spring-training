from urllib.parse import quote
from sqlalchemy import create_engine 
from functionality import loadData
user = 'root'
password = quote("Abdul@954")
host = 'localhost'  
database = 'fincity2'

engine = create_engine(f'mysql+mysqlconnector://{user}:{password}@{host}/{database}')

loadData(engine)