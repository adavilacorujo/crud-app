__author__  = 'Andres Davila'
__date__    = '09/10/2023'
__version__ = 1.0

import os
import psycopg2

from psycopg2 import Error
from sqlalchemy import create_engine
from psycopg2.extras import RealDictCursor

# Config file containing objects to be used in the app


db_name = os.getenv('DBNAME', 'notes')
db_user = os.getenv('DBUSER', 'andres')
db_password = os.getenv('DBPASSWORD', 'password')
db_host = os.getenv('DBHOST', 'localhost')
db_port = os.getenv('DBPORT', 5432)

conn = psycopg2.connect(dbname=db_name, user=db_user, host=db_host, port=db_port, password=db_password)

db_dsn = f"postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
# engine = create_engine(f"postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}")