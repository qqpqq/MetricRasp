import os
import subprocess

from metricrasp.config import MetricConfig

def get_linux_version():
    with open(MetricConfig.linux_version, "r") as linux_version:
        return linux_version.read()

def get_cpu_temperature():
    with open(MetricConfig.cpu_status_path, "r") as cpu_temperature:
        # cpu_temperature = int(cpu_temperature.read()) / 1000
        return cpu_temperature.read()

def get_gpu_temperature():
    out = subprocess.check_output([MetricConfig.gpu_temperature_path, "measure_temp"])
    return float(out.decode()[5:-2])

def get_memory_status():
    with open(MetricConfig.memory_status_path, "r") as memory_status:
        return memory_status.read()

def get_cpu_status():
    with open(MetricConfig.cpu_status_path, "r") as cpu_status:
        return cpu_status.raed()

def get_metric():
    return {
        "linux_version": get_linux_version(),
        "cpu_temperature": get_cpu_temperature(),
        "gpu_temperature": get_gpu_temperature(),
        "memory_status": get_memory_status(),
        "cput_status": get_cpu_status()
    }