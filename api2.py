import requests
import json
from flask import Flask, request, json, jsonify
from flask_restplus import Resource, Api


app = Flask(__name__)
api = Api(app, title='TMS Classification for - Unit Test')

rbt = api.namespace('RBT Test', description='Risk-based Testing, Sanity and Regression | accessible by CLI, no API')

@rbt.route('/rbt')
class ConnectToTestTool(Resource): 
    def get(self):
        url = 'https://api.github.com/events'
        r = requests.get(url)
        data = r.text
        return data

    def post(self):
        url = 'http://httpbin.org/post'
        r = requests.post(url, data = {'key':'value'})
        data = r.text
        return data
    

    
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5002)
