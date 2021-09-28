import funcs_all

link = "http://suninjuly.github.io/find_xpath_form"

try:
    funcs_all.open_wd(link)

    funcs_all.btn_click()

finally:
    funcs_all.final_step()
