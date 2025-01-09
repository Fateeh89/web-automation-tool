import unittest
from unittest.mock import patch
from api.controllers.device_controller import DeviceController

class TestDeviceController(unittest.TestCase):
    @patch('api.controllers.device_controller.DeviceService')
    def test_get_devices(self, mock_device_service):
        mock_device_service.get_all_devices.return_value = []
        controller = DeviceController()
        response = controller.get_devices()
        self.assertEqual(response.status_code, 200)

    @patch('api.controllers.device_controller.DeviceService')
    def test_get_device(self, mock_device_service):
        mock_device_service.get_device_by_id.return_value = {}
        controller = DeviceController()
        response = controller.get_device(1)
        self.assertEqual(response.status_code, 200)

    @patch('api.controllers.device_controller.DeviceService')
    def test_add_device(self, mock_device_service):
        mock_device_service.add_device.return_value = {}
        controller = DeviceController()
        response = controller.add_device({'name': 'test_device', 'ip_address': '192.168.1.2'})
        self.assertEqual(response.status_code, 201)

    @patch('api.controllers.device_controller.DeviceService')
    def test_delete_device(self, mock_device_service):
        mock_device_service.delete_device.return_value = None
        controller = DeviceController()
        response = controller.delete_device(1)
        self.assertEqual(response.status_code, 204)