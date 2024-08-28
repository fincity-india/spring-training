from sqlalchemy import create_engine
from activity_schema import activity_schema
from importer_function import importer_function
from latest_activity_schema import latest_activity_schema
from opportunity_schema import opportunity_schema


def main():
    user = 'root'
    password = 'root'
    host = 'localhost'
    database = 'FincityData'
    engine = create_engine(f'mysql+mysqlconnector://{user}:{password}@{host}/{database}')

    files = [
        ('opportunity.csv', 'data_of_opportunity', opportunity_schema),
        ('activity.csv', 'data_of_activity', activity_schema),
        ('opportunity_latest_activities.csv', 'data_of_latest_activity_opportunity', latest_activity_schema)
    ]

    for file, table_name, schema_func in files:
        importer_function(file, table_name, engine, schema_func)

if __name__ == "__main__":
    main()
