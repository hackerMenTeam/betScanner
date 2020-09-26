import os
from selenium import webdriver
import TennisMarathonBetModule
import Tennis1xbetModule
import logging
import time
import asyncio
from concurrent.futures.thread import ThreadPoolExecutor


def main():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    # chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--log-level=3")
    driver_1xbet = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)
    driver_marathonbet = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)
    read_data([start_1xbet, start_marathonbet], [driver_1xbet, driver_marathonbet])


def start_marathonbet(driver):
    tennis = TennisMarathonBetModule.TennisMarathonBet(driver)
    tennis.load_page()
    start_time = time.time()
    file_log = logging.FileHandler('Log.log')
    console_out = logging.StreamHandler()
    logging.basicConfig(level=logging.INFO, format='[%(asctime)s | %(levelname)s]: %(message)s',
                        datefmt='%m.%d.%Y %H:%M:%S', handlers=(file_log, console_out))
    matches = dict(bookmaker_key='1xbet', matches=tennis.get_matches())
    print(matches)
    logging.info('time for script execution %s seconds' % str(time.time() - start_time))
    driver.close()
    return matches


def start_1xbet(driver):
    tennis = Tennis1xbetModule.Tennis1xbet(driver)
    tennis.load_page()
    start_time = time.time()
    file_log = logging.FileHandler('Log.log')
    console_out = logging.StreamHandler()
    logging.basicConfig(level=logging.INFO, format='[%(asctime)s | %(levelname)s]: %(message)s',
                        datefmt='%m.%d.%Y %H:%M:%S', handlers=(file_log, console_out))
    matches = dict(bookmaker_key='marathonbet', matches=tennis.get_matches())
    print(matches)
    logging.info('time for script execution %s seconds' % str(time.time() - start_time))
    driver.close()
    return matches


def read_data(scanners, drivers):
    loop_answer = []
    executor = ThreadPoolExecutor(10)
    loop = asyncio.get_event_loop()
    for i in range(len(scanners)):
        loop_answer.append(loop.run_in_executor(executor, scanners[i], drivers[i]))
    loop.run_until_complete(asyncio.gather(*loop_answer))
    print("Ответ ", loop_answer)
    return loop_answer


if __name__ == "__main__":
    main()
