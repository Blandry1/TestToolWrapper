import requests
import json
from flask import Flask, request, json, jsonify, Blueprint
from flask_restplus import Resource, Api, reqparse, fields, SchemaModel
import urllib2
#import untangle
import re

app = Flask(__name__)
api = Api(app, title='Function Test', doc='/FT')

rbt = api.namespace('RBT', description='Accessible by API')
junit = api.namespace('JUnit', description='Accessible by API and CLI')
rocket = api.namespace('Rocket', description='Accessible by API')

# model = rbt.model('Model', {
#     'task': fields.String,
#     'uri': fields.Url('todo_ep')
# })

# address = rbt.schema_model('Address', {
#     'properties': {
#         'road': {
#             'type': 'string'
#         },
#     },
#     'type': 'object'
# })

host='142.133.174.149'
port=':8888'

@rbt.route('/<string:url>/<string:tag>')
@rbt.param('url', 'Relative Path for Test, i.e. AfgVafgMasterSmokeTestSuites.TestSuiteVafgAll.TestSuiteVafgEnafGba?suite&format=xml')
@rbt.param('tag', 'Group Parameter, i.e. AFG, TNO')

class RBT(Resource):

    @rbt.doc(responses={
        200: 'Success',
        400: 'Validation Error',
        500: 'Internal Server Error'
    })

    #@rbt.marshal_with(address)
    def get(self, url , tag):
        '''TC#1 Definition'''
        url2 = 'http://' + host +  port + '/' + url
        urllib2.unquote(url2).decode('utf8')

       # url = 'http://httpbin.org/get'
        url3 = 'http://142.133.174.149:8888/AfgApTestCases.TestCase0800SuccessAfgApAutGbaDigest?test&format=xml'
        tag = tag   # TODO: tag goes to a grouping file. Grouping would be done backend and hardcoded.
        r = requests.get(url3)
        data = r.text

        f = open('Test_logs.xml', 'w') # in string-format
        f.write(data)
        f.close()

        return data

@junit.route('/<string:url>/<string:tag>')
@junit.param('url', 'Relative Path for Test, i.e. AfgVafgMasterSmokeTestSuites.TestSuiteVafgAll.TestSuiteVafgEnafGba?suite&format=xml')
@junit.param('tag', 'Group Parameter, i.e. AFG, TNO')  
class JUnit (Resource):

    @api.doc(responses={
        200: 'Success',
        400: 'Validation Error',
        500: 'Internal Server Error'
    })

    def get(self, url , tag):
        '''TC#1 Definition'''
        url2 = 'http://' + host +  port + '/' + url
        urllib2.unquote(url2).decode('utf8')

       # url = 'http://httpbin.org/get'
        url3 = 'http://142.133.174.149:8888/AfgApTestCases.TestCase0800SuccessAfgApAutGbaDigest?test&format=xml'
        tag = tag   # TODO: tag goes to a grouping file. Grouping would be done backend and hardcoded.
        r = requests.get(url3)
        data = r.text

        f = open('Test_logs.xml', 'w') # in string-format
        f.write(data)
        f.close()

        return data



@rocket.route('/<string:url>/<string:tag>')
@rocket.param('url', 'Relative Path for Test, i.e. AfgVafgMasterSmokeTestSuites.TestSuiteVafgAll.TestSuiteVafgEnafGba?suite&format=xml')
@rocket.param('tag', 'Group Parameter, i.e. AFG, TNO')    
class Rocket (Resource):

    @api.doc(responses={
        200: 'Success',
        400: 'Validation Error',
        500: 'Internal Server Error'
    })

    def get(self, url , tag):
        '''TC#1 Definition'''
        url2 = 'http://' + host +  port + '/' + url
        urllib2.unquote(url2).decode('utf8')

       # url = 'http://httpbin.org/get'
        url3 = 'http://142.133.174.149:8888/AfgApTestCases.TestCase0800SuccessAfgApAutGbaDigest?test&format=xml'
        tag = tag   # TODO: tag goes to a grouping file. Grouping would be done backend and hardcoded.
        r = requests.get(url3)
        data = r.text

        f = open('Test_logs.xml', 'w') # in string-format
        f.write(data)
        f.close()

        return data


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5002)