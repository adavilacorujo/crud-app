"""
DB CREDS
"""
import os
port = os.getenv('DBPORT', '5432')
dbname = os.getenv('DBNAME', 'notes')
host = os.getenv('DBHOST', 'localhost')
username = os.getenv('DBNAME', 'andres')
password = os.getenv('DBPASSWORD', 'password')

test_port = os.getenv('test_DBPORT', '5433')
test_dbname = os.getenv('test_DBNAME', 'test_notes')
test_host = os.getenv('test_DBHOST', 'localhost')
test_username = os.getenv('test_DBNAME', 'test')
test_password = os.getenv('test_DBPASSWORD', 'password')

class Config(object):
    TESTING = False

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = ''

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = f'postgresql+psycopg2://{username}:{password}'\
            f'@{host}:{port}/{dbname}'

class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = f'postgresql+psycopg2://{test_username}:{test_password}'\
            f'@{test_host}:{test_port}/{test_dbname}'
    TESTING = True

    global port
    global dbname
    global host
    global username
    global password

    port = test_port
    dbname = test_dbname
    host = test_host
    username = test_username
    password = test_password