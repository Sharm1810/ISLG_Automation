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


class Test_009_UseAsFullTextSearch:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_UseAsFullTextSearch(self, setup):
        self.logger.info("****TestCase 009 - Use As Full Text Search***")
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
        self.navigator.clickOnBranchA()
        parent_handle = self.driver.current_window_handle
        print(parent_handle)
        self.driver.find_element(By.XPATH, "//*[contains(@title,'Actions')]").click()
        self.driver.find_element(By.XPATH, "//*[contains(@ title, 'Use as Full Text Search Filfter')]").click()
        all_handles = self.driver.window_handles
        print(all_handles)
        for handle in all_handles:
            if handle != parent_handle:
                self.driver.switch_to.window(handle)
                time.sleep(2)
                element = self.driver.find_element(By.XPATH, "//span[@title='Search Subject']")
                self.driver.execute_script("arguments[0].scrollIntoView();", element)
                time.sleep(2)
                getelementtext = self.driver.find_element(By.XPATH, "//span[@title='Search Subject']//ul").text
                print(getelementtext)
                self.logger.info(getelementtext + "  Full Text is present ")
                self.driver.close()
        self.driver.quit()
