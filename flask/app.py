__author__  = 'Andres Davila'
__date__    = '09/07/2023'
__version__ = 1.0


from config import db_dsn
from driver.Driver import *
from flask_cors import CORS
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

import json

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = db_dsn
db = SQLAlchemy(app)

class Notes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    owner = db.Column(db.String(50), nullable=False)
    content = db.Column(db.String(150), nullable=False)
    created_date = db.Column(db.Date, nullable=False)
    important = db.Column(db.Boolean, nullable=False)

@app.route('/')
def index():
    return "Hello"

@app.route('/<string:library>/addData', methods=['POST'])
def add_data(library:int):
    return SQLDriver(db=db, Notes=Notes).create(library=library, request=request)

@app.route('/<string:library>/getData', methods=['GET'])
def get_data(library:int):
    return SQLDriver(db=db, Notes=Notes).view(library=library)

@app.route('/<string:library>/updateData/<string:id>', methods=['PUT'])
def update_data(library:str, id:int):
    return SQLDriver(db=db, Notes=Notes).update(library=library, request=request, id=id)

@app.route('/<string:library>/deleteData/<string:id>', methods=['GET'])
def delete_data(library:str, id:int):
    return SQLDriver(db=db, Notes=Notes).delete(library=library, id=id)

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8000, debug=True)