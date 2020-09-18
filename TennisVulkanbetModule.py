import time
import logging


class TennisVulcanbet:
    def __init__(self, driver):
        self.driver = driver

    def load_page(self):
        self.driver.get('https://vulkanbet.ru/sports/tournament/betting:7:sr:tournament:11499')
        start_time = time.time()
        file_log = logging.FileHandler('Log.log')
        console_out = logging.StreamHandler()
        logging.basicConfig(level=logging.INFO, format='[%(asctime)s | %(levelname)s]: %(message)s',
                            datefmt='%m.%d.%Y %H:%M:%S', handlers=(file_log, console_out))
        print(self.driver.page_source)
        logging.info('time for script execution %s seconds' % str(time.time() - start_time))

        self.get_matches()
        return True

    def get_matches(self):
        time.sleep(2)
        a=self.driver.find_elements_by_xpath("//div[contains(@class,'categorizerTournamentRow__row___38Ex_')]")
        a[0].click( )
        time.sleep(3)
