__author__  = 'Andres Davila'
__date__    = '09/10/2023'
__version__ = 1.0

from alchemy.driver import SQLAlchemy
from psycopg.driver import Psycopg

class SQLDriver():
    def __init__(self):
        pass

    def update(self, library, request, id):
        if library == 'psycopg2':
            return Psycopg().update(request, id)

        elif library == 'sqlalchemy':
            return SQLAlchemy().update(request, id)
        
    def delete(self, library, id):
        if library == 'psycopg2':
            return Psycopg().delete(id)

        elif library == 'sqlalchemy':
            return SQLAlchemy().delete(id)
        
    def create(self, library, request):
        if library == 'psycopg2':
            return Psycopg().create(request)

        elif library == 'sqlalchemy':
            return SQLAlchemy().create(request)
        
    def view(self, library):
        if library == 'psycopg2':
            return Psycopg().view()

        elif library == 'sqlalchemy':
           return SQLAlchemy().view()
        
    