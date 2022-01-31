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


class Test_008_SearchByAnyWords:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_searchByAnyWords(self, setup):
        self.logger.info("****TestCase 008 - Search By Any Words***")
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
        # this expands the advanced find
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@id='btn-search-options-control']/i").click()
        self.logger.info("Clicked on the expand search")
        anywords = self.driver.find_element_by_xpath("//input[@id='rb-any-words']")
        self.driver.execute_script("arguments[0].click();", anywords)
        self.driver.find_element_by_xpath("//*[@id='btn-search-options-control']/i").click()
        text = self.driver.find_element_by_xpath("//*[@id='search-subject']")
        # entering Canada And Country as search value
        text.send_keys(" 'Abuse of right'  award")

        self.navigator.findText()
        time.sleep(2)
        textval = self.driver.find_element_by_xpath("//span[@class='no-of-search-subject']").get_attribute(
            'textContent')
        print(textval)  # This will print the no of matches found
        self.logger.info("Search Entry - 'Abuse of Right' ")
        self.logger.info(textval + " No of Matches found")
        time.sleep(1)
        text.clear()
        text.send_keys(" 'Clean hands' doctrine")
        self.navigator.findText()
        time.sleep(2)
        textval1 = self.driver.find_element_by_xpath("//span[@class='no-of-search-subject']").get_attribute(
            'textContent')
        print(textval1)  # This will print the no of matches found
        self.logger.info("Search Entry - 'Clean hands' doctrine ")
        self.logger.info(textval1 + " Matches Found")
        text.clear()
        text.send_keys(" '+'Clean hands' + doctrine - claimant")
        self.navigator.findText()
        time.sleep(2)
        textval2 = self.driver.find_element_by_xpath("//span[@class='no-of-search-subject']").get_attribute(
            'textContent')
        print(textval2)  # This will print the no of matches found
        self.logger.info("Search Entry - '+'Clean hands' + doctrine - claimant ")
        self.logger.info(textval2 + " Matches Found")
        self.driver.quit()
