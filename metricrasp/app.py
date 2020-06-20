import metricrasp.extensions

from flask import Flask

def register_api(app):
    return None

def register_extension(app):
    extensions.cors.init_app(app)
    extensions.jwt.init_app(app)
    return None

def set_config(app, host_config):
    app.config.from_object(host_config)
    return None

def create_app(host_config):
    app = Flask("metricrasp", __name__)
    set_config(app, host_config)
    register_extension(app)
    register_api(app)

    return app