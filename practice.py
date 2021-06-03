from flask import Flask,request
import json import pymongo
from pymongo import MongoClient
client=MongoClient("mongodb://127.0.0.1:27017/?compressors=disabled&gssapiServiceName=mongodb")
db = MongoClient['user_login']

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    req=request.data
    reqJson=json.loads(req)
    resp=db.user_login.find_one(reqJson)
    if resp == None:
        return {'message':'Incorrect username and password'}    
    return {'message':'user logged in successfully'}

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8000,debug=True)