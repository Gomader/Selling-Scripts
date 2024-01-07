from selenium.webdriver.chrome.options import Options
from selenium import webdriver

from config.config import Config


def get_chrome_window():
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--headless')
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

    browser = webdriver.Chrome(options=chrome_options)

    browser.maximize_window()

    return browser


def get_window():
    return {
        "CHROME": get_chrome_window
    }[Config.DRIVER]()
