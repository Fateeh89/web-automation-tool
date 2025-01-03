from typing import Dict, Any, List
import logging
from dataclasses import dataclass

logging.basicConfig(level=logging.INFO)

@dataclass
class DeviceInfo:
    type: str
    ipAddress: str
    status: str

class DeviceManager:
    """Manages devices with CRUD operations."""

    def __init__(self) -> None:
        self.devices: Dict[str, DeviceInfo] = {}

    def add_device(self, device_id: str, device_info: DeviceInfo) -> bool:
        """Adds a new device."""
        if device_id in self.devices:
            logging.warning(f"Device '{device_id}' already exists.")
            return False
        self.devices[device_id] = device_info
        logging.info(f"Device '{device_id}' added successfully.")
        return True

    def edit_device(self, device_id: str, device_info: DeviceInfo) -> bool:
        """Edits an existing device."""
        if device_id not in self.devices:
            logging.error(f"Device '{device_id}' not found.")
            return False
        self.devices[device_id] = device_info
        logging.info(f"Device '{device_id}' updated successfully.")
        return True

    def delete_device(self, device_id: str) -> bool:
        """Deletes a device."""
        if device_id not in self.devices:
            logging.error(f"Device '{device_id}' not found.")
            return False
        del self.devices[device_id]
        logging.info(f"Device '{device_id}' deleted successfully.")
        return True

    def list_devices(self) -> List[DeviceInfo]:
        """Returns a list of all devices."""
        return list(self.devices.values())

    def __str__(self) -> str:
        """String representation of all devices."""
        return "\n".join([f"{device_id}: {info}" for device_id, info in self.devices.items()])