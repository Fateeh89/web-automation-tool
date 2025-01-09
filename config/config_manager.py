# config/config_manager.py
import os
import json
from jinja2 import Template
from netmiko import ConnectHandler

def load_config_template(device_type):
    template_path = os.path.join("config", "templates", f"{device_type}_config_template.j2")
    with open(template_path, "r") as file:
        return Template(file.read())

def check_running_configuration(device):
    net_connect = ConnectHandler(device_type=device['device_type'], ip=device['device_ip'], username=device['device_username'], password=device['device_password'])
    net_connect.enable()
    if device['device_type'] in ["cisco_common_ios", "cisco_ios_xe", "cisco_ios_xr"]:
        running_config = net_connect.send_command("show running-config")
    elif device['device_type'] == "juniper":
        running_config = net_connect.send_command("show configuration")
    elif device['device_type'] == "huawei":
        running_config = net_connect.send_command("display current-configuration")
    net_connect.disconnect()
    return running_config

def modify_configuration(device, defined_config, running_config):
    modified_config = []
    for line in defined_config.splitlines():
        if line not in running_config.splitlines():
            modified_config.append(line)
    return "\n".join(modified_config)

def push_configuration(device, defined_config, modified_config):
    net_connect = ConnectHandler(device_type=device['device_type'], ip=device['device_ip'], username=device['device_username'], password=device['device_password'])
    net_connect.enable()
    if device['device_type'] in ["cisco_common_ios", "cisco_ios_xe", "cisco_ios_xr"]:
        net_connect.config_mode()
    elif device['device_type'] == "huawei":
        net_connect.send_command("system-view")
    elif device['device_type'] == "juniper":
        net_connect.send_command("configure")
    if modified_config:
        net_connect.send_config_set(modified_config.splitlines())
    else:
        net_connect.send_config_set(defined_config.splitlines())
    if device['device_type'] in ["huawei", "juniper", "cisco_ios_xr"]:
        net_connect.commit()
    if device['device_type'] in ["cisco_common_ios", "cisco_ios_xe", "cisco_ios_xr"]:
        net_connect.exit_config_mode()
    net_connect.disconnect()

def push_configurations(devices, defined_config):
    for device in devices:
        running_config = check_running_configuration(device)
        modified_config = modify_configuration(device, defined_config, running_config)
        push_configuration(device, defined_config, modified_config)
        save_pushed_configuration(device, defined_config)

def save_pushed_configuration(device, defined_config):
    with open(f"{device['device_name']}.cfg", "w") as file:
        file.write(defined_config)

def push_configuration_periodically(devices, defined_config, interval):
    for device in devices:
        running_config = check_running_configuration(device)
        modified_config = modify_configuration(device, defined_config, running_config)
        push_configuration(device, defined_config, modified_config)
        time.sleep(interval)