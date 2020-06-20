from flask import Blueprint, request
from flask_restful import Api, Resource


api = Api(Blueprint(__name__, __name__))

@api.resource("/auth")
class Auth(Resource):
    def post(self):
        password = request.json("password")