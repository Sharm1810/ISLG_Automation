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


class Test_004_Switchlayout:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_Switchlayout(self, setup):
        self.logger.info("****TestCase 004 - Switch Layout***")
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
        self.navigator.clickOnBranchA()  # Clicks on Branch A
        a = self.driver.find_element_by_xpath("//span[(text()= 'AA')]")
        self.driver.execute_script("arguments[0].click();", a)
        b = self.driver.find_element_by_xpath("//span[(text()= 'Sharmila Test test11072021')]")
        self.driver.execute_script("arguments[0].click();", b)
        card = self.driver.find_element_by_link_text("Dispute Document").text
        if card == "Dispute Document":
            assert True == True
            self.logger.info("***Dispute Document is displayed for card***")
        cardview = self.driver.find_element_by_link_text("Dispute Details").text
        if cardview == "Dispute Details":
            assert True == True
            self.logger.info("***Dispute Details is displayed for card***")
        #compact view is clicked
        self.driver.find_element_by_xpath("//*[@id='page-content']/div/div/div[4]/div[2]/div/button[2]").click()
        self.logger.info("****Compact View is clicked****")
        self.driver.quit()
        self.logger.info("done")
