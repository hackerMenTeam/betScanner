import time
from lxml import html


class TennisMarathonBet:
    XPATH_TABLE_MATCHES = "//table[@class='coupon-row-item']"
    XPATH_PLAYER = ".//a[@class='member-link']"
    CLASS_K_1 = "first-in-main-row"
    XPATH_K_1 = ".//td[contains(@class,'%s')]" % CLASS_K_1
    XPATH_K_2 = ".//td[contains(@class,'price') and not(contains(@class,'%s'))]" % CLASS_K_1
    SCRIPT_SCROLL_INTO_VIEW = "arguments[0].scrollIntoView();"
    SCRIPT_CHECK_ACTIVE_AJAX_PERIOD = "return jQuery.active == 0"

    def __init__(self, driver):
        self.driver = driver

    def load_page(self):
        self.driver.get('https://www.marathonbet.ru/su/popular/Tennis+-+2398')
        self.get_table_rows()
        return True

    def get_matches(self):
        tree = html.fromstring(self.driver.page_source)
        table_rows = tree.xpath(self.XPATH_TABLE_MATCHES)
        matches = list(filter(has_rates, map(self.list_matches, table_rows)))
        return matches

    def list_matches(self, table_row):
        player_1 = table_row.xpath(self.XPATH_PLAYER)[0].text_content().strip()
        player_2 = table_row.xpath(self.XPATH_PLAYER)[1].text_content().strip()
        match = '%s VS %s' % (player_1.replace(',', ''), player_2.replace(',', ''))
        k_1 = table_row.xpath(self.XPATH_K_1)[0].text_content().strip()
        k_2 = table_row.xpath(self.XPATH_K_2)[0].text_content().strip()
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


def has_rates(table_row):
    if (table_row['K1'] or table_row['K2']) == '—':
        return False
    else:
        return True
