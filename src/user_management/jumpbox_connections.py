from typing import Dict, Any
import logging
from dataclasses import dataclass

logging.basicConfig(level=logging.INFO)

@dataclass
class JumpboxDetails:
    hostname: str
    username: str
    password: str
    port: int

class JumpboxConnectionManager:
    """Manages jumpbox connections with CRUD operations."""

    def __init__(self) -> None:
        self.connections: Dict[str, JumpboxDetails] = {}

    def add_connection(self, name: str, details: JumpboxDetails) -> None:
        """Adds a new jumpbox connection."""
        if name in self.connections:
            logging.error(f"Connection '{name}' already exists.")
            raise ValueError("Connection already exists.")
        self.connections[name] = details
        logging.info(f"Connection '{name}' added successfully.")

    def edit_connection(self, name: str, new_details: JumpboxDetails) -> None:
        """Edits an existing jumpbox connection."""
        if name not in self.connections:
            logging.error(f"Connection '{name}' does not exist.")
            raise ValueError("Connection does not exist.")
        self.connections[name] = new_details
        logging.info(f"Connection '{name}' updated successfully.")

    def delete_connection(self, name: str) -> None:
        """Deletes a jumpbox connection."""
        if name not in self.connections:
            logging.error(f"Connection '{name}' does not exist.")
            raise ValueError("Connection does not exist.")
        del self.connections[name]
        logging.info(f"Connection '{name}' deleted successfully.")

    def __str__(self) -> str:
        """String representation of all connections."""
        return "\n".join([f"{name}: {details}" for name, details in self.connections.items()])