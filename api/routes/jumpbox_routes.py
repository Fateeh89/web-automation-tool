# api/routes/jumpbox_routes.py

from flask import Blueprint
from api.controllers.jumpbox_controller import jumpbox_controller

jumpbox_routes = Blueprint('jumpbox_routes', __name__)

jumpbox_routes.register_blueprint(jumpbox_controller, url_prefix='/api/jumpboxes')