from flask import Blueprint
from api.controllers.device_controller import device_controller

device_routes = Blueprint('device_routes', __name__)

device_routes.register_blueprint(device_controller, url_prefix='/api/devices')