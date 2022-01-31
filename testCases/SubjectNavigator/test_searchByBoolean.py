from telnetlib import EC

import pytest
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.LoginPage import LoginPage
from pageObjects.SubjectNavigator import SubjectNavigator
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from selenium.webdriver.common.keys import Keys
from ddt import ddt, data, unpack
from selenium.webdriver import ActionChains
import string
import pyperclip

import random


@ddt


class Test_006_SearchByBoolean:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    # @data("Canada And Country")
    # @unpack
    def test_searchByBoolean(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("*****Login Successful****")
        self.navigator = SubjectNavigator(self.driver)
        self.navigator.clickOnSubjectNavigatormenu()
        self.navigator.clickOnClientListing()

        self.logger.info("****TestCase 006 - Verify search by boolean***")
        self.logger.info("Subject Navigator menu is available")
        self.driver.find_element_by_xpath("//*[@id='search-subject']").click()
        text = self.driver.find_element_by_xpath("//*[@id='search-subject']")
        # entering Canada And Country as search value
        text.send_keys("Canada And Country")
        self.navigator.findText()
        time.sleep(2)
        textval = self.driver.find_element_by_css_selector("#search-subject").get_attribute(
            'textContent')
        print(textval)  # This will print the no of matches found
        self.logger.info(textval + " Matches Found")
        time.sleep(2)
        text.clear()
        text.send_keys("(Abuse or Rights) AND (abuse w/5 rights)")
        self.navigator.findText()
        time.sleep(2)
        textval2 = self.driver.find_element_by_css_selector("#search-subject").get_attribute(
            'textContent')
        print(textval2)  # This will print the no of matches found
        self.logger.info(textval2 + "  Matches Found")
        text.clear()
        # fuzzysearch
        text.send_keys("countr%ies")
        self.navigator.findText()
        time.sleep(2)
        textval4 = self.driver.find_element_by_css_selector("#search-subject").get_attribute(
            'textContent')
        print(textval4)  # This will print the no of matches found
        self.logger.info(textval4 + "  Matches Found")
        closepop = self.driver.find_element_by_xpath("//*[@id='search-popover']/a")
        self.driver.execute_script("arguments[0].click();", closepop)
        self.logger.info("****Search Completed***")
        # Validate reset button
        self.driver.find_element_by_xpath("//*[@id='search-reset']").click()
        self.driver.quit()
