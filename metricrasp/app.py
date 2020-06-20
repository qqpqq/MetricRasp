from flask import Flask

from metricrasp import extensions
from metricrasp.apis import auth
from metricrasp.apis import metric


def register_api(app):
    app.register_blueprint(auth.api.blueprint)
    app.register_blueprint(metric.api.blueprint)
    return None

def register_extension(app):
    extensions.cors.init_app(app)
    extensions.jwt.init_app(app)
    return None

def set_config(app, host_config):
    app.config.from_object(host_config)
    return None

def create_app(host_config):
    app = Flask(__name__)
    set_config(app, host_config)
    register_extension(app)
    register_api(app)

    return app