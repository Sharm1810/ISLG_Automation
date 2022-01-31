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


class Test_003_AddtoResearch:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_AddtoResearch(self, setup):
        self.logger.info("****TestCase 003 - Verify Add to Research***")
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
        self.navigator.clickOnBranchA()
        #Clicks on Expand All of the first row
        self.driver.find_element_by_xpath("(//div[contains(@class,'card__actions')]/a[1])[1]").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[contains(@title,'Actions')]").click()
        self.driver.find_element_by_xpath("//*[contains(@title,'Research Notepad')]").click()
        self.driver.find_element_by_css_selector("#popup-add-to-rn > div.scrolling-content > div:nth-child(3) > div > ul > li:nth-child(2) > label").click()
        comments = self.driver.find_element_by_xpath("//*[@id='bookmark-comments']")
        comments.send_keys("Adding to Research Notepad")
        self.driver.find_element_by_xpath("//*[@ id = 'btn-popup-add']").click()
        self.logger.info("Added to Research Notepad")
        self.driver.quit()
        self.logger.info("done")