from collections import OrderedDict

from flask import Flask
from flask_restplus import fields, Api, Resource

app = Flask(__name__)
api = Api(app)

import urlparse
url_params = "session_id=1234&input=Hello+World"
params_dict = urlparse.parse_qsl(url_params)
params = dict(params_dict)
print params
#  will print {"session_id":"1234","input":"Hello World"}


if __name__ == '__main__':
    app.run(debug=True)




