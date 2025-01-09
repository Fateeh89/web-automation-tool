# api/models/device.py

from web_automation_tool.database import db
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Device(db.Model):
    """
    Represents a network device.

    Attributes:
        id (int): Unique identifier for the device.
        name (str): Name of the device.
        type (str): Type of the device (e.g., router, switch, firewall).
        ip_address (str): IP address of the device.
        username (str): Username for accessing the device.
        password (str): Password for accessing the device.
        created_at (datetime): Timestamp when the device was created.
        updated_at (datetime): Timestamp when the device was last updated.
    """

    __tablename__ = 'devices'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    type = Column(String(50), nullable=False)
    ip_address = Column(String(64), nullable=False)
    username = Column(String(64), nullable=False)
    password = Column(String(128), nullable=False)
    created_at = Column(DateTime, default=db.func.current_timestamp())
    updated_at = Column(DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    def __init__(self, name, type, ip_address, username, password):
        """
        Initializes a new Device instance.

        Args:
            name (str): Name of the device.
            type (str): Type of the device.
            ip_address (str): IP address of the device.
            username (str): Username for accessing the device.
            password (str): Password for accessing the device.
        """
        self.name = name
        self.type = type
        self.ip_address = ip_address
        self.username = username
        self.password = password

    def __repr__(self):
        """
        Returns a string representation of the Device instance.

        Returns:
            str: String representation of the Device instance.
        """
        return f"Device('{self.name}', '{self.type}', '{self.ip_address}')"

    def to_dict(self):
        """
        Returns a dictionary representation of the Device instance.

        Returns:
            dict: Dictionary representation of the Device instance.
        """
        return {
            'id': self.id,
            'name': self.name,
            'type': self.type,
            'ip_address': self.ip_address,
            'username': self.username,
            'password': self.password,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }

    def update(self, **kwargs):
        """
        Updates the Device instance with the provided attributes.

        Args:
            **kwargs: Keyword arguments to update the Device instance.
        """
        for key, value in kwargs.items():
            setattr(self, key, value)