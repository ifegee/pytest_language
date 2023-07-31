from selenium.webdriver.common.by import By

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_button(browser):
    browser.implicitly_wait(3)
    browser.get(link)
    button = browser.find_elements(By.CLASS_NAME, 'btn-add-to-basket')
    assert len(button) == 1
