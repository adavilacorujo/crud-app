__author__  = 'Andres Davila'
__date__    = '09/12/2023'
__version__ = 0.1

import os
import sys

sys.path.insert(0, os.path.abspath('../..'))

import unittest

from model import Notes
from datetime import datetime

class TestNotes(unittest.TestCase):
    """
    Test the creation of a new note using the DB model created using
    SQLAlchemy.
    """

    def test_new_note(self):
        """
        Scenario: User wants to create a new note
            Given a dictionary containing all info related to the note

            When the user sends a request through the React frontend
                to the Flask backend

            Then a new object should be created using the Notes class
                defined in the main app used to interact with the 
                    table in the DB
        """
        note = {
            'owner': 'john',
            'content': 'don\'t forget groceries',
            'created_date': datetime.now(),
            'important': True
        }

        note_obj = Notes(owner=note['owner'], content=note['content'], 
                     created_date=note['created_date'], 
                        important=note['important'])
        
        self.assertEqual(note_obj.owner, note['owner'], 'Object does not store \
                         owner correctly')
        self.assertEqual(note_obj.content, note['content'], 'Object \
                         does not store content correctly')
        self.assertEqual(note_obj.created_date, note['created_date'], 'Object does not store \
                         date correctly')
        self.assertEqual(note_obj.important, note['important'], 'Object does not store \
                         important flag correclty')
        


if __name__ == '__main__':
    unittest.main()