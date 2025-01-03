from typing import Dict, Any
import logging

logging.basicConfig(level=logging.INFO)

class ConfigManager:
    """Manages application configuration settings."""

    def __init__(self) -> None:
        self.config: Dict[str, Any] = {}

    def load_config(self, file_path: str) -> None:
        """Loads configuration from a file."""
        try:
            with open(file_path, 'r') as file:
                self.config = json.load(file)
            logging.info(f"Configuration loaded from {file_path}.")
        except Exception as e:
            logging.error(f"Failed to load configuration: {e}")

    def get_setting(self, key: str) -> Any:
        """Retrieves a configuration setting."""
        return self.config.get(key)

    def set_setting(self, key: str, value: Any) -> None:
        """Sets a configuration setting."""
        self.config[key] = value
        logging.info(f"Configuration setting '{key}' updated to '{value}'.")