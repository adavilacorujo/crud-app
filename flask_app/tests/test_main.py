__author__  = 'Andres Davila'
__date__    = '09/12/2023'
__version__ = 0.1

import os
import sys
import unittest

sys.path.insert(0, os.path.abspath('..'))
sys.path.insert(0, os.path.abspath('../flaskr'))

# sys.path.insert(0, os.path.abspath('./functional'))

from functional.psycopg.test_psycopg2_notes import *
from functional.alchemy.test_sqlalchemy_notes import *


if __name__ == '__main__':
    unittest.main()