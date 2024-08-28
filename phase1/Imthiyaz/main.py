from sqlalchemy import create_engine
from creatingDatabase import databaseCredentials
from files import runEngine
from creatingDatabase import create_database

newDatabaseName = "CSV_file_database"

create_database(newDatabaseName)
 
user = databaseCredentials['user']
password = databaseCredentials['password']
host = databaseCredentials['host']
database = newDatabaseName

csv_files = ['E:\\NXTWAVE\\databases\\activity.csv', 'E:\\NXTWAVE\\databases\\opportunity.csv', 'E:\\NXTWAVE\\databases\\opportunity_latest_activities.csv']

engine = create_engine(f'mysql+mysqlconnector://{user}:{password}@{host}/{database}')

runEngine(engine, csv_files)