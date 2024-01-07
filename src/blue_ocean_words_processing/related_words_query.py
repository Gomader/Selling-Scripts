import logging
import os
import shutil
import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from tqdm import tqdm

from blue_ocean_words_processing.config import BlueOceanWordQueryConfig
from configs.config import Config
from configs.urls import MYSYCM
from login.mysycm import login_mysycm

logger = logging.getLogger(__name__)


def read_word_root() -> list:
    logger.info('Reading word root file...')
    with open(BlueOceanWordQueryConfig.WORD_ROOT_FILE, encoding='utf-8') as f:
        words = f.read().split('、')
        logger.info(f'Read word root file successfully. Total words: {len(words)}')
        return words


def get_related_words(word_root):
    logger.info('Getting related words...')
    browser = login_mysycm()
    browser.get(MYSYCM.SSFX)

    time.sleep(1)

    for word in tqdm(word_root, desc='Getting related words...'):
        browser.find_element(By.ID, 'keyword').clear()
        browser.find_element(By.ID, 'keyword').send_keys(word)
        browser.find_element(By.ID, 'keyword').send_keys(Keys.ENTER)
        time.sleep(5)
        download_btn = browser.find_element(By.XPATH, '//button[@class="dt-button buttons-csv buttons-html5"]')
        browser.execute_script('arguments[0].click();', download_btn)
        time.sleep(5)
        os.rename(os.path.join(Config.DOWNLOAD_DIR, '生意参谋查词 市场行情查词 在线查词 生意参谋 查词 标题权重 做标题.csv'),
                  os.path.join(Config.DOWNLOAD_DIR, f'{word}.csv'))
        shutil.move(os.path.join(Config.DOWNLOAD_DIR, f'{word}.csv'),
                    os.path.join(Config.BLUE_OCEAN_WORDS_PROCESSING_FOLDER, 'raw_data'))


def run():
    word_root = read_word_root()
    get_related_words(word_root=word_root)


if __name__ == '__main__':
    logger.info('Run query related words by file self.')
    run()
