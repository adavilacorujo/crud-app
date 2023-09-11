__author__  = 'Andres Davila'
__date__    = '09/07/2023'
__version__ = 1.0


from flask_cors import CORS
from driver.Driver import SQLDriver
from flask import Flask, request


app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return "Hello"

@app.route('/<string:library>/addData', methods=['POST'])
def addData(library:int):
    return SQLDriver().create(library=library, request=request)

@app.route('/<string:library>/getData', methods=['GET'])
def getData(library:int):
    return SQLDriver().view(library=library)

@app.route('/<string:library>/updateData/<string:id>', methods=['PUT'])
def updateData(library:str, id:int):
    return SQLDriver().update(library=library, request=request, id=id)

@app.route('/<string:library>/deleteData/<string:id>', methods=['GET'])
def deleteData(library:str, id:int):
    return SQLDriver().delete(library=library, id=id)

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8000, debug=True)