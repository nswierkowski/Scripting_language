import sys
import peewee as pe
import logging
from singleton_database import Database_name

file_name = "historia_przejazdow_2021-"
database_name = 'rentals_duration'

if len(sys.argv) >= 2:
    db = Database_name(sys.argv[1])
    if len(sys.argv) > 2:
        file_name = sys.argv[2]
else: 
    db = Database_name(database_name)


from database_classes import Stations, Rentals, read_db_from_file      

log_file_error = "/home/nikodem/Uczelnia/Języki_Skryptowe/lab10/log_file_error"
logging.basicConfig(filename=log_file_error, level=logging.ERROR)

database = pe.SqliteDatabase(f"{database_name}.sqlite3")
database.connect()

#read_db_from_file(f"../{file_name}")

def read_all():
    try:
        for i in range(8,13):
            print(i)
            if i < 10:
                read_db_from_file(f"../{file_name}0{i}.csv")
            else:
                read_db_from_file(f"../{file_name}{i}.csv")
    except KeyboardInterrupt:
        print(i)

read_all()