#
import requests
import json
from flask import Flask, request, json, jsonify
from flask_restplus import Resource, Api


app = Flask(__name__)
api = Api(app, title='Test Tools')

rbt = api.namespace('RBT Test', description='RBT operations')
ns = api.namespace('practice', description='Practice operations')

@rbt.route('/rbt')
class ConnectToTestTool(Resource): 
    def get(self):
        url = 'https://api.github.com/events'
        r = requests.get(url)
        data = r.text

        #datajson = json.load(r)
        #datajson = request.get_json()
        #datajson = json.loads(request.data)
        return data
    @rbt.ns.route('/rbt/extra2')
    class ConnectTOExtra(Resource):
        def post(self):
            url = 'http://httpbin.org/post'
            r = requests.post(url, data = {'key':'value'})
            data = r.text
            return data

@rbt.route('/rbt/extra')
class ConnectToTestTool(Resource): 
    def get(self):
        url = 'https://api.github.com/events'
        r = requests.get(url)
        data = r.text

        #datajson = json.load(r)
        #datajson = request.get_json()
        #datajson = json.loads(request.data)
        return data

    def post(self):
        url = 'http://httpbin.org/post'
        r = requests.post(url, data = {'key':'value'})
        data = r.text
        return data
    
    # def post(self, test_id):
    #     url = 'http://httpbin.org/post/test_id'
    #     r = requests.post(url, data = {'key':'value'})
    #     return data


    # def put(self):
    #     url = 'http://httpbin.org/put'
    #     r = requests.post(url, data = {'key':'value'})
    #     data = r.text
    #     return data

    # def delete(self):
    #     url = 'http://httpbin.org/delete'
    #     r = requests.post(url, data = {'key':'value'})
    #     data = r.text
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
    app.run(host='0.0.0.0', debug=True, port=5005)
