import time

import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def extract_time(starting_point, ending_point):
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    op = webdriver.ChromeOptions()
    op.add_argument('headless')
    driver = webdriver.Chrome(PATH, options=op)

    maps_time_address = "https://www.bing.com/maps/"
    driver.get(maps_time_address)

    # ACCEPTING COOKIES
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#bnp_btn_accept"))).click()

    directions_btn = driver.find_element_by_class_name("directionsIcon")
    directions_btn.click()
    time.sleep(2)

    start = driver.find_element_by_css_selector(".start+ input")
    end = driver.find_element_by_css_selector(".end+ input")

    start.send_keys(starting_point)
    end.send_keys(ending_point)

    go_btn = driver.find_element_by_class_name("dirBtnGo.commonButton")
    go_btn.click()

    time_minutes = None
    time_hours = None
    while time_hours is None:
        try:
            time_hours = driver.find_element_by_class_name('drHours')
            time_minutes = driver.find_element_by_class_name('drMins')
        except selenium.common.exceptions.NoSuchElementException:
            pass

    travel_time = f"{time_hours.text} h: {time_minutes.text} min"
    print(travel_time)


if __name__ == '__main__':
    extract_time('43.203714,23.547599', '22.6975,23.3241')
