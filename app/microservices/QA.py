import requests
import json
import uuid
from flask import Flask, request, json, jsonify
from flask_restplus import Resource, Api, Resource, reqparse


app = Flask(__name__)
api = Api(app, title='Quality Assurance')

pureload = api.namespace('Pureload', description='API executes commands, and results are retrieved by CLI')
appdynamics = api.namespace('AppDynamics', description='Accessible by API and CLI')


@pureload.route('/<string:TC>/<string:responder>/<string:tag>/Test1')    
class Pureload(Resource):

    @api.doc(responses={
        200: 'Success',
        400: 'Validation Error',
        500: 'Internal Server Error'
    })

    def get(self, TC, responder, tag):
        '''TC#1 Definition'''
        url = 'http://httpbin.org/get'
        tag = tag   # TODO: tag goes to a grouping file. Grouping would be done backend and hardcoded.
        parameters = {"TC": TC, 'responder': responder}
        r = requests.get(url, parameters)
        data = r.text
        jsonData = json.loads(data)

        with open('Tests_Logs.txt', 'a+') as outfile:
            json.dump(jsonData, outfile, sort_keys = False, indent = 4,
               ensure_ascii = False)

        return jsonData



@appdynamics.route('/<string:TC>/<string:responder>/<string:tag>/Test1')    
class AppDynamics (Resource):

    @api.doc(responses={
        200: 'Success',
        400: 'Validation Error',
        500: 'Internal Server Error'
    })

    def get(self, TC, responder, tag):
        '''TC#1 Definition'''
        url = 'http://httpbin.org/get'
        tag = tag   # TODO: tag goes to a grouping file. Grouping would be done backend and hardcoded.
        parameters = {"TC": TC, 'responder': responder}
        r = requests.get(url, parameters)
        data = r.text
        jsonData = json.loads(data)

        with open('Tests_Logs.txt', 'a+') as outfile:
            json.dump(jsonData, outfile, sort_keys = False, indent = 4,
               ensure_ascii = False)

        return jsonData




if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5006)