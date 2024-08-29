import os
from sqlalchemy import create_engine
from utils import create_table, get_table_name, insert_data


def main():
    user = '****'
    password = '****'
    host = '****'
    database = 'FincityData'
    engine = create_engine(f'mysql+mysqlconnector://{user}:{password}@{host}/{database}')
    
    files = get_table_name()
    for file in files:
        table_name = os.path.splitext(os.path.basename(file))[0]
        create_table(file, table_name, engine)
        insert_data(file,table_name,engine)

if __name__ == "__main__":
    main()
