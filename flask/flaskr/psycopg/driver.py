__author__  = 'Andres Davila'
__date__    = '09/10/2023'
__version__ = 1.0

import uuid

from flaskr.psycopg.operations import *

class Psycopg():
    def __init__(self, table="notes"):
        self.table = table

    def update(self, request, id):
        return update(request=request, id=id)

    def view(self):
        return view(table=self.table)
        
    def create(self, request):
        return create(request=request)

    def delete(self, id:int):
        return delete(id=id, table=self.table)