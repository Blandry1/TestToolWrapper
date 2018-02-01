
import requests
import json
from flask import Flask, request, json, jsonify
from flask_restplus import Resource, Api


app = Flask(__name__)
api = Api(app, title='TMS Classification for - Function Test')

rbt = api.namespace('RBT Test', description='Risk-based Testing, Sanity and Regression | accessible by API, no CLI')
ns = api.namespace('practice', description='Practice operations')

@rbt.route('/rbt')
class ConnectToTestTool(Resource): 
    def get(self):
        url = 'https://api.github.com/events'
        r = requests.get(url)
        data = r.text

        #datajson = json.load(r)
        #datajson = r.json()['form']
        #datajson = request.get_json()
        #datajson = json.loads(request.data)

        #data = r.text
        #data = r.request.data
        return data

    def post(self, host, port, resource, responder, id, animals):
        # url = 'http://httpbin.org/post/'
        # url = '{host}/{port}/{resource}/{responder}/{id}/'.format(host, port, resource, responder, test-id)
        url = 'http://' + host + port + resource + responder + id
        
        #r = requests.post(url, data = {'animalFarm': animals, 'dessert': 'ocean'})
        r = requests.post(url, data={'interests': ['football', 'basketball']})
        data = r.text
        #data = r.request.body
        return data
    
    # def post(self, test_id):
    #     url = 'http://httpbin.org/post/test_id'
    #     r = requests.post(url, data = {'key':'value'})
    #     return data



    # def options(self):
    #     url = 'http://httpbin.org/get'
    #     r = requests.post(url, data = {'key':'value'})
    #     data = r.text
    #     return data

    # def head(self):
    #     url = 'http://httpbin.org/get'
    #     r = requests.post(url, data = {'key':'value'})
    #     data = r.text
    #     return data



#todos = {}           
# @ns.route('/<string:todo_id>')
# class TodoSimple(Resource):
#     def get(self, todo_id):
#         return {todo_id: todos[todo_id]}

#     def put(self, todo_id):
#         todos[todo_id] = request.form['data']
#         return {todo_id: todos[todo_id]}

# @ns.route('/hello')
# class HelloWorld(Resource):
#     def get(self):
#         return {'hello2': 'world'}


    
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5001)