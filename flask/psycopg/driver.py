__author__  = 'Andres Davila'
__date__    = '09/10/2023'
__version__ = 1.0

import uuid

from config import *
from datetime import datetime
from psycopg.operations import *

class Psycopg():
    def __init__(self, table="notes"):
        self.table = table

    def update(self, request, id):

        data = None

        try:
            cursor = conn.cursor(cursor_factory=RealDictCursor)
            data = update(request, cursor, id)


        except (Exception, Error) as error:
            return str(error)
        
        finally:
            if (cursor):
                cursor.close()
        
        return data

    def view(self):

        records = None

        try:
            cursor = conn.cursor(cursor_factory=RealDictCursor)
            records = view(cursor, table='notes')
        except (Exception, Error) as error:
            return str(error)
        
        finally:
            if (cursor):
                cursor.close()
        
        return records
        
    def create(self, request):

        data = None

        try:

            cursor = conn.cursor(cursor_factory=RealDictCursor)

            data = create(request, cursor)

        except (Exception, Error) as error:
            return str(error)
        
        finally:
            if (cursor):
                cursor.close()
        
        return data

    def delete(self, id:int):
        
        try:
            cursor = conn.cursor(cursor_factory=RealDictCursor)
            delete(cursor, id)

        except (Exception, Error) as error:
            return str(error)
        
        finally:
            if (cursor):
                cursor.close()

        return self.view()