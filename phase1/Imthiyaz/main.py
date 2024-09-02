import os
from utils import create_table, engine_creator, get_table_name, insert_data, create_database


def main():
    engine = engine_creator()
    files, database_name = get_table_name()
    create_database(database_name)
    for file in files:
        table_name = os.path.splitext(os.path.basename(file))[0]
        create_table(file, table_name, engine)
        insert_data(file,table_name,engine)

if __name__ == "__main__":
    main()
