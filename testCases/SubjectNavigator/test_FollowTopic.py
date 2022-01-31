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


class Test_0010_FollowTopic:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_FollowTopic(self, setup):
        self.logger.info("****TestCase 10 - Follow Topic***")
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
        self.driver.find_element(By.XPATH, "//*[contains(@title,'Actions')]").click()
        followtopic = self.driver.find_element_by_xpath("//*[contains(@title, 'Follow Topic')]")
        self.driver.execute_script("arguments[0].click();", followtopic)
        time.sleep(2)
        message = self.driver.find_element(By.XPATH, "//*[contains(text(), 'You have followed this topic.')]").get_attribute(
            'textContent')
        print(message)
        self.logger.info(message + " is displayed when Followed Topic option is clicked")
        self.driver.find_element(By.XPATH, "//*[contains(@title,'Actions')]").click()
        self.driver.find_element(By.XPATH, "//*[contains(@title,'Actions')]").click()
        time.sleep(2)
        followtopicstate = self.driver.find_element_by_xpath("//*[contains(@title, 'Follow Topic')]")
        elementdisabled = followtopicstate.get_property('disabled')
        print(elementdisabled)
        self.logger.info(elementdisabled)
        self.logger.info("follow topic is disabled")
        self.driver.quit()


