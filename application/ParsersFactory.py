import os

from selenium import webdriver
from application.parsers.TennisMarathonBetModule import TennisMarathonBet
from application.parsers.Tennis1xbetModule import Tennis1xbet
from .model import Bookmaker


def create_pages():
    criteria = Bookmaker.Criteria()
    criteria.is_enabled = True
    bookmakers = Bookmaker.list_by_criteria(criteria)
    return list(map(lambda bookmaker: _init_page(bookmaker.name), bookmakers))


def _init_page(bookmaker_key):
    key_to_page_map = {
        TennisMarathonBet.KEY: lambda driver: TennisMarathonBet(driver),
        Tennis1xbet.KEY: lambda driver: Tennis1xbet(driver)
    }
    page_creator = key_to_page_map.get(bookmaker_key)
    return page_creator(_create_driver())


def _create_driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--log-level=3")
    return webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)
