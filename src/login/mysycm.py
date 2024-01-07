import logging

from selenium.webdriver.common.by import By

from configs.urls import MYSYCM
from utils.drivers import get_window

logger = logging.getLogger(__name__)


def login_mysycm():
    logger.info('Logging in mysycm...')

    browser = get_window()
    browser.get(MYSYCM.LOGIN)

    browser.find_element(By.ID, 'mobile').send_keys(MYSYCM.USERNAME)
    browser.find_element(By.ID, 'password').send_keys(MYSYCM.PASSWORD)

    submit_btn = browser.find_element(By.ID, "login")
    browser.execute_script('arguments[0].click();', submit_btn)

    return browser


if __name__ == '__main__':
    login_mysycm()
