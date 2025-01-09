# user_management/jumpbox_connections.py

from services.jumpbox_service import JumpboxService

class JumpboxConnectionManager:
    def __init__(self):
        self.jumpbox_service = JumpboxService()

    def add_jumpbox(self, jumpbox_data):
        return self.jumpbox_service.add_jumpbox(jumpbox_data)

    def get_jumpbox(self, jumpbox_id):
        return self.jumpbox_service.get_jumpbox_by_id(jumpbox_id)

    def update_jumpbox(self, jumpbox_id, jumpbox_data):
        return self.jumpbox_service.update_jumpbox(jumpbox_id, jumpbox_data)

    def delete_jumpbox(self, jumpbox_id):
        return self.jumpbox_service.delete_jumpbox(jumpbox_id)