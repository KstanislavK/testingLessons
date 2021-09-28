import funcs_all

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    funcs_all.open_wd(link)

    funcs_all.btn_click()

    funcs_all.switch_to_new_window(1)

    funcs_all.calc()

    funcs_all.btn_click()
finally:
    funcs_all.final_step()
