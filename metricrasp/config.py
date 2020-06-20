from metricrasp.util import json_parser


class MetricConfig:
    parsed_config = json_parser("../metricrasp.json")

    linux_version = parsed_config["linux_version"]
    cpu_temperature_path = parsed_config["cpu_temperature_path"]
    gpu_temperature_path = parsed_config["gpu_temperature_path"]
    memory_status_path = parsed_config["memory_status_path"]
    cpu_status_path = parsed_config["cpu_status_path"]


class HostConfig:
    ENV = "production"
    SECRET_KEY = os.getenv("SECRET_KEY")
    PASSWORD = os.getenv("PASSWORD")
