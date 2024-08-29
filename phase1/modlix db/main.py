from urllib.parse import quote
import os
import pandas as pd
from database import get_engine, create_table
from file_processing import list_csv_files, infer_table_schema, load_csv_to_db

def main():
    user = 'root'
    password = quote('A1b2c3@123')
    host = 'localhost'
    directory_path = 'venv\\modlixdata1' 
    database = os.path.basename(directory_path)
    engine = get_engine(user, password, host, database)
    csv_files = list_csv_files(directory_path)
    
    for filename in csv_files:
        file_path = os.path.join(directory_path, filename)
        table_name = filename[:-4]  # Removing the '.csv' extension

        sample_chunk = pd.read_csv(file_path, nrows=1000)
        columns = infer_table_schema(sample_chunk)
        
        create_table(engine, table_name, columns)
        load_csv_to_db(engine, file_path, table_name)
    
    print(f"Finished loading {len(csv_files)} CSV files into the MySQL database '{database}'.")

if __name__ == "__main__":
    main()
