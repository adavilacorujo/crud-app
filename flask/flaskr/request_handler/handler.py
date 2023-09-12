__author__  = 'Andres Davila'
__date__    = '09/10/2023'
__version__ = 1.0

from  flaskr.alchemy.driver import SQLAlchemy
from flaskr.psycopg.driver import Psycopg

class SQLHandler():

    def update(self, library, request, id):
        if library == 'psycopg2':
            return Psycopg().update(request, id)

        elif library == 'sqlalchemy':
            return SQLAlchemy().update(request, id)
        
        else:
            raise ModuleNotFoundError('Library param is not valid')
        
    def delete(self, library, request, id):
        if library == 'psycopg2':
            return Psycopg().delete(id)

        elif library == 'sqlalchemy':
            return SQLAlchemy().delete(id)
        
        else:
            raise ModuleNotFoundError('Library param is not valid')
        
    def create(self, library, request, id):
        if library == 'psycopg2':
            return Psycopg().create(request)

        elif library == 'sqlalchemy':
            return SQLAlchemy().create(request)
        
        else:
            raise ModuleNotFoundError('Library param is not valid')
        
    def view(self, library, request, id):
        if library == 'psycopg2':
            return Psycopg().view()

        elif library == 'sqlalchemy':
           return SQLAlchemy().view()
        
        else:
            raise ModuleNotFoundError('Library param is not valid')
        
    