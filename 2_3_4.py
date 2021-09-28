from selenium import webdriver
import time
import funcs_all

link = "http://suninjuly.github.io/alert_accept.html"


try:
    browser = webdriver.Chrome()
    browser.get(link)

    funcs_all.btn_click(browser)

    modal_w = browser.switch_to.alert
    modal_w.accept()

    elem = browser.find_element_by_id('input_value')
    x = elem.text
    y = funcs_all.calc(x)

    answer = browser.find_element_by_id('answer')
    answer.send_keys(y)

    funcs_all.btn_click(browser)

finally:
    time.sleep(5)
    browser.quit()
