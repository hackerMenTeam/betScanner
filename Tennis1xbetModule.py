import logging
import time
import re
from lxml import html


class Tennis1xbet:
    XPATH_TABLE_MATCHES = "//div[contains(@class,'c-events-scoreboard__wrap')]"
    XPATH_PLAYER_1 = ".//div[@class='c-events-scoreboard__team-wrap'][1]"
    XPATH_PLAYER_2 = ".//div[@class='c-events-scoreboard__team-wrap'][2]"
    XPATH_K_1 = ".//span[@title='П1']"
    XPATH_K_2 = ".//span[@title='П2']"

    def __init__(self, driver):
        self.driver = driver

    def load_page(self):
        self.driver.get('https://1xstavka.ru/live/Tennis/')
        return True

    def get_matches(self):
        page = self.driver.page_source
        tree = html.fromstring(page)
        table_rows = tree.xpath(self.XPATH_TABLE_MATCHES)
        start_time = time.time()
        file_log = logging.FileHandler('Log.log')
        console_out = logging.StreamHandler()
        logging.basicConfig(level=logging.INFO, format='[%(asctime)s | %(levelname)s]: %(message)s',
                            datefmt='%m.%d.%Y %H:%M:%S', handlers=(file_log, console_out))
        matches = list(map(self.list_matches, table_rows))
        logging.info('time for script execution %s seconds' % str(time.time() - start_time))
        return matches

    def list_matches(self, table_row):
        player_1 = get_name(table_row.xpath(self.XPATH_PLAYER_1)[0].text_content())
        player_2 = get_name(table_row.xpath(self.XPATH_PLAYER_2)[0].text_content())
        match = '%s VS %s' % (player_1, player_2)
        try:
            # the exception is triggered when the rates are not set
            k_1 = re.sub(r'[^0-9.]+', r'', table_row.xpath(self.XPATH_K_1)[0].text_content())
            k_2 = re.sub(r'[^0-9.]+', r'', table_row.xpath(self.XPATH_K_2)[0].text_content())
            return dict(match=match, K1=k_1, K2=k_2)
        except IndexError:
            pass


def get_name(name):
    try:
        return name[: name.index('(')]
    except ValueError:
        return name
