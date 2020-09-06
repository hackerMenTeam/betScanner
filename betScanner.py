import time
import logging
import os
from selenium import webdriver


def main():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--log-level=3")
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)
    tennis = Tennis(driver)
    tennis.load_page()
    print(tennis.get_matches())
    driver.close()


def has_rates(table_string):
    if (table_string['K1'] or table_string['K2']) == '—':
        return False
    else:
        return True


class Tennis:
    CLASS_K_1 = 'first-in-main-row'
    XPATH_K_1 = ".//td[contains(@class,'%s')]" % CLASS_K_1
    XPATH_K_2 = ".//td[contains(@class,'price') and not(contains(@class,'%s'))]" % CLASS_K_1
    XPATH_TABLE_MATCHES = "//table[@class='coupon-row-item']"
    XPATH_TABLE_MATCHES = "//table[@class='coupon-row-item']"
    SCRIPT_SCROLL_INTO_VIEW = "arguments[0].scrollIntoView();"
    SCRIPT_ACTIVE_AJAX = 'return jQuery.active == 0'

    def __init__(self, driver):
        self.driver = driver

    def load_page(self):
        self.driver.get("https://www.marathonbet.ru/su/")
        self.driver.find_element_by_class_name("icon-sport-tennis").click()
        self.get_table_rows()
        return True

    def get_matches(self):
        table_mass = self.driver.find_elements_by_xpath(Tennis.XPATH_TABLE_MATCHES)
        start_time = time.time()
        file_log = logging.FileHandler('Log.log')
        console_out = logging.StreamHandler()
        logging.basicConfig(handlers=(file_log, console_out), format='[%(asctime)s | %(levelname)s]: %(message)s',
                            datefmt='%m.%d.%Y %H:%M:%S', level=logging.INFO)
        matches = list(filter(has_rates, map(self.get_list_matches, table_mass)))
        logging.info('time for script execution %s seconds' % str(time.time() - start_time))
        return matches

    def get_list_matches(self, table_string):
        name_row = "member-link"
        player_1 = (table_string.find_element_by_xpath(".//tr[1]")).find_element_by_class_name(name_row)
        player_2 = (table_string.find_element_by_xpath(".//tr[2]")).find_element_by_class_name(name_row)
        match = player_1.text.replace(',', '') + ' VS ' + player_2.text.replace(',', '')
        k_1 = table_string.find_element_by_xpath(Tennis.XPATH_K_1).text
        k_2 = table_string.find_element_by_xpath(Tennis.XPATH_K_2).text
        return dict(match=match, K1=k_1, K2=k_2)

    def get_table_rows(self):
        location = 0
        while True:
            table_mass = self.driver.find_elements_by_xpath(Tennis.XPATH_TABLE_MATCHES)
            if location != table_mass[-1]:
                self.driver.execute_script(Tennis.SCRIPT_SCROLL_INTO_VIEW, table_mass[-1])
                location = table_mass[-1]
                active_requests = self.driver.execute_script(Tennis.SCRIPT_ACTIVE_AJAX)
                while active_requests is not True:
                    active_requests = self.driver.execute_script(Tennis.SCRIPT_ACTIVE_AJAX)
                    time.sleep(0.1)
            else:
                return True


if __name__ == "__main__":
    main()
