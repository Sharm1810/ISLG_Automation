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


class Test_007_SearchByAllWords:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_searchOptions(self, setup):
        self.logger.info("****TestCase 007 - Search By All Words***")
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
        time.sleep(3)
        allwords = self.driver.find_element_by_id("rb-all-words").click()

        print(booleanoption)
        self.assertTrue(booleanoption, "By Default Boolean is selected")
        self.logger.info("By Default Boolean is selected")
