from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element_by_id('num1')
    x = num1.text

    num2 = browser.find_element_by_id('num2')
    y = num2.text

    z = int(x) + int(y)

    select = Select(browser.find_element_by_tag_name('select'))
    select.select_by_value(str(z))

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(5)
    browser.quit()
