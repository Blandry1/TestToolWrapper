
import requests
import json
import uuid
from flask import Flask, request, json, jsonify
from flask_restplus import Resource, Api, Resource, reqparse


app = Flask(__name__)
api = Api(app, title='TMS Classification for - Function Test') # TODO: change for each UT, ST, VA

rbt = api.namespace('RBT Test', description='Risk-based Testing, Sanity and Regression | accessible by API, no CLI')
#TODO: change to arq, JUNIT

#TODO: change to arq.route('/arq/<string:TC>/<string:responder>/<string:tag>/') 
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

        with open('Test_Logs.txt', 'a+') as outfile:
            json.dump(jsonData, outfile, sort_keys = False, indent = 4, ensure_ascii = False)
        
        return jsonData


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5001) # TODO: change port for each microservice


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
    

