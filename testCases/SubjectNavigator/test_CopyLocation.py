import time
import unittest
import clipboard
import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from pageObjects.LoginPage import LoginPage
from pageObjects.SubjectNavigator import SubjectNavigator
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class Test_0011_CopyLocation:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    #@pytest.mark.sanity
    def test_CopyLocation(self,setup):
        self.logger.info("****TestCase 11 - Copy Location***")
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
        self.driver.find_element_by_xpath("//*[contains(@title, 'Copy Location')]").click()
        time.sleep(2)
        parent_handle = self.driver.current_window_handle
        print(parent_handle)
        test = self.driver.find_element_by_xpath("//input[@title='Search']")

        time.sleep(2)
        all_handles = self.driver.window_handles
        print(test.send_keys(Keys.CONTROL + "v"))
        myurl = clipboard.paste()
        self.driver.execute_script("window.open('" + myurl + "');")
        time.sleep(2)
        for handle in all_handles:
            if handle != parent_handle:
                self.driver.switch_to.window(handle)
        self.driver.quit()
