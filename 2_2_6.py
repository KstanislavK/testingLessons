from selenium import webdriver
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    elem = browser.find_element_by_id('input_value')
    x = elem.text
    y = calc(x)

    answer = browser.find_element_by_id('answer')
    answer.send_keys(y)

    check_check = browser.find_element_by_id('robotCheckbox')
    check_check.click()

    robotR = browser.find_element_by_id('robotsRule')
    robotR.click()

    button = browser.find_element_by_css_selector("button.btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла

