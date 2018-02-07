import requests
import json
import uuid
from flask import Flask, request, json, jsonify, Blueprint
from flask_restplus import Resource, Api, Resource, reqparse


app = Flask(__name__)

api = Api(app, title='Function Test')

#blueprint = Blueprint('api', __name__, url_prefix='/test')
#api = Api(blueprint)
#app.register_blueprint(blueprint)

rbt = api.namespace('RBT', description='Accessible by API')
junit = api.namespace('JUnit', description='Accessible by API and CLI')
rocket = api.namespace('Rocket', description='Accessible by API')

host='142.133.174.149'
port=':8888'
#resource = '/AfgVafgMasterSmokeTestSuites.TestSuiteVafgAll.TestSuiteVafgEnafGba'
#responder = '?suite'
#http://142.133.174.149:8888/AfgVafgMasterSmokeTestSuites.TestSuiteVafgAll.TestSuiteVafgEnafGba?suite

@rbt.route('/<string:resource>/<string:responder>/<string:tag>')  
@rbt.param('resource', 'url project tracing, i.e. test_ID')
@rbt.param('responder', 'editable file results')
@rbt.param('tag', 'grouping parameter')

class RBT(Resource):

    @rbt.doc(responses={
        200: 'Success',
        400: 'Validation Error',
        500: 'Internal Server Error'
    })

    def get(self, resource, responder, tag):
        '''TC#1 Definition'''
        url2 = 'http://' + host +  port + '/' + resource + '?' +responder
        print(url2)


        url = 'http://httpbin.org/get'
       # url = 'http://142.133.174.149:8888/AfgApTestCases.TestCase0800SuccessAfgApAutGbaDigest?test'
        tag = tag   # TODO: tag goes to a grouping file. Grouping would be done backend and hardcoded.
        parameters = {'resource': resource, 'responder':responder, 'tag': tag}
        r = requests.get(url2)
        data = r.text
      
        jsonData = json.loads(data)

        with open('Tests_Logs.txt', 'a') as outfile:
           json.dump(jsonData, outfile, sort_keys = False, indent = 4,
              ensure_ascii = False)

        return jsondata



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



@rocket.route('/<string:TC>/<string:responder>/<string:tag>/Test1')    
class Rocket (Resource):

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
    app.run(host='0.0.0.0', debug=True, port=5002)