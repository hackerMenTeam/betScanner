import os
from selenium import webdriver
from application.parsers import TennisMarathonBetModule, Tennis1xbetModule
import threading
import logging
import time


def main():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--log-level=3")
    driver_1xbet = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)
    driver_marathonbet = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)
    threading.Thread(target=start_1xbet(driver_1xbet)).start()
    threading.Thread(target=start_marathonbet(driver_marathonbet)).start()
    driver_1xbet.close()
    driver_marathonbet.close()


def start_marathonbet(driver):
    tennis = TennisMarathonBetModule.TennisMarathonBet(driver)
    tennis.load_page()
    start_time = time.time()
    file_log = logging.FileHandler('../Log.log')
    console_out = logging.StreamHandler()
    logging.basicConfig(level=logging.INFO, format='[%(asctime)s | %(levelname)s]: %(message)s',
                        datefmt='%m.%d.%Y %H:%M:%S', handlers=(file_log, console_out))
    matches = dict(bookmaker_key='1xbet', matches=tennis.get_matches())
    print(matches)
    logging.info('time for script execution %s seconds' % str(time.time() - start_time))


def start_1xbet(driver):
    tennis = Tennis1xbetModule.Tennis1xbet(driver)
    tennis.load_page()
    start_time = time.time()
    file_log = logging.FileHandler('../Log.log')
    console_out = logging.StreamHandler()
    logging.basicConfig(level=logging.INFO, format='[%(asctime)s | %(levelname)s]: %(message)s',
                        datefmt='%m.%d.%Y %H:%M:%S', handlers=(file_log, console_out))
    matches = dict(bookmaker_key='marathonbet', matches=tennis.get_matches())
    print(matches)
    logging.info('time for script execution %s seconds' % str(time.time() - start_time))


if __name__ == "__main__":
    main()
