# logger.py

import logging
import sys

def setup_logger(log_level="INFO", log_file_path=None):
    log_level_enum = getattr(logging, log_level.upper(), logging.INFO)

    logger = logging.getLogger("COSMOS_LOGGER")
    logger.setLevel(log_level_enum)

    if logger.hasHandlers():
        logger.handlers.clear()

    # Handler do Console
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)
    console_formatter = logging.Formatter('[%(levelname)s] %(message)s')
    console_handler.setFormatter(console_formatter)
    logger.addHandler(console_handler)

    # Handler do Arquivo
    if log_file_path:
        file_handler = logging.FileHandler(log_file_path, mode='w')
        file_handler.setLevel(logging.DEBUG)
        file_formatter = logging.Formatter('%(asctime)s - [%(levelname)s] - %(module)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
        file_handler.setFormatter(file_formatter)
        logger.addHandler(file_handler)

    return logger