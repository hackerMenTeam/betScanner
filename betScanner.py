import os
from selenium import webdriver
import TennisMarathonBetModule


def main():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--log-level=3")
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)
    tennis = TennisMarathonBetModule.TennisMarathonBet(driver)
    tennis.load_page()
    print(tennis.get_matches())
    driver.close()


if __name__ == "__main__":
    main()
