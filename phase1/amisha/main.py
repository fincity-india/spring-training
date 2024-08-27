from sqlalchemy import create_engine

from import_activity import ActivityImporter
from import_latest_activity_opportunity import LatestActivityImporter
from import_opportunity import OpportunityImporter


user = 'root'
password = 'root'
host = 'localhost'  # e.g., 'localhost' or '127.0.0.1'
database = 'FincityData'
 
# Create a connection to the MySQL database
engine = create_engine(f'mysql+mysqlconnector://{user}:{password}@{host}/{database}')
ActivityImporter('activity.csv','data_of_activity',engine)
LatestActivityImporter('opportunity_latest_activities.csv','data_of_latest_activity_opportunity',engine)
OpportunityImporter('opportunity.csv','data_of_opportunity',engine)

