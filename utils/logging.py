# utils/logging.py

import logging
from logging.handlers import RotatingFileHandler
from flask import current_app

def setup_logging():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    file_handler = RotatingFileHandler('web_automation_tool.log', maxBytes=1000000, backupCount=1)
    file_handler.setFormatter(formatter)

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    return logger

logger = setup_logging()
