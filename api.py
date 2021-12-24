from flask import Flask, request
from flask_restful import Api, Resource

app = Flask(__name__)

api = Api(app)


class BatResource(Resource):
    def get(self):
        return {
            'sts': 'success',
            'msg': 'checking docker deployment',
            'res': '1 + 1 = 2'
        }

    def post(self):

        obj = request.get_json()

        return {
            'sts': 'success',
            'msg': 'data posted successfully',
            'res': obj
        }


api.add_resource(
    BatResource,  # shape of user resource
    '/bat'
)

if __name__ == '__main__':
    app.run(debug=True)
