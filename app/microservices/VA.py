
import requests
import json
import uuid
from flask import Flask, request, json, jsonify 
from flask_restplus import Resource, Api, Resource, reqparse

app = Flask(__name__)
api = Api(app, title='Vulnerability Assessment')

cisCat = api.namespace('CIS-CAT', description='accessible by CLI')
openVas = api.namespace('OpenVAS', description='accesible by API & CLI')
nessus = api.namespace('Nessus', description='accesible by API')
nexpose = api.namespace('Nexpose', description='accesible by API & CLI')
openScap = api.namespace('OpenSCAP', description='accessible by API & CLI')
metasploit = api.namespace('Metasploit', description='accesible by API')


@cisCat.route('/<string:TC>/<string:responder>/<string:tag>/Test1')    
class cisCatGET(Resource):

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

        with open('Test_Logs.txt', 'a+') as outfile:
            json.dump(jsonData, outfile, sort_keys = False, indent = 4, ensure_ascii = False)
        
        return jsonData
 
@openVas.route('/<string:TC>/<string:responder>/<string:tag>/Test1')    
class openVasGET(Resource):

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

        with open('Test_Logs.txt', 'a+') as outfile:
            json.dump(jsonData, outfile, sort_keys = False, indent = 4, ensure_ascii = False)
        
        return jsonData

@nessus.route('/<string:TC>/<string:responder>/<string:tag>/Test1')    
class nessusGET(Resource):

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

        with open('Test_Logs.txt', 'a+') as outfile:
            json.dump(jsonData, outfile, sort_keys = False, indent = 4, ensure_ascii = False)
        
        return jsonData

@nexpose.route('/<string:TC>/<string:responder>/<string:tag>/Test1')    
class nexposeGET(Resource):

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

        with open('Test_Logs.txt', 'a+') as outfile:
            json.dump(jsonData, outfile, sort_keys = False, indent = 4, ensure_ascii = False)
        
        return jsonData

@openScap.route('/<string:TC>/<string:responder>/<string:tag>/Test1')    
class openScapGET(Resource):

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

        with open('Test_Logs.txt', 'a+') as outfile:
            json.dump(jsonData, outfile, sort_keys = False, indent = 4, ensure_ascii = False)
        
        return jsonData

@metasploit.route('/<string:TC>/<string:responder>/<string:tag>/Test1')    
class metasploitGET(Resource):

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

        with open('Test_Logs.txt', 'a+') as outfile:
            json.dump(jsonData, outfile, sort_keys = False, indent = 4, ensure_ascii = False)
        
        return jsonData


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5005)