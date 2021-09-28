import math
import time


def btn_click(browser):
    button = browser.find_element_by_css_selector("button.btn")
    button.click()


def btn_click_id(browser, id):
    button = browser.find_element_by_id(id)
    button.click()


def calc(browser):
    elem = browser.find_element_by_id('input_value')
    x = elem.text

    y = str(math.log(abs(12 * math.sin(int(x)))))
    answer = browser.find_element_by_id('answer')
    answer.send_keys(y)


def final_step(browser):
    time.sleep(10)
    browser.quit()


def switch_to_new_window(x, browser):
    first_window = browser.window_handles[0]

    new_window = browser.window_handles[x]
    browser.switch_to.window(new_window)
    return first_window
