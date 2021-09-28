import unittest
from selenium import webdriver
import funcs_all
import time


class TestUserReg(unittest.TestCase):
    def test_reg_1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
        funcs_all.get_and_insert(browser, '.first_block .first', 'Ivan')
        funcs_all.get_and_insert(browser, '.first_block .second', 'Ivanov')
        funcs_all.get_and_insert(browser, '.first_block .third', 'ivan@ivanov.test')

        funcs_all.btn_click(browser)

        time.sleep(1)

        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!")

    def test_reg_2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)
        funcs_all.get_and_insert(browser, '.first_block .first', 'Ivan')
        funcs_all.get_and_insert(browser, '.first_block .second', 'Ivanov')
        funcs_all.get_and_insert(browser, '.first_block .third', 'ivan@ivanov.test')

        funcs_all.btn_click(browser)

        time.sleep(1)

        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!")


if __name__ == "__main__":
    unittest.main()
