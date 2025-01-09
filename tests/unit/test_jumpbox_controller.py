import unittest
from unittest.mock import patch
from api.controllers.jumpbox_controller import JumpboxController

class TestJumpboxController(unittest.TestCase):
    @patch('api.controllers.jumpbox_controller.JumpboxService')
    def test_get_jumpboxes(self, mock_jumpbox_service):
        mock_jumpbox_service.get_all_jumpboxes.return_value = [{}]
        controller = JumpboxController()
        response = controller.get_jumpboxes()
        self.assertEqual(response.status_code, 200)

    @patch('api.controllers.jumpbox_controller.JumpboxService')
    def test_get_jumpbox(self, mock_jumpbox_service):
        mock_jumpbox_service.get_jumpbox_by_id.return_value = {}
        controller = JumpboxController()
        response = controller.get_jumpbox(1)
        self.assertEqual(response.status_code, 200)

    @patch('api.controllers.jumpbox_controller.JumpboxService')
    def test_add_jumpbox(self, mock_jumpbox_service):
        mock_jumpbox_service.add_jumpbox.return_value = {}
        controller = JumpboxController()
        response = controller.add_jumpbox({'name': 'test', 'ip_address': '192.168.1.1'})
        self.assertEqual(response.status_code, 201)

    @patch('api.controllers.jumpbox_controller.JumpboxService')
    def test_delete_jumpbox(self, mock_jumpbox_service):
        mock_jumpbox_service.delete_jumpbox.return_value = None
        controller = JumpboxController()
        response = controller.delete_jumpbox(1)
        self.assertEqual(response.status_code, 204)