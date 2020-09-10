import logging
import time


class TennisMarathonBet:
    CLASS_K_1 = 'first-in-main-row'
    XPATH_K_1 = ".//td[contains(@class,'%s')]" % CLASS_K_1
    XPATH_K_2 = ".//td[contains(@class,'price') and not(contains(@class,'%s'))]" % CLASS_K_1
    XPATH_TABLE_MATCHES = "//table[@class='coupon-row-item']"
    SCRIPT_SCROLL_INTO_VIEW = "arguments[0].scrollIntoView();"
    SCRIPT_CHECK_ACTIVE_AJAX_PERIOD = 'return jQuery.active == 0'
    NAME_ROW = "member-link"

    def __init__(self, driver):
        self.driver = driver

    def load_page(self):
        self.driver.get('https://www.marathonbet.ru/su/popular/Tennis+-+2398')
        self.get_table_rows()
        return True

    def get_matches(self):
        table_rows = self.driver.find_elements_by_xpath(self.XPATH_TABLE_MATCHES)
        start_time = time.time()
        file_log = logging.FileHandler('Log.log')
        console_out = logging.StreamHandler()
        logging.basicConfig(level=logging.INFO, format='[%(asctime)s | %(levelname)s]: %(message)s',
                            datefmt='%m.%d.%Y %H:%M:%S', handlers=(file_log, console_out))
        matches = list(filter(has_rates, map(self.list_matches, table_rows)))
        logging.info('time for script execution %s seconds' % str(time.time() - start_time))
        return matches

    def list_matches(self, table_string):
        player_1 = (table_string.find_element_by_xpath(".//tr[1]")).find_element_by_class_name(self.NAME_ROW)
        player_2 = (table_string.find_element_by_xpath(".//tr[2]")).find_element_by_class_name(self.NAME_ROW)
        match = '%s VS %s' % (player_1.text.replace(',', ''), player_2.text.replace(',', ''))
        k_1 = table_string.find_element_by_xpath(self.XPATH_K_1).text
        k_2 = table_string.find_element_by_xpath(self.XPATH_K_2).text
        return dict(match=match, K1=k_1, K2=k_2)

    def get_table_rows(self):
        location = 0
        while True:
            table_mass = self.driver.find_elements_by_xpath(self.XPATH_TABLE_MATCHES)
            if location != table_mass[-1]:
                self.driver.execute_script(self.SCRIPT_SCROLL_INTO_VIEW, table_mass[-1])
                location = table_mass[-1]
                active_requests = self.driver.execute_script(self.SCRIPT_CHECK_ACTIVE_AJAX_PERIOD)
                while active_requests is not True:
                    active_requests = self.driver.execute_script(self.SCRIPT_CHECK_ACTIVE_AJAX_PERIOD)
                    time.sleep(0.1)
            else:
                return True


def has_rates(table_string):
    if (table_string['K1'] or table_string['K2']) == '—':
        return False
    else:
        return True