import pytest
import self
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
import pytest
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.LoginPage import LoginPage
from pageObjects.SubjectNavigator import SubjectNavigator
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import string
import pyperclip


@pytest.fixture(scope="class")
def setup(request):
    # if browser == 'chrome':
    options = Options()
    driver = webdriver.Chrome(executable_path="C:\\chromedriver",chrome_options=options)
    driver.get("https://app.investorstatelawguide.com")
    driver.maximize_window()
    driver.find_element(By.XPATH, "//*[@id='UserName']").send_keys("sharmishri")
    driver.find_element(By.XPATH, "//*[@id='Password']").send_keys("Messages321@")
    driver.find_element(By.XPATH, "//*[@id='loginDetail']").click()
    request.cls.driver = driver
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])




# elif browser == 'firefox':
# driver = webdriver.Firefox(executable_path="C:\\geckodriver")

# elif browser == 'edge':
# driver = webdriver.Edge(executable_path="C:\\msedgedriver")

# else:
# driver = webdriver.Chrome(executable_path="C:\\chromedriver")


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


def pytest_configure(config):
    config._metadata['Project Name'] = 'ISLG Subscriber'
    config._metadata['Application: '] = 'ISLG Subscriber'
    config._metadata['Tester Name'] = 'Sharmila'


@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
import pytest




@pytest.fixture(scope="session")
def get_driver(request, browser, platform, environment):
    df = DriverFactory(browser, platform, environment)
    driver = df.get_driver_instance()
    session = request.node
    for item in session.items:
        cls = item.getparent(pytest.Class)
        setattr(cls.obj, "driver", driver)
    yield
    driver.quit()


def pytest_addoption(parser):
    parser.addoption("--browser", help="Browser Type")
    parser.addoption("--platform", help="Operating System Type")
    parser.addoption("--environment", help="Application Environment")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def platform(request):
    return request.config.getoption("--platform")


@pytest.fixture(scope="session")
def environment(request):
    return request.config.getoption("--environment")
