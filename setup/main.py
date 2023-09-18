from model import *
from config import *

from sqlalchemy import create_engine

try:
    engine = create_engine(SQLALCHEMY_DATABASE_URI)
    Base.metadata.create_all(engine)

except Exception as e:
    print('Error creating table', str(e))

finally:
    print('Finished create table attempt')

