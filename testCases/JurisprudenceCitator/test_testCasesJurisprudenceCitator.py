import sys
from telnetlib import EC

import clipboard
import pytest
import time
import json

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select

from pageObjects.LoginPage import LoginPage
from pageObjects.SubjectNavigator import SubjectNavigator
from pageObjects.JusrisprudenceCitator import JursiprudenceCitator
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from bs4 import BeautifulSoup
import requests
import string
import pyperclip
import pandas as pd
import random

@pytest.mark.usefixtures("setup")
class Test_testCasesJurisprudence:
    logger = LogGen.loggen()

    @pytest.mark.skip(reason="Takes longer to retrieve records")
    def test_addtoResearch(self):
        self.logger.info("****TestCase JC-001 - Verify Add to Research***")
        self.logger.info("*****Login Successful****")
        self.logger.info("**** Jurisprudence Citator testing *****")
        self.navigator = JursiprudenceCitator(self.driver)
        self.navigator.clickOnJurisprudenceMenu()
        self.logger.info("Clicked on Jurisprudence Citator from the navigation menu")
        self.navigator.clickOnClientListing()
