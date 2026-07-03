import logging


logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)


def wifi():
    logger.info(f"Module: {__name__}, file_path: {__file__}: Connecting to wifi")


def mobile_internet():
    print("Connecting to mobile internet")


def wire_internet():
    print("Connecting to wire internet")