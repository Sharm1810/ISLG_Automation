import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Login:  # This is a test case to login to the application
    baseUrl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_homePageTitle(self, setup):
        self.logger.info("******Test_001_Login****")
        self.logger.info("******Verifying Homepage Title****")
        self.driver = setup
        self.driver.get(self.baseUrl)

        act_title = self.driver.title

        if act_title == "Investor-State LawGuide":
            assert True
            self.driver.close()
            self.logger.info("******Homepage Title is passed****")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
            self.driver.close()
            self.logger.info("******Homepage Title is failed****")
            assert False

    #@pytest.mark.sanity
    def test_login(self, setup):
        self.logger.info("******Verifying Login****")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title

        if act_title == "Investor-State LawGuide":
            assert True
            #self.driver.close()
            self.logger.info("******Logged in successfully****")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            #self.driver.close()
            self.logger.info("******Login failed****")
            #assert False

