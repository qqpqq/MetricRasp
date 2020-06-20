import extensions

from flask import Flask

def register_api(app: Flask) -> None:
    return None

def register_extension(app: Flask) -> None:
    extension.cors.init_app(app)
    return None

def create_app() -> Flask:
    app = Flask("metricrasp", __name__)
    register_extension(app)
    register_api(app)

    return app