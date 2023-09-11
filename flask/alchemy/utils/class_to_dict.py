from typing import List

def class_to_dict(notes : List[object], columns: List) -> List[dict]:
    """
    Transform a list of class objects to a list of dictionaries to send over
        the network

    Input:
        - notes (List[Notes]), list of Notes objects containing data from the 
            db
    Return:
        (list[dict])
    """
    temp_notes = []
    for note in notes:
        temp = note.__dict__
        temp = {key: temp[key] for key in columns}
        temp_notes.append(
            temp
        )

    return temp_notes