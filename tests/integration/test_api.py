import unittest
from api import app

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_get_devices(self):
        response = self.app.get('/api/devices')
        self.assertEqual(response.status_code, 200)

    def test_get_device(self):
        response = self.app.get('/api/devices/1')
        self.assertEqual(response.status_code, 200)

    def test_add_device(self):
        data = {'device_id': 1, 'device_type': 'router', 'device_address': '192.168.1.1'}
        response = self.app.post('/api/devices', json=data)
        self.assertEqual(response.status_code, 201)

    def test_update_device(self):
        data = {'device_id': 1, 'device_type': 'router', 'device_address': '192.168.1.1'}
        response = self.app.put('/api/devices/1', json=data)
        self.assertEqual(response.status_code, 200)

    def test_delete_device(self):
        response = self.app.delete('/api/devices/1')
        self.assertEqual(response.status_code, 204)

if __name__ == '__main__':
    unittest.main()