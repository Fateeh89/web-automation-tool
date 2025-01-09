# services/jumpbox_service.py

from api.models.jumpbox import Jumpbox

class JumpboxService:
    def __init__(self):
        self.jumpbox_model = Jumpbox

    def get_all_jumpboxes(self):
        return self.jumpbox_model.query.all()

    def get_jumpbox_by_id(self, jumpbox_id):
        return self.jumpbox_model.query.get(jumpbox_id)

    def add_jumpbox(self, jumpbox_data):
        jumpbox = self.jumpbox_model(name=jumpbox_data['name'], ip_address=jumpbox_data['ip_address'])
        db.session.add(jumpbox)
        db.session.commit()
        return jumpbox

    def update_jumpbox(self, jumpbox_id, jumpbox_data):
        jumpbox = self.get_jumpbox_by_id(jumpbox_id)
        if jumpbox:
            jumpbox.name = jumpbox_data['name']
            jumpbox.ip_address = jumpbox_data['ip_address']
            db.session.commit()
            return jumpbox
        return None

    def delete_jumpbox(self, jumpbox_id):
        jumpbox = self.get_jumpbox_by_id(jumpbox_id)
        if jumpbox:
            db.session.delete(jumpbox)
            db.session.commit()
            return True
        return False