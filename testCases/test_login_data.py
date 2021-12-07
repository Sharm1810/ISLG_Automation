import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import ExcelUtils
import time


class Test_002_login_data:  # This is a test case to login to the application
    baseUrl = ReadConfig.getApplicationURL()

    path = ".//TestData/login.xlsx"
    logger = LogGen.loggen()

    def test_login_data(self, setup):
        self.logger.info("***Test_002_login_data***")
        self.logger.info("******Verifying Login****")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)

        self.rows = ExcelUtils.getRowCount(self.path, 'Sheet1')
        print("Rowcount is ", self.rows)
        lst_status = []

        for r in range(2, self.rows + 1):
            self.user = ExcelUtils.readData(self.path, 'Sheet1', r, 1)
            self.password = ExcelUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = ExcelUtils.readData(self.path, 'Sheet1', r, 3)

            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)
            act_title = self.driver.title
            exp_title = "Investor-State LawGuide"

            if act_title == exp_title:
                if self.exp == "Pass":
                    self.logger.info("***test passed**")
                    self.lp.clickLogout()
                    lst_status.append("Pass")
                elif self.exp == "Fail":
                    self.logger.info("***test failed**")
                    lst_status.append("Pass")
            elif act_title != exp_title:
                if self.exp == "Pass":
                    self.logger.info("***test failed**")
                    lst_status.append("Pass")
                elif self.exp == "Fail":
                    self.logger.info("***test passed**")
                    lst_status.append("Pass")

        if "Fail" not in lst_status:
            self.logger.info("Login passed")
            self.driver.close()
            assert True
        else:
            self.logger.info("Login Failed")
            self.driver.close()
            assert False

        self.logger.info("Test Passed")


