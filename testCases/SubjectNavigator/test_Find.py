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
from selenium.webdriver import ActionChains
import string
import pyperclip

import random


class Test_002_Find:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_Find(self, setup):
        self.logger.info("****TestCase 002 - Verify Subject Navigator menu***")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("*****Login Successful****")
        self.logger.info("**** Subject Navigator testing *****")

        self.navigator = SubjectNavigator(self.driver)
        self.navigator.clickOnSubjectNavigatormenu()
        self.navigator.clickOnClientListing()
        self.logger.info("Subject Navigator menu is available")
        self.driver.find_element_by_xpath("//*[@id='search-subject']").click()
        text = self.driver.find_element_by_xpath("//*[@id='search-subject']")
        # entering Abuse of Right as search value
        text.send_keys("Abuse of Right")
        self.navigator.findText()
        time.sleep(3)
        textval = self.driver.find_element_by_css_selector("#search-popover > div > p > strong > span").get_attribute(
            'textContent')
        print(textval)  # This will print the no of matches found
        self.logger.info(textval + " Matches Found")
        time.sleep(3)
        text.clear()
        text.send_keys("ahj")
        self.navigator.findText()
        time.sleep(3)
        matchesnotfound = self.driver.find_element_by_css_selector("div[class='grid search-subject-no-results'] strong").get_attribute(
            'textContent')
        print(matchesnotfound)  # This will print matches not found
        self.logger.info(textval + "  Matches Found")
        time.sleep(2)
        closepop = self.driver.find_element_by_xpath("//*[@id='search-popover']/a")
        self.driver.execute_script("arguments[0].click();", closepop)
        self.logger.info("****Search Completed***")
        # Validate reset button
        self.driver.find_element_by_xpath("//*[@id='search-reset']").click()
        self.driver.quit()
