"""Logging Module using a convenient loguru wrapper library"""

import os
from loguru import logger


LOG_DIR = "../logs"
os.makedirs(LOG_DIR,exist_ok=True)
LOG_FILENAME = "running_logs.log"
LOG_PATH = os.path.join(LOG_DIR, LOG_FILENAME)
logger.add(LOG_PATH)

if __name__ == "__main__":
    logger.info("Testing whether logging works")
    