__author__  = 'Andres Davila'
__date__    = '09/10/2023'
__version__ = 1.0

from flaskr.alchemy.operations import *

class SQLAlchemy():
    def __init__(self):
        pass

    def update(self, request, id):
        return update(request, id)

    def view(self):
        return view()
    
    def create(self, request):
        return create(request)

    def delete(self, id):
        delete(id)
        return view()