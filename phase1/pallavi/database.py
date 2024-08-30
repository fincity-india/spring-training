from sqlalchemy import create_engine, MetaData, Table 

def get_engine(user, password, host, database):
    return create_engine(f'mysql+mysqlconnector://{user}:{password}@{host}/{database}')

def create_table(engine, table_name, columns):
    metadata = MetaData()
    table = Table(table_name, metadata, *columns)
    metadata.create_all(engine)
    print(f"Table '{table_name}' created or already exists.")
    return table

#database has no change