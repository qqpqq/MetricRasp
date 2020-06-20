from flask import Blueprint, request
from flask_restful import Api, Resource

from metricrasp.apis import admin
from metricrasp.apis.services.metric_service import get_metric


api = Api(Blueprint(__name__, __name__))

@api.resource("/information")
class ServerInfo(Resource):
    @admin
    def get(self):
        return get_metric()