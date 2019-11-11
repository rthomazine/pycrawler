import logging
import sys
from configparser import ConfigParser
from os import path, getcwd

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

config = ConfigParser()
file_name = f"{getcwd()}/config.cfg"
if not path.exists(file_name):
    logger.exception('Config file is missing')
    sys.exit()
config.read(file_name)
