from flask import Flask,request
import json


app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    req=request.data
    reqJson=json.loads(req)
    if reqJson['username']=='swapna'and reqJson['password']=='abcd':
        return 'user sucessfully logged in'
    return 'password incorrect'

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8000,debug=True)