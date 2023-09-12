__author__  = 'Andres Davila'
__date__    = '09/12/2023'
__version__ = 0.1

import os
import sys
import unittest

sys.path.insert(0, os.path.abspath('../../../flaskr'))
sys.path.insert(0, os.path.abspath('../../..'))

from flaskr import create_app
from functional.alchemy.helpers import *

class TestRouteSQlAlchemy(unittest.TestCase):

    def setUp(self) -> None:
        self.flask_app = create_app(test_config=True)

    # @unittest.skip('Tested')
    def test_creating_note_sqlalchemy(self):
        with self.flask_app.test_client() as test_client:
            for important_flag in [True, False]:
                with self.subTest(important_flag):
                    test_data, response_data = creating_note(important_flag, test_client)

                    self.assertDictContainsSubset(test_data, response_data, 
                                                  'Return value not as expected')
    # @unittest.skip('')            
    def test_reading_note_sqlalchemy(self):
        with self.flask_app.test_client() as test_client:
            get_data_response, response = reading_note(test_client)

            self.assertEqual(response.status_code, 200, 'Server responded'\
                             ' different code than expected')
            self.assertIsInstance(get_data_response, list, 'Data returned'\
                                  ' is not in expected list format') 
    
    # @unittest.skip('')
    def test_updating_note_sqlalchemy(self):
        with self.flask_app.test_client() as test_client:

            data_to_send, update_data_response = updating_note(test_client)

            self.assertDictContainsSubset(data_to_send, 
                                            update_data_response, 'Returned'\
                                            ' is not as expected')
                
                
    def test_update_with_wrong_id_sqlalchemy(self):
        with self.flask_app.test_client() as test_client:

            response = updating_note_with_enmpty_id(test_client)

            if response:
                self.assertEqual(response.status_code, 404, 'Status code'\
                                ' did not return 404 as expected')
            
                self.assertIn('Not Found', response.data.decode('utf-8'), 
                          'Header info did not contain expected not found')
       

    # @unittest.skip('Adding data to test')
    def test_deleting_note_sqlalchemy(self):
        with self.flask_app.test_client() as test_client:

            get_data_response, del_data_response = deleting_note(test_client)

            self.assertEqual(get_data_response, del_data_response, 
                                 'Returned object is not as expected')
                
    def test_deleting_with_wrong_id_sqlalchemy(self):
        with self.flask_app.test_client() as test_client:
            response = deleting_note_with_empty_id(test_client)
            
            self.assertEqual(response.status_code, 404, 'Status code'\
                                ' did not return 404 as expected')
            
            self.assertIn('Not Found', response.data.decode('utf-8'), 
                            'Header info did not contain expected not found')
            

if __name__ == '__main__':
    unittest.main()