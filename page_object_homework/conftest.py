import pytest

from selenium import webdriver

DRIVERS = "C:/Users/Licard/Desktop/Develop/Drivers"


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--url", action="store", default="http://192.168.1.74:8081")


@pytest.fixture
def driver(request):
    browser_name = request.config.getoption("--browser")
    url = request.config.getoption("--url")

    if browser_name == "chrome":
        browser = webdriver.Chrome(executable_path=DRIVERS + "/chromedriver")
    elif browser_name == "firefox":
        browser = webdriver.Firefox(executable_path=DRIVERS + "/geckodriver")
    elif browser_name == "opera":
        browser = webdriver.Opera(executable_path=DRIVERS + "/operadriver")
    else:
        raise ValueError("Browser not supported!")

    browser.maximize_window()
    request.addfinalizer(browser.close)

    browser.get(url)
    browser.url = url

    return browser
