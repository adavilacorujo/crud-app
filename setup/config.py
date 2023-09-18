"""
DB CREDS
"""
import os
port = os.getenv('DBPORT', '5432')
dbname = os.getenv('DBNAME', 'notes')
host = os.getenv('DBHOST', 'localhost')
username = os.getenv('DBUSER', 'andres')
password = os.getenv('DBPASSWORD', 'password')

test_port = os.getenv('test_DBPORT', '5433')
test_dbname = os.getenv('test_DBNAME', 'test_notes')
test_host = os.getenv('test_DBHOST', 'localhost')
test_username = os.getenv('test_DBNAME', 'test')
test_password = os.getenv('test_DBPASSWORD', 'password')

SQLALCHEMY_DATABASE_URI = f'postgresql+psycopg2://{username}:{password}'\
            f'@{host}:{port}/{dbname}'