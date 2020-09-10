import logging
import time
from selenium.common.exceptions import NoSuchElementException


class Tennis1xbet:
    XPATH_PLAYER_1 = ".//div[@class='c-events-scoreboard__team-wrap'][1]"
    XPATH_PLAYER_2 = ".//div[@class='c-events-scoreboard__team-wrap'][2]"
    XPATH_K_1 = ".//span[@class='c-bets__bet c-bets__bet_coef c-bets__bet_sm'][1]"
    XPATH_K_2 = ".//span[@class='c-bets__bet c-bets__bet_coef c-bets__bet_sm'][2]"
    CLASS_TABLE_MATCHES = 'c-events-scoreboard__wrap'

    def __init__(self, driver):
        self.driver = driver

    def load_page(self):
        self.driver.get('https://1xstavka.ru/live/Tennis/')
        return True

    def get_matches(self):
        table_rows = self.driver.find_elements_by_class_name(self.CLASS_TABLE_MATCHES)
        start_time = time.time()
        file_log = logging.FileHandler('Log.log')
        console_out = logging.StreamHandler()
        logging.basicConfig(level=logging.INFO, format='[%(asctime)s | %(levelname)s]: %(message)s',
                            datefmt='%m.%d.%Y %H:%M:%S', handlers=(file_log, console_out))
        matches = list(map(self.list_matches, table_rows))
        logging.info('time for script execution %s seconds' % str(time.time() - start_time))
        return matches

    def list_matches(self, table_string):
        player_1 = get_name((table_string.find_element_by_xpath(self.XPATH_PLAYER_1)).text)
        player_2 = get_name((table_string.find_element_by_xpath(self.XPATH_PLAYER_2)).text)
        match = '%s VS %s' % (player_1, player_2)
        try:
            k_1 = table_string.find_element_by_xpath(self.XPATH_K_1).text
            k_2 = table_string.find_element_by_xpath(self.XPATH_K_2).text
            return dict(match=match, K1=k_1, K2=k_2)
        except NoSuchElementException:
            pass


def get_name(name):
    try:
        return name[: name.index('(')]
    except ValueError:
        return name
