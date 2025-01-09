from flask import Blueprint, request, jsonify
from api.models.device import Device
from api.services.device_service import DeviceService

device_controller = Blueprint('device_controller', __name__)

@device_controller.route('/devices', methods=['GET'])
def get_devices():
    device_service = DeviceService()
    devices = device_service.get_all_devices()
    return jsonify([device.to_dict() for device in devices])

@device_controller.route('/devices/<int:device_id>', methods=['GET'])
def get_device(device_id):
    device_service = DeviceService()
    device = device_service.get_device_by_id(device_id)
    if device:
        return jsonify(device.to_dict())
    return jsonify({'message': 'Device not found'}), 404

@device_controller.route('/devices', methods=['POST'])
def add_device():
    device_service = DeviceService()
    device_data = request.get_json()
    device = device_service.add_device(device_data)
    return jsonify(device.to_dict()), 201

@device_controller.route('/devices/<int:device_id>', methods=['PUT'])
def update_device(device_id):
    device_service = DeviceService()
    device_data = request.get_json()
    device = device_service.update_device(device_id, device_data)
    if device:
        return jsonify(device.to_dict())
    return jsonify({'message': 'Device not found'}), 404

@device_controller.route('/devices/<int:device_id>', methods=['DELETE'])
def delete_device(device_id):
    device_service = DeviceService()
    device_service.delete_device(device_id)
    return jsonify({'message': 'Device deleted successfully'}), 204