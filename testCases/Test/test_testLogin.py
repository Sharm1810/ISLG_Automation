import pytest
import self
from selenium import webdriver

from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
import pytest
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.LoginPage import LoginPage
from pageObjects.SubjectNavigator import SubjectNavigator
from utilities.readProperties import ReadConfig
#from utilities.customLogger import Logger
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import string
import pyperclip



def test_login():
    # if browser == 'chrome':
    driver = webdriver.Chrome(executable_path="C:\\chromedriver")
    driver.get("https://staging.investorstatelawguide.com")
    driver.maximize_window()
    driver.find_element(By.XPATH, "//*[@id='UserName']").send_keys("sharmishri")
    driver.find_element(By.XPATH, "//*[@id='Password']").send_keys("Messages321@")
    driver.find_element(By.XPATH, "//*[@id='loginDetail']").click()



