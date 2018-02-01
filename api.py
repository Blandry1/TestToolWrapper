
import requests
import json
import uuid
from flask import Flask, request, json, jsonify
from flask_restplus import Resource, Api, Resource, reqparse


app = Flask(__name__)
api = Api(app, title='TMS Classification for - Function Test')

rbt = api.namespace('RBT Test', description='Risk-based Testing, Sanity and Regression | accessible by API, no CLI')
ns = api.namespace('practice', description='Practice operations') 

@rbt.route('/rbt')
class ConnectToTestTool(Resource): 

    #@api.expect()
    @api.doc(responses={
        200: 'Success',
        400: 'Validation Error',
        500: 'Internal Server Error'
    })
    
    def get(self):
        #url = 'http://' + host + port + resource + responder + id
        url = 'http://httpbin.org/get'
        r = requests.get(url)
        data = r.text
        jsonData = json.loads(data)
        #specific_jsonData = json.loads(data)['headers']
        
        #TODO: send jsonData variable to log file.
        f = open('test_logs.txt', 'a')
        f.write(jsonData) # change this line of code!!!
        f.close()

        return jsonData

@rbt.route('/rbt/<string:TC>/<string:responder>/<string:tag>/')    
class TestTool(Resource):

    @api.doc(responses={
        200: 'Success',
        400: 'Validation Error',
        500: 'Internal Server Error'
    })

    def get(self, TC, responder, tag):
        url = 'http://httpbin.org/get'
        tag = tag   # TODO: tag goes to a grouping file. Grouping would be done backend and hardcoded.
        parameters = {"TC": TC, 'responder': responder}
        r = requests.get(url, parameters)
        data = r.text
        jsonData = json.loads(data)
        
        return jsonData


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5001)


###-------------------------###

    # def post(self, host, port, resource, responder, id, animals):
    #     # url = 'http://httpbin.org/post/'
    #     # url = '{host}/{port}/{resource}/{responder}/{id}/'.format(host, port, resource, responder, test-id)
    #     url = 'http://' + host + port + resource + responder + id


#todos = {}           
# @ns.route('/<string:todo_id>')
# class TodoSimple(Resource):
#     def get(self, todo_id):
#         return {todo_id: todos[todo_id]}

#     def put(self, todo_id):
#         todos[todo_id] = request.form['data']
#         return {todo_id: todos[todo_id]}


#datajson = request.get_json()
#datajson = json.loads(request.data)
    

