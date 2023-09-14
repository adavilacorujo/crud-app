import os

from model import db
from flask import request, Flask
from request_handler.handler import SQLHandler

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_object('config.DevelopmentConfig')
        
    else:
        # load the test config if passed in
        app.config.from_object('config.TestingConfig')

    db.init_app(app)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    return app

app = create_app()

@app.route('/')
def index():
    return "Hello"

@app.route('/<string:library>/addData', methods=['POST'])
def add_data(library:int):
    return SQLHandler().create(library=library, request=request, id=id)

@app.route('/<string:library>/getData', methods=['GET'])
def get_data(library:int):
    return SQLHandler().view(library=library, request=request, id=id)

@app.route('/<string:library>/updateData/<string:id>', methods=['PUT'])
def update_data(library:str, id:int):
    return SQLHandler().update(library=library, request=request, id=id)

@app.route('/<string:library>/deleteData/<string:id>', methods=['GET'])
def delete_data(library:str, id:int):
    return SQLHandler().delete(library=library, request=request, id=id)
