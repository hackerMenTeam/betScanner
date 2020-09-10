import os
from selenium import webdriver
import TennisMarathonBetModule
import Tennis1xbetModule
import threading


def main():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--log-level=3")
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)
    threading.Thread(target=start_1xbet(driver)).start()
    threading.Thread(target=start_marathonbet(driver)).start()
    driver.close()


def start_marathonbet(driver):
    tennis = TennisMarathonBetModule.TennisMarathonBet(driver)
    tennis.load_page()
    print(tennis.get_matches())


def start_1xbet(driver):
    tennis = Tennis1xbetModule.Tennis1xbet(driver)
    tennis.load_page()
    print(tennis.get_matches())


if __name__ == "__main__":
    main()
