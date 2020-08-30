import time
from datetime import datetime

import logging

from selenium import webdriver


def main():
    driver = webdriver.Chrome()
    driver.get("https://www.marathonbet.ru/su/")
    btn_tennis = driver.find_element_by_class_name("icon-sport-tennis")
    btn_tennis.click()
    start_time = time.time()
    file_log = logging.FileHandler('Log.log')
    console_out = logging.StreamHandler()
    logging.basicConfig(handlers=(file_log, console_out), format='[%(asctime)s | %(levelname)s]: %(message)s',
                        datefmt='%m.%d.%Y %H:%M:%S', level=logging.INFO)
    mathes = []
    table_mass=scrollToTheEnd(driver)
    for i in table_mass:
        match = (i.find_element_by_xpath(
            ".//table[@class='member-area-content-table ']/tbody/tr[1]")).find_element_by_class_name(
            "member-link").text.replace(',', '') \
                + ' VS ' + (i.find_element_by_xpath(
            ".//table[@class='member-area-content-table ']/tbody/tr[2]")).find_element_by_class_name(
            "member-link").text.replace(',', '')
        k1 = i.find_element_by_xpath(".//td[contains(@class,'first-in-main-row')]").text
        k2 = i.find_element_by_xpath(
            ".//td[contains(@class,'price') and not(contains(@class,'first-in-main-row'))]").text
        table = dict(match=match, K1=k1, K2=k2)
        mathes.append(table)
    print(mathes)
    logging.info('time for script execution %s seconds'% str(time.time() - start_time))
    driver.close()


def scrollToTheEnd(driver):
    location = 0
    while True:
        table_mass = driver.find_elements_by_xpath("//table[@class='coupon-row-item']")
        if location != table_mass[-1]:
            table_mass[-1].location_once_scrolled_into_view
            location = table_mass[-1]
            time.sleep(2)
        else:
            return table_mass


if __name__ == "__main__":
    main()
