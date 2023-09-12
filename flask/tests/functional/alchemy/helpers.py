__author__  = 'Andres Davila'
__date__    = '09/12/2023'
__version__ = 0.1

import os
import sys
import json
import string
import random

sys.path.insert(0, os.path.abspath('../../flaskr'))
sys.path.insert(0, os.path.abspath('../..'))

def creating_note(important_flag : bool, client : object) -> tuple:
    test_data = {
            "owner": "test",
            "content": "test_note",
            "important": important_flag
        }
    response = client.post('/sqlalchemy/addData', json=test_data)
    response_data = json.loads(response.data.decode('utf-8'))
    return test_data, response_data

def reading_note(client : object) -> tuple:
    response = client.get('/sqlalchemy/getData')

    get_data_response = json.loads(response.data.decode('utf-8'))

    return get_data_response, response

def updating_note(client : object) -> tuple:
    # Get data from server
    response = client.get('/sqlalchemy/getData')
    get_data_response = json.loads(response.data.decode('utf-8'))
    
    update_obj = get_data_response[0]

    # generate random string of 5 chars
    update_obj['owner'] = ''.join(random.choices(
        string.ascii_letters, k=5))
    
    # generate random string of 10 chars
    update_obj['content'] = ''.join(random.choices(
        string.ascii_letters, k=10))

    # generate random bool flag for 
    update_obj['important'] = (random.randint(1, 100) % 2) == 0

    data_to_send = {
        "owner" : update_obj["owner"],
        "content": update_obj["content"],
        "important": update_obj["important"]
    }

    response = client.put(f"/sqlalchemy/updateData/"
                                f"{update_obj['id']}",
                                json=data_to_send)
    
    update_data_response = json.loads(response.data.decode('utf-8'))
    
    return data_to_send, update_data_response

def updating_note_with_enmpty_id(client : object) -> (object | None):
    # Get data from server
    response = client.get('/sqlalchemy/getData')
    get_data_response = json.loads(response.data.decode('utf-8'))
    
    if len(get_data_response) > 0:
        update_obj = get_data_response[0]

        # Modify id 
        update_obj['id'] = ''

        # generate random string of 5 chars
        update_obj['owner'] = ''.join(random.choices(
            string.ascii_letters, k=5))
        
        # generate random string of 10 chars
        update_obj['content'] = ''.join(random.choices(
            string.ascii_letters, k=10))

        # generate random bool flag for 
        update_obj['important'] = (random.randint(1, 100) % 2) == 0

        data_to_send = {
            "owner" : update_obj["owner"],
            "content": update_obj["content"],
            "important": update_obj["important"]
        }

        response = client.put(f"/sqlalchemy/updateData/"
                                    f"{update_obj['id']}",
                                    json=data_to_send)
        
        return response
    
    else:
        return None

def deleting_note(client : object) -> tuple:
    response = client.get('/sqlalchemy/getData')
    get_data_response = json.loads(response.data.decode('utf-8'))
            
    if len(get_data_response) > 0:
        delete_obj = get_data_response[0]   
        get_data_response.remove(delete_obj) # delete the first object

        response = client.get(f"/sqlalchemy/deleteData/"\
                                    f"{delete_obj['id']}")
        
        del_data_response = json.loads(response.data.decode('utf-8'))

    else:
        del_data_response = []


    return get_data_response, del_data_response


def deleting_note_with_empty_id(client : object) -> object:
    response = client.get(f"/sqlalchemy/deleteData/")

    return response