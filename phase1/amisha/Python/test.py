import os
from pathlib import Path

current_directory = Path(os.getcwd())
main_folder_path = None
for path in current_directory.rglob("*"):
    if path.is_dir() and path.name == "Databases":
        main_folder_path = path
        break  
if not main_folder_path.exists():
    raise FileNotFoundError(f"The directory does not exist.")
folders = [folder for folder in main_folder_path.iterdir() if folder.is_dir()]
if not folders:
    raise FileNotFoundError("No subdirectories found in the specified main folder.")
database = folders[0] 
files = [str(file) for file in database.iterdir() if file.is_file()]
print(files)
print("abc")