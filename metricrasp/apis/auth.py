from flask import Blueprint, request
from flask_restful import Api, Resource
from flask_jwt_extended import create_access_token

from metricrasp.config import HostConfig


api = Api(Blueprint(__name__, __name__))

@api.resource("/auth")
class Auth(Resource):
    def post(self):
        password = request.json("password")
        if not password == HostConfig.PASSWORD: abort(409)
        return create_access_token(identity="admin")