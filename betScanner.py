import time
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
    matches = list(filter(delete_bets_without_odds, map(massive_of_matches, massive_of_table_strings(driver))))
    print(matches)
    logging.info('time for script execution %s seconds' % str(time.time() - start_time))
    driver.close()
    return len(matches)


def delete_bets_without_odds(table_string):
    if (table_string['K1'] or table_string['K2']) == '—':
        return 0
    else:
        return 1


def massive_of_matches(table_string):
    player1 = (table_string.find_element_by_xpath(".//tr[1]")).find_element_by_class_name("member-link")
    player2 = (table_string.find_element_by_xpath(".//tr[2]")).find_element_by_class_name("member-link")
    match = player1.text.replace(',', '') + ' VS ' + player2.text.replace(',', '')
    k1 = table_string.find_element_by_xpath(".//td[contains(@class,'first-in-main-row')]").text
    k2 = table_string.find_element_by_xpath(
        ".//td[contains(@class,'price') and not(contains(@class,'first-in-main-row'))]").text
    return dict(match=match, K1=k1, K2=k2)


def massive_of_table_strings(driver):
    location = 0
    while True:
        table_mass = driver.find_elements_by_xpath("//table[@class='coupon-row-item']")
        if location != table_mass[-1]:
            driver.execute_script("arguments[0].scrollIntoView();", table_mass[-1])
            location = table_mass[-1]
            time.sleep(0.1)
            active_requests = driver.execute_script('return jQuery.active == 0')
            while active_requests is not True:
                active_requests = driver.execute_script('return jQuery.active == 0')
                time.sleep(0.1)
        else:
            return table_mass


if __name__ == "__main__":
    main()
