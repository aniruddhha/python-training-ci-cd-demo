from flask import Flask, request
from flask_restful import Api, Resource

app = Flask(__name__)

api = Api(app)


class DeafultResource(Resource):
    def get(self):
        return {
            'sts': 'success',
            'msg': 'deploying flask app on aws'
        }


class BatResource(Resource):
    def get(self):
        return {
            'sts': 'success',
            'msg': 'checking docker deployment',
            'res': '1 + 1 = 2'
        }

    def post(self):

        obj = request.get_json()
        print(obj)

        return {
            'sts': 'success',
            'msg': 'data posted successfully',
            'res': obj
        }


class CatResource(Resource):
    def get(self):
        return {
            'sts': 'success',
            'msg': 'mewooo'
        }


api.add_resource(
    DeafultResource,  # shape of user resource
    '/'
)
api.add_resource(
    BatResource,  # shape of user resource
    '/bat'
)
api.add_resource(
    CatResource,  # shape of user resource
    '/cat'
)

if __name__ == '__main__':
    app.run(
        debug=True,
        host='0.0.0.0',
        port=80
    )
