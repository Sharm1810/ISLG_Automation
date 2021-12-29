import pytest
from selenium import webdriver


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome(executable_path="C:\\chromedriver")

    elif browser == 'firefox':
        driver = webdriver.Firefox(executable_path="C:\\geckodriver")

    elif browser == 'edge':
        driver = webdriver.Edge(executable_path="C:\\msedgedriver")

    else:
        driver = webdriver.Chrome(executable_path="C:\\chromedriver")

    return driver


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
