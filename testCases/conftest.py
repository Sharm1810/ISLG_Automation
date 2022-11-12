import pytest
import self
from selenium import webdriver

from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
import pytest
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.LoginPage import LoginPage
from pageObjects.SubjectNavigator import SubjectNavigator
from utilities.readProperties import ReadConfig
#from utilities.customLogger import Logger
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import string
import pyperclip


@pytest.fixture(scope="class")
def setup(request):
    # if browser == 'chrome':
    driver = webdriver.Chrome(executable_path="C:\\chromedriver")
    driver.get("https://app.investorstatelawguide.com/Login/")
    driver.maximize_window()
    driver.find_element(By.XPATH, "//*[@id='UserName']").send_keys("sharmishri")
    driver.find_element(By.XPATH, "//*[@id='Password']").send_keys("Messages321@")
    driver.find_element(By.XPATH, "//*[@id='loginDetail']").click()
    request.cls.driver = driver




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
