import time

import self
from selenium import webdriver


class LoginPage:
    textbox_username_id = "UserName"
    textbox_password_id = "Password"
    button_id = "loginDetail"
    account_id = "menu-dropdown-1-control"
    logout_css_selector = "//*[@id='aLogout']"

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, UserName):
        self.driver.maximize_window()
        self.driver.find_element_by_id(self.textbox_username_id).clear()
        self.driver.find_element_by_id(self.textbox_username_id).send_keys(UserName)

    def setPassword(self, Password):
        self.driver.find_element_by_id(self.textbox_password_id).clear()
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(Password)

    def clickLogin(self):
        self.driver.find_element_by_id(self.button_id).click();

    def clickLogout(self):
        self.driver.find_element_by_id("menu-dropdown-1-control").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//*[@id='aLogout']").click()

