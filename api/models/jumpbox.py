# api/models/jumpbox.py

from web_automation_tool.database import db
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Jumpbox(db.Model):
    """
    Represents a jumpbox connection.

    Attributes:
        id (int): Unique identifier for the jumpbox connection.
        name (str): Name of the jumpbox connection.
        ip_address (str): IP address of the jumpbox connection.
        username (str): Username for accessing the jumpbox connection.
        password (str): Password for accessing the jumpbox connection.
        created_at (datetime): Timestamp when the jumpbox connection was created.
        updated_at (datetime): Timestamp when the jumpbox connection was last updated.
    """

    __tablename__ = 'jumpboxes'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    ip_address = Column(String(64), nullable=False)
    username = Column(String(64), nullable=False)
    password = Column(String(128), nullable=False)
    created_at = Column(DateTime, default=db.func.current_timestamp())
    updated_at = Column(DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    def __init__(self, name, ip_address, username, password):
        """
        Initializes a new Jumpbox instance.

        Args:
            name (str): Name of the jumpbox connection.
            ip_address (str): IP address of the jumpbox connection.
            username (str): Username for accessing the jumpbox connection.
            password (str): Password for accessing the jumpbox connection.
        """
        self.name = name
        self.ip_address = ip_address
        self.username = username
        self.password = password

    def __repr__(self):
        """
        Returns a string representation of the Jumpbox instance.

        Returns:
            str: String representation of the Jumpbox instance.
        """
        return f"Jumpbox('{self.name}', '{self.ip_address}')"

    def to_dict(self):
        """
        Returns a dictionary representation of the Jumpbox instance.

        Returns:
            dict: Dictionary representation of the Jumpbox instance.
        """
        return {
            'id': self.id,
            'name': self.name,
            'ip_address': self.ip_address,
            'username': self.username,
            'password': self.password,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }

    def update(self, **kwargs):
        """
        Updates the Jumpbox instance with the provided attributes.

        Args:
            **kwargs: Keyword arguments to update the Jumpbox instance.
        """
        for key, value in kwargs.items():
            setattr(self, key, value)