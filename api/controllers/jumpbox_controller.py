from flask import Blueprint, request, jsonify
from api.models.jumpbox import Jumpbox
from api.services.jumpbox_service import JumpboxService

jumpbox_controller = Blueprint('jumpbox_controller', __name__)

@jumpbox_controller.route('/jumpboxes', methods=['GET'])
def get_jumpboxes():
    jumpbox_service = JumpboxService()
    jumpboxes = jumpbox_service.get_all_jumpboxes()
    return jsonify([jumpbox.to_dict() for jumpbox in jumpboxes])

@jumpbox_controller.route('/jumpboxes/<int:jumpbox_id>', methods=['GET'])
def get_jumpbox(jumpbox_id):
    jumpbox_service = JumpboxService()
    jumpbox = jumpbox_service.get_jumpbox_by_id(jumpbox_id)
    if jumpbox:
        return jsonify(jumpbox.to_dict())
    return jsonify({'message': 'Jumpbox not found'}), 404

@jumpbox_controller.route('/jumpboxes', methods=['POST'])
def add_jumpbox():
    jumpbox_service = JumpboxService()
    jumpbox_data = request.get_json()
    jumpbox = jumpbox_service.add_jumpbox(jumpbox_data)
    return jsonify(jumpbox.to_dict()), 201

@jumpbox_controller.route('/jumpboxes/<int:jumpbox_id>', methods=['PUT'])
def update_jumpbox(jumpbox_id):
    jumpbox_service = JumpboxService()
    jumpbox_data = request.get_json()
    jumpbox = jumpbox_service.update_jumpbox(jumpbox_id, jumpbox_data)
    if jumpbox:
        return jsonify(jumpbox.to_dict())
    return jsonify({'message': 'Jumpbox not found'}), 404

@jumpbox_controller.route('/jumpboxes/<int:jumpbox_id>', methods=['DELETE'])
def delete_jumpbox(jumpbox_id):
    jumpbox_service = JumpboxService()
    jumpbox_service.delete_jumpbox(jumpbox_id)
    return jsonify({'message': 'Jumpbox deleted successfully'}), 204