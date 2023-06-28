from peewee import *
import sys
from singleton_database import Database_name
import logging
import datetime

obj_represent_name_of_db = Database_name('default_database_name')
database = SqliteDatabase(f"{obj_represent_name_of_db._name}.sqlite3") 

class Stations(Model):
    station_id = PrimaryKeyField()
    station_name = CharField()

    def __str__(self):
        return f"{self.station_name}"
    
    class Meta:
        database = database
        table_name = 'Stations'


class Rentals(Model):
    rentals_id = IntegerField(unique=True)
    bike_number = IntegerField()
    start_time = DateTimeField()
    end_time = DateTimeField()
    rental_station = ForeignKeyField(Stations)
    return_station = ForeignKeyField(Stations)
    duration = IntegerField()

    class Meta:
        database = database
        table_name = 'Rentals'

def create_tables():
    database.connect()
    database.create_tables([Stations, Rentals])

#############################################
# EXERCISE 2
#############################################

def new_station(new_station_name):
    query = Stations.select().where(Stations.station_name == new_station_name)
    if query.exists():
        record = query.first()
    else:
        record = Stations.create(station_name=new_station_name)
        record.save()
    
    return record

def new_rental(data):
    try:
        rental = Rentals.create(rentals_id=data[0], 
                           bike_number=data[1], 
                           start_time=data[2], 
                           end_time=data[3], 
                           rental_station=new_station(data[4]).station_id, 
                           return_station=new_station(data[5]).station_id,
                           duration=data[6])
        rental.save()
    except IntegrityError:
        logging.error("repeating ID: " + str(data))

def read_db_from_file(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        header = True
        for line in lines:
            if header:
                header = False
            else:
                data = line.strip().split(',')
                new_rental(data)

#############################################
# EXERCISE 3
#############################################

def to_datatime_from_dtf(date):
    print(str(date))
    print(date)
    return datetime.datetime.strptime(str(date), '%Y-%m-%d %H:%M:%S')

def get_occur(station_id):
    count = Rentals.select().where(Rentals.rental_station_id == station_id).count()
    print(count)

def get_average_duration_at(station_id):
    avg_duration_started = Rentals.select(fn.avg(Rentals.duration).alias('avg_duration')) \
        .where(Rentals.rental_station_id == station_id) \
        .scalar()
    
    return int(avg_duration_started) if avg_duration_started else 0

def get_average_duration_to(station_id):
    avg_duration_end = Rentals.select(fn.avg(Rentals.duration).alias('avg_duration')) \
        .where(Rentals.return_station_id == station_id) \
        .scalar()
    
    return int(avg_duration_end) if avg_duration_end else 0
    
def get_number_of_bicycles(stations_id):
    unique_bikes_count = (Rentals
        .select(fn.COUNT(fn.DISTINCT(Rentals.bike_number)).alias('unique_bikes'))
        .where(Rentals.rental_station_id == stations_id)
        .scalar())

    return int(unique_bikes_count) if unique_bikes_count else 0

def get_total_bikes_rented(station_id):
    total_bikes = Rentals.select().where(Rentals.rental_station_id == station_id).count()
    return total_bikes

def get_total_bikes_returned(station_id):
    total_bikes = Rentals.select().where(Rentals.return_station_id == station_id).count()
    return total_bikes

def get_rental_difference(station_id):
    return get_total_bikes_rented(station_id) - get_total_bikes_returned(station_id)