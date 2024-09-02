from sqlalchemy import create_engine, MetaData, Table, text

def setup_database(user, password, host, database_name):
    engine = create_engine(f'mysql+mysqlconnector://{user}:{password}@{host}')
    with engine.connect() as connection:
        connection.execute(text(f"CREATE DATABASE IF NOT EXISTS {database_name}"))
    return create_engine(f'mysql+mysqlconnector://{user}:{password}@{host}/{database_name}')

def create_table(engine, table_name, columns):
    metadata = MetaData()
    table = Table(table_name, metadata, *columns)
    metadata.create_all(engine, checkfirst=True)
