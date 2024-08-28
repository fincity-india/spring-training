from urllib.parse import quote
from sqlalchemy import create_engine 
from functionality import loadData
user = 'root'
password = quote("Abdul@954")
host = 'localhost'  
database = 'fincity2'

engine = create_engine(f'mysql+mysqlconnector://{user}:{password}@{host}/{database}')

files=['Archive/activity.csv','Archive/opportunity.csv','Archive/opportunity_latest_activities.csv']
tables=['activity','opportunity','opportunity_latest_activity']

loadData(engine,files,tables)