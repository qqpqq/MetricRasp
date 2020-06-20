from metricrasp.app import create_app
from metricrasp.config import HostConfig
from metricrasp.const import RUN_SETTINGS


if __name__ == "__main__":
    app = create_app(HostConfig)

    from waitress import serve
    serve(app, **RUN_SETTINGS)