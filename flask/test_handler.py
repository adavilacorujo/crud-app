import unittest
import request_handler.handler as handler

from alchemy.driver import SQLAlchemy

class TestRequestHandler(unittest.TestCase):
    """
    This class tests the module handler's capability of returning the requested
    class.
    """

    def test_update_not_found_library(self):
        with self.assertRaises(ModuleNotFoundError):
            handler.SQLHandler(db=None, Notes=None).update(
                library='sql', request=None, id=None)
        
    


if __name__ == '__main__':
    import sys
    sys.path.insert(0, '/Users/adavila/Documents/work/occam/dev/crud-app/flask/')
    unittest.main()
