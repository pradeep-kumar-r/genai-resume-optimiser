import logging
import os
import sys


LOG_FORMAT = "[ %(asctime)s ] - %(name)s - %(levelname)s - %(message)s"
LOG_LEVEL = logging.INFO
LOG_DIR = "../logs"
os.makedirs(LOG_DIR,exist_ok=True)
LOG_FILENAME = "running_logs.log"
LOG_PATH = os.path.join(os.getcwd(), LOG_DIR, LOG_FILENAME)


logging.basicConfig(
    format=LOG_FORMAT,
    level=LOG_LEVEL,
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler(LOG_PATH)
    ]
)

logger = logging.getLogger('resume-optimiser-logger')