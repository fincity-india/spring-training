from urllib.parse import quote
from sqlalchemy import create_engine
from functionality import loadData
# MySQL database credentials
user = 'root'
password = quote("A1b2c3@123")
host = 'localhost'  # e.g., 'localhost' or '127.0.0.1'
database = 'fincity1'
 
# Create a connection to the MySQL database
engine = create_engine(f'mysql+mysqlconnector://{user}:{password}@{host}/{database}')
 
loadData(engine)