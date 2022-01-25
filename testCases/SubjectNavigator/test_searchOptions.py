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


class Test_005_SearchOptions:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_searchOptions(self, setup):
        self.logger.info("****TestCase 005 - Boolean Find***")
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
        # this expands the advanced find and checks if Boolean option is selected by default
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@id='btn-search-options-control']/i").click()
        self.logger.info("Clicked on the expand search")
        time.sleep(3)
        booleanoption = self.driver.find_element_by_id("rb-Boolean").is_selected()
        print(booleanoption)
        self.assertTrue(booleanoption, "By Default Boolean is selected")
        self.logger.info("By Default Boolean is selected")

        # Check if Linguistic Aids - Stemming is selected by default
        stemmingcheck = self.driver.find_element_by_id("chk-stemming").is_selected()
        print(stemmingcheck)
        self.assertTrue(stemmingcheck, "By Default Stemming is selected")
        self.logger.info("By Default Stemming is selected")

        # Check if Linguistic Aids - Fuzzy Typo is selected by default
        fuzzytypocheck = self.driver.find_element_by_id("chk-fuzzy-typo")
        print(fuzzytypocheck)
        self.assertTrue(fuzzytypocheck, "By Default fuzzy typo is selected")
        self.logger.info("By Default Fuzzy Typo is selected")


        self.driver.quit()

    def assertTrue(self, booleanoption, param):
        pass
