from metricrasp.util import json_parser


class MetricConfig:
    parsed_config: dict = json_parser("metricrasp.conf")

    linux_version: str = parsed_config["linux_version"]
    cpu_temperature_path: str = parsed_config["cpu_temperature_path"]
    gpu_temperature_path: str = parsed_config["gpu_temperature_path"]
    memory_status_path: str = parsed_config["memory_status_path"]
    cpu_status_path: str = parsed_config["cpu_status_path"]


class HostConfig:
    HOST = "0.0.0.0"
    PORT = 3000
    ENV = "production"
    PASSWORD = os.getenv("PASSWORD")
