import funcs_all
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
    funcs_all.btn_click(browser)

    funcs_all.calc(browser)

    funcs_all.btn_click_id(browser, id='solve')

finally:
    funcs_all.final_step(browser)
