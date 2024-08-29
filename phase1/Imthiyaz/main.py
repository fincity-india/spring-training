from sqlalchemy import create_engine
from files import runEngine
from creatingDatabase import create_database
import os
from dotenv import load_dotenv

load_dotenv()

def main():
    newDatabaseName = "test_database"

    create_database(newDatabaseName)
    
    user = os.getenv('USER')
    password = os.getenv('PASSWORD')
    host = os.getenv('HOST')
    database = newDatabaseName

    csv_files = ['E:\\NXTWAVE\\databases\\activity.csv', 'E:\\NXTWAVE\\databases\\opportunity.csv', 'E:\\NXTWAVE\\databases\\opportunity_latest_activities.csv']

    engine = create_engine(f'mysql+mysqlconnector://{user}:{password}@{host}/{database}')

    runEngine(engine, csv_files)

if __name__ == "__main__":
    main()