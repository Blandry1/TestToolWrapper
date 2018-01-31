# from app import app

#from apis import blueprint as api
#from nodes import blueprint as api
#app.register_blueprint(run)

from flask import Flask, render_template, url_for, send_from_directory, request, make_response
from flask_restplus import Resource, Api, reqparse, fields, Namespace
from flask_cors import CORS, cross_origin
import requests 
app = Flask(__name__)
api = Api(app)
CORS(app)


#======== views ===========


@api.route('/sayHello')
def hello_world():
    return "Hello World!"

@api.route('/tryGET', methods=['GET'])
class testAccess(Resource):
    def get(self):
        try:
            url = 'https://www.google.com/'
            r = requests.get(url)
            data = r.text
            return data

        except Exception as exc:
            message = 'Something went wrong ' + str(exc)
            return message, 500
  
@api.route('/tryPOST', methods=['POST'])
def my_awesome_endpoint():
    data = request.json
    return data

   
if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True, port=5005)



# @api.route('/<string:location_uuid>/salerecommendation')
# class GetSaleRecommendation(Resource):
#     @api.doc(responses={
#         200: 'Success',
#         400: 'Validation Error'
#     })
#     def get(self, location_uuid):
#         '''Return a list of items recommended for putting on sale'''
#         try:
#             try:
#                 url = neo_http_ap + '/db/data/cypher'
#                 data = {'query': get_sales_recommendations, 'params': {'uuid': str(location_uuid)}}
#                 data = json.dumps(data, separators=(',', ':'))
#                 response = session.post(url, data=data, verify=False)
#                 responses = response.json()['data']
#             except:
#                 message = 'Location could not be found\n'
#                 logger.debug(message)
#                 return message, 400


#         except Exception as exc:
#             message = 'Something went wrong'
#             logger.critical(message)
#             logger.dump_exception(exc)
#             return message, 500


# @app.route('/timetrigger', methods = ['PUT'])
# def time_triggered():
#     try:
#         data = request.get_json()
#         date = datetime.datetime.strptime(data['datetime'],"%Y-%m-%d %H:%M:%S.%f")
#         #TODO: Actually make this function handle dates
#         return 'Successfully updated database',200
#     except Exception as exc:
#         message = 'Something went wrong ' + str(exc)
#         return message, 500


# @app.route('/yo', methods = ['GET'])
# def get_toTestTools(dir):
#     if request.method == 'POST':
#         try:
#             f = request.files['file']
#             name = secure_filename(f.filename)
#             #Make sure this line is changed to the right referencing method for windows or linux
#             f.save(os.path.join(os.path.join(os.path.dirname(os.path.realpath(__file__)),'nodes/static/'+ dir +'/',name)))
#             return str(name), 200
#         except:
#             return 'Something went wrong', 500
#     return '''
#         <!doctype html>
#         <title>Upload new File</title>
#         <h1>Upload new File</h1>
#         <form method=post enctype=multipart/form-data>
#           <p><input type=file name=file>
#              <input type=submit value=Upload>
#         </form>
#         '''

