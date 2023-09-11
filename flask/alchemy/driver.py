__author__  = 'Andres Davila'
__date__    = '09/10/2023'
__version__ = 1.0

from alchemy.operations import *

class SQLAlchemy():
    def __init__(self):
        pass

    def update(self, db, Notes, request, id):
        return update(db, Notes, request, id)

    def view(self, db, Notes):
        return view(db, Notes)
    
    def create(self, db, Notes, request):
        return create(db, Notes, request)

    def delete(self, db, Notes, id):
        delete(db, Notes, id)
        return view(db, Notes)
