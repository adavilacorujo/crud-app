import uuid

import psycopg2
from flaskr.config import *
from datetime import datetime
from psycopg2.extras import RealDictCursor



def update(request, id):
    cursor = None

    try:
        data = request.json
        data['id'] = int(id)
        # DB schema should contain an updated column, not just created
        data['created_date'] = datetime.now().strftime('%Y-%m-%d')
        data['important'] = data['important']

        update_query = """ UPDATE notes set owner = %s, content = %s, created_date = %s, important = %s
                                        WHERE id = %s
                                    """

        record_to_update = (data['owner'], data['content'], data['created_date'], data['important'], data['id'])
        
        conn = psycopg2.connect(user=username,
                                    password=password,
                                    host=host,
                                    port=port,
                                    database=dbname)
        
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        
        cursor.execute(update_query, record_to_update)
        conn.commit()


    except (Exception) as error:
        return str(error)
    
    finally:
        if (cursor):
            cursor.close()
    
    return data


def view(table):
    records = None
    cursor = None

    try:
        conn = psycopg2.connect(user=username,
                                    password=password,
                                    host=host,
                                    port=port,
                                    database=dbname)
        
        cursor = conn.cursor(cursor_factory=RealDictCursor)

        cursor.execute(f"SELECT * from {table}")
        records = cursor.fetchall()

    except (Exception) as error:
        return str(error)
    
    finally:
        if (cursor):
            cursor.close()
    
    return records


def create(request):
    data = None
    cursor = None

    try:
        data = request.json
        data['id'] = int(str(uuid.uuid4())[-4:], 16)
        data['created_date'] = datetime.now().strftime('%Y-%m-%d')
        data['important'] = data['important']
        insert_query = """ INSERT INTO notes (id, owner, content, created_date, important) 
                        VALUES (%s, %s, %s, %s, %s)
                    """
                
        record_to_insert = (data['id'], data['owner'], data['content'], data['created_date'], data['important'])
        conn = psycopg2.connect(user=username,
                                    password=password,
                                    host=host,
                                    port=port,
                                    database=dbname)
    
        cursor = conn.cursor(cursor_factory=RealDictCursor)

        cursor.execute(insert_query, record_to_insert)
        conn.commit()

    except (Exception) as error:
        return str(error)
    
    finally:
        if (cursor):
            cursor.close()
    
    return data

def delete(id, table):
    cursor = None

    try:
        delete_query = """ DELETE from notes where id = %s"""
        conn = psycopg2.connect(user=username,
                                        password=password,
                                        host=host,
                                        port=port,
                                        database=dbname)
        
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        
        cursor.execute(delete_query, [id])
        conn.commit()

    except (Exception) as error:
        return str(error)
    
    finally:
        if (cursor):
            cursor.close()

    return view(table=table)