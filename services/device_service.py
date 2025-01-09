# services/device_service.py

from api.models.device import Device

class DeviceService:
    def __init__(self):
        self.device_model = Device

    def get_all_devices(self):
        return self.device_model.query.all()

    def get_device_by_id(self, device_id):
        return self.device_model.query.get(device_id)

    def add_device(self, device_data):
        device = self.device_model(name=device_data['name'], type=device_data['type'], ip_address=device_data['ip_address'])
        db.session.add(device)
        db.session.commit()
        return device

    def update_device(self, device_id, device_data):
        device = self.get_device_by_id(device_id)
        if device:
            device.name = device_data['name']
            device.type = device_data['type']
            device.ip_address = device_data['ip_address']
            db.session.commit()
            return device
        return None

    def delete_device(self, device_id):
        device = self.get_device_by_id(device_id)
        if device:
            db.session.delete(device)
            db.session.commit()
            return True
        return False