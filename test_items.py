import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_button_add_basket(browser):
    browser.get(link)
    time.sleep(2)
    button = browser.find_elements_by_css_selector('button.btn')
    assert button, "Кнопка не найдена"
