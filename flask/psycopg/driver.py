__author__  = 'Andres Davila'
__date__    = '09/10/2023'
__version__ = 1.0

import uuid

from config import *
from datetime import datetime

class Psycopg():
    def __init__(self, table="notes"):
        self.table = table

    def update(self, request, id):
        data = request.json
        data['id'] = int(id)
        # DB schema should contain an updated column, not just created
        data['created_date'] = datetime.now().strftime('%Y-%m-%d')
        data['important'] = 't' if data['important'] else 'f'
        
        try:
            cursor = conn.cursor(cursor_factory=RealDictCursor)

            update_query = """ UPDATE notes set owner = %s, content = %s, created_date = %s, important = %s
                                WHERE id = %s
                            """

            record_to_update = (data['owner'], data['content'], data['created_date'], data['important'], data['id'])
            
            cursor.execute(update_query, record_to_update)
            conn.commit()

        except (Exception, Error) as error:
            return str(error)
        
        finally:
            if (cursor):
                cursor.close()
        
        return data

    def view(self):
        try:
            cursor = conn.cursor(cursor_factory=RealDictCursor)
            cursor.execute(f"SELECT * from {self.table}")
            records = cursor.fetchall()
        except (Exception, Error) as error:
            return str(error)
        
        finally:
            if (cursor):
                cursor.close()
        
        return records
        
    def create(self, request):
        data = request.json
        data['id'] = int(str(uuid.uuid4())[-4:], 16)
        data['created_date'] = datetime.now().strftime('%Y-%m-%d')
        data['important'] = 't' if data['important'] else 'f'

        try:

            cursor = conn.cursor(cursor_factory=RealDictCursor)

            insert_query = """ INSERT INTO notes (id, owner, content, created_date, important) 
                    VALUES (%s, %s, %s, %s, %s)
                """
            
            record_to_insert = (data['id'], data['owner'], data['content'], data['created_date'], data['important'])
            
            cursor.execute(insert_query, record_to_insert)
            conn.commit()

        except (Exception, Error) as error:
            return str(error)
        
        finally:
            if (cursor):
                cursor.close()
        
        return data

    def delete(self, id:int):
        
        try:
            cursor = conn.cursor(cursor_factory=RealDictCursor)

            delete_query = """ DELETE from notes where id = %s"""

            cursor.execute(delete_query, [id])
            conn.commit()

        except (Exception, Error) as error:
            return str(error)
        
        finally:
            if (cursor):
                cursor.close()

        return self.view()