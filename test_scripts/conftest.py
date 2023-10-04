import pytest
import logging
import configparser
from selenium import webdriver
from inclusive_function.configure import Config

config = configparser.RawConfigParser()
config.read("..\\pytest.ini")


def pytest_addoption(parser):

    parser.addoption("--browser", action="store", default=Config.BROWSER)


@pytest.fixture(scope="class")
def log(request):

    logging.basicConfig(filename=config.get('pytest', 'log_file'), format=config.get('pytest', 'log_file_format'),
                            datefmt=config.get('pytest', 'log_file_date_format'))
    logger = logging.getLogger()
    logger.setLevel(config.get('pytest', 'log_file_level'))

    request.cls.logger = logger
    return request.cls.logger


# fixture to launch browser via command prompt

@pytest.fixture(scope="class")
def get_browser(request):
    browser = request.config.getoption("--browser")
    return browser


@pytest.fixture(scope="class")
def launch_browser(request, get_browser, log):

    if get_browser.lower() == "chrome" :
        log.info("launching chrome browser")
        opt = webdriver.ChromeOptions()
        opt.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=opt)

    elif get_browser.lower() == "edge":
        log.info("launching  edge browser")
        opt = webdriver.EdgeOptions()
        opt.add_experimental_option("detach", True)
        driver = webdriver.Edge(options=opt)

    else:
        raise Exception

    driver.maximize_window()
    driver.get(Config.URL)
    driver.implicitly_wait(30)

    request.cls.driver = driver

    yield request.cls.driver

    driver.quit()






































# parser.addoption("--f", action="store", default="../configration/config.json")

# # launch browser via json file
# @pytest.fixture()
# def get_json_file(request):
#     file_name = request.config.getoption("--f")
#     return file_name
#
#
# @pytest.fixture()
# def launch_browser_json(get_json_file):
#
#     file = open(get_json_file)
#     data = json.load(file)
#
#     browser = data["browser"]
#
#     if browser == "chrome":
#         credentials = webdriver.ChromeOptions()
#         credentials.browser_version = data["version"]
#         credentials.platform_name = data["platform"]
#         driver = webdriver.Chrome(options=credentials)
#
#     elif browser == "edge":
#         credentials = webdriver.EdgeOptions()
#         credentials.browser_version = data["version"]
#         credentials.platform_name = data["platform"]
#         driver = webdriver.Chrome(options=credentials)
#
#     driver.get("https://www.sony.co.in")
#     driver.maximize_window(Config.URL)
#     driver.implicitly_wait(20)
#
#     request.cls.driver = driver
#
#     yield request.cls.driver





