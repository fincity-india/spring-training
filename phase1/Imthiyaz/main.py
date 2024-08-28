import os
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.exc import SQLAlchemyError
from creatingDatabase import databaseCredentials
from files import runEngine
from creatingDatabase import create_database

databaseName = "New"

create_database(databaseName)
 
user = databaseCredentials['user']
password = databaseCredentials['password']
host = databaseCredentials['host']
database = databaseName

engine = create_engine(f'mysql+mysqlconnector://{user}:{password}@{host}/{database}')

runEngine(engine)