from selenium.webdriver.common.by import By
import time

link = "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_should_see_add_to_basket_button(browser):
    browser.get(link)
    button = len(browser.find_elements(By.CSS_SELECTOR, "#add_to_basket_form > button"))
    assert button > 0, 'add to basket button not found'