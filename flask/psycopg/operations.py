import uuid

from config import conn
from datetime import datetime


def update(request, cursor, id):
    data = request.json
    data['id'] = int(id)
    # DB schema should contain an updated column, not just created
    data['created_date'] = datetime.now().strftime('%Y-%m-%d')
    data['important'] = 't' if data['important'] else 'f'

    update_query = """ UPDATE notes set owner = %s, content = %s, created_date = %s, important = %s
                                    WHERE id = %s
                                """

    record_to_update = (data['owner'], data['content'], data['created_date'], data['important'], data['id'])
                
    cursor.execute(update_query, record_to_update)
    conn.commit()

    return data

def view(cursor, table):
    cursor.execute(f"SELECT * from {table}")
    return cursor.fetchall()


def create(request, cursor):
    data = request.json
    data['id'] = int(str(uuid.uuid4())[-4:], 16)
    data['created_date'] = datetime.now().strftime('%Y-%m-%d')
    data['important'] = 't' if data['important'] else 'f'
    insert_query = """ INSERT INTO notes (id, owner, content, created_date, important) 
                    VALUES (%s, %s, %s, %s, %s)
                """
            
    record_to_insert = (data['id'], data['owner'], data['content'], data['created_date'], data['important'])
    
    cursor.execute(insert_query, record_to_insert)
    conn.commit()

    return data

def delete(cursor, id):
    delete_query = """ DELETE from notes where id = %s"""

    cursor.execute(delete_query, [id])
    conn.commit()
