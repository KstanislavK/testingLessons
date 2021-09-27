from selenium import webdriver
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_elem = browser.find_element_by_id('input_value')
    x = x_elem.text
    y = calc(x)

    answer = browser.find_element_by_id('answer')
    answer.send_keys(y)

    check_check = browser.find_element_by_id('robotCheckbox')
    check_check.click()

    robotR = browser.find_element_by_id('robotsRule')
    robotR.click()

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(5)
    browser.quit()
