import requests
import json
import uuid
from flask import Flask, request, json, jsonify
from flask_restplus import Resource, Api, Resource, reqparse


app = Flask(__name__)
api = Api(app, title='TMS Classification for - Unit Test')

gtest = api.namespace('gTest', description='Accessible by API and CLI')
arq = api.namespace('Arquillian', description='Accessible by API and CLI')
junit = api.namespace('JUnit', description='Accessible by API and CLI')


@gtest.route('/<string:TC>/<string:responder>/<string:tag>/Test1')    
class gTest(Resource):

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



@arq.route('/<string:TC>/<string:responder>/<string:tag>/Test1')    
class Arquillian (Resource):

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



@junit.route('/<string:TC>/<string:responder>/<string:tag>/Test1')    
class JUnit (Resource):

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
    app.run(host='0.0.0.0', debug=True, port=5001)