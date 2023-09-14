import uuid

from model import Notes, db
from datetime import datetime
from alchemy.utils.class_to_dict import class_to_dict


def update(request, id):
    data = request.json
    data['id'] = int(id)
    data['created_date'] = datetime.now().strftime('%Y-%m-%d')

    note = db.get_or_404(Notes, int(data['id']))
    note.owner = data['owner']
    note.content = data['content']
    note.created_date = data['created_date']
    note.important = data['important']

    db.session.add(note)
    db.session.commit()

    return data

def create(request):
    data = request.json
    data['id'] = int(str(uuid.uuid4())[-4:], 16)
    data['created_date'] = datetime.now().strftime('%Y-%m-%d')

    data['important'] = data['important']

    note = Notes(
        id = data['id'],
        owner = data['owner'],
        content = data['content'],
        created_date = data['created_date'],
        important = data['important']
    )

    db.session.add(note)
    db.session.commit()

    return data

def view():
    notes = db.session.execute(db.Select(Notes)).scalars()

    # Transform each class instance into a dictionary
    columns = [field for field in Notes.__dict__ if not field.startswith('_')]
    notes = class_to_dict(notes, columns)

    return notes
    
def delete(id):
    note = db.get_or_404(Notes, id)

    db.session.delete(note)
    db.session.commit()
