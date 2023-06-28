from singleton_database import Database_name
import sys

db = None
if len(sys.argv) >= 2:
    db = Database_name(sys.argv[1])
else:
    db = Database_name('Default_database_name')

import database_classes
database_classes.create_tables()
