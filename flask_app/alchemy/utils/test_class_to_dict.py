import unittest
from class_to_dict import class_to_dict

class TestObj():
    value_1 = '1'
    value_2 = '2'
    value_3 = '3'
    value_4 = '4'

class TestClassToDict(unittest.TestCase):
    def test_class_to_dict(self):
        obj = TestObj
        list_obj = [obj]
        return_value = [
            {
             'value_1': '1',
             'value_2': '2',
             'value_3': '3',
             'value_4': '4'
            }
        ]
        columns=[field for field in obj.__dict__ if not field.startswith('_')]

        self.assertEqual(class_to_dict(list_obj, columns), 
                        return_value, 'Return value differs')


if __name__ == '__main__':
     unittest.main()