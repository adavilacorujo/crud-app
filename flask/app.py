__author__  = 'Andres Davila'
__date__    = '09/07/2023'
__version__ = 1.0

import model 

from config import db_dsn
from request_handler.handler import *
from flask_cors import CORS
from flask import Flask, request

import json

def create_app(config_filename):
    app = Flask(__name__)
    
    # Initialize Cross Origin Resource sharing for the application
    CORS(app)

    app.config['SQLALCHEMY_DATABASE_URI'] = db_dsn

    app.config.from_pyfile(config_filename)

    model.db.init_app(app)

    return app

app = create_app()


@app.route('/')
def index():
    return "Hello"

@app.route('/<string:library>/addData', methods=['POST'])
def add_data(library:int):
    return SQLHandler(db=db, Notes=Notes).create(library=library, request=request, id=id)

@app.route('/<string:library>/getData', methods=['GET'])
def get_data(library:int):
    return SQLHandler(db=db, Notes=Notes).view(library=library, request=request, id=id)

@app.route('/<string:library>/updateData/<string:id>', methods=['PUT'])
def update_data(library:str, id:int):
    return SQLHandler(db=db, Notes=Notes).update(library=library, request=request, id=id)

@app.route('/<string:library>/deleteData/<string:id>', methods=['GET'])
def delete_data(library:str, id:int):
    return SQLHandler(db=db, Notes=Notes).delete(library=library, request=request, id=id)

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8000, debug=True)