import time

import logging

from selenium import webdriver


def main():
    driver = webdriver.Chrome()
    driver.get("https://www.marathonbet.ru/su/")
    btn_tennis = driver.find_element_by_class_name("icon-sport-tennis")
    btn_tennis.click()
    logging.basicConfig(level=logging.INFO, filename='./myapp.log', format='%(asctime)s %(levelname)s:%(message)s')
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s:%(message)s')
    logging.info('start tennis page')
    buf = []
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
        buf.append(table)
    # print(buf)
    logging.info('end of program')
    driver.close()
    return len(table_mass)


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
