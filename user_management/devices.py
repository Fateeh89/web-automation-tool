# user_management/devices.py

from services.device_service import DeviceService

class DeviceManager:
    def __init__(self):
        self.device_service = DeviceService()

    def add_device(self, device_data):
        return self.device_service.add_device(device_data)

    def get_device(self, device_id):
        return self.device_service.get_device_by_id(device_id)

    def update_device(self, device_id, device_data):
        return self.device_service.update_device(device_id, device_data)

    def delete_device(self, device_id):
        return self.device_service.delete_device(device_id)