import pytest
import allure
import datetime

from selenium import webdriver

from log import setup_logging

DRIVERS = "C:/Users/Licard/Desktop/Develop/Drivers"


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--url", action="store", default="http://192.168.1.74:8081")
    parser.addoption("--executor", action="store", default="192.168.1.74")
    parser.addoption("--log_level", action="store", default="INFO")
    parser.addoption("--videos", default=False)
    parser.addoption("--vnc", default=True)
    parser.addoption("--logs", default=True)


@pytest.fixture
def driver(request):
    browser_name = request.config.getoption("--browser")
    url = request.config.getoption("--url")
    executor = request.config.getoption("--executor")
    vnc = request.config.getoption("--vnc")
    logs = request.config.getoption("--logs")
    videos = request.config.getoption("--videos")
    log_level = request.config.getoption("--log_level")
    test_name = request.node.name

    if executor == "local":
        if browser_name == "chrome":
            browser = webdriver.Chrome(executable_path=DRIVERS + "/chromedriver")
        elif browser_name == "firefox":
            browser = webdriver.Firefox(executable_path=DRIVERS + "/geckodriver")
        elif browser_name == "opera":
            browser = webdriver.Opera(executable_path=DRIVERS + "/operadriver")
        else:
            raise ValueError("Browser not supported!")
    else:
        executor_url = f"http://{executor}:4444/wd/hub"
        caps = {
            "browserName": browser_name,
            "name": "Tester",
            "selenoid:options": {
                "enableVNC": vnc,
                "enableVideo": videos,
                "enableLog": logs
            }
        }
        browser = webdriver.Remote(
            command_executor=executor_url,
            desired_capabilities=caps
        )

    logger = setup_logging(log_level, test_name)
    logger.info("===> Test {} started at {}".format(test_name, datetime.datetime.now()))

    browser.test_name = test_name
    browser.log_level = log_level
    browser.maximize_window()
    browser.logger = logger
    browser.get(url)
    browser.url = url
    logger.info("Browser: {}".format(browser.capabilities))

    def fin():
        browser.quit()
        logger.info("===> Test {} finished at {}".format(test_name, datetime.datetime.now()))

    request.addfinalizer(fin)

    return browser


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    try:
        if rep.when == 'call' and rep.failed:
            if 'browser' in item.fixturenames:
                web_driver = item.funcargs['browser']
            else:
                print('Fail to take screen-shot')
                return
            allure.attach(
                web_driver.get_screenshot_as_png(),
                name='screenshot',
                attachment_type=allure.attachment_type.PNG
            )
    except Exception as e:
        print('Fail to take screen-shot: {}'.format(e))
