import logging.config
import os

from configs.logger_config import LoggerConfig

logger = logging.getLogger(__name__)
logging.config.dictConfig(LoggerConfig.dictConfig)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


class Config:
    DEBUG = True
    DRIVER = 'CHROME'

    DOWNLOAD_DIR = 'C:\\Users\\宫赫\\Downloads'
    BLUE_OCEAN_WORDS_PROCESSING_FOLDER = os.path.join(BASE_DIR, 'blue_ocean_words_processing')
