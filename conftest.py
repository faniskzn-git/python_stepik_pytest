import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                 help="Choose browser: =chrome or =firefox")
    parser.addoption('--language', action='store', default='ru',
                     help="Choose language: =ru, =en, =etc")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        chrome_options.add_experimental_option("excludeSwitches", ['enable-logging'])
        chrome_options.add_argument("--log-level=3")
        chrome_options.add_argument("start-maximized")
        browser = webdriver.Chrome(options=chrome_options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(options=firefox_options)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()