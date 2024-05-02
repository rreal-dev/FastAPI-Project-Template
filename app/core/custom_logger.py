# app/core/custom_logger.py
import logging

def get_logger(name):
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

    handler = logging.StreamHandler()
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    logger.addHandler(handler)

    return logger

