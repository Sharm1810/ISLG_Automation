import sys
from telnetlib import EC

import clipboard
import ddt
import pyautogui
import pytest
import time
import json



from tkinter import Tk
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select

from pageObjects.JurisprudenceCitator import JurisprudenceCitator
from pageObjects.LoginPage import LoginPage
from pageObjects.Disputes import Disputes
from pageObjects.FullTextSearch import FullTextSearch
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from bs4 import BeautifulSoup
import requests
import string
import pyperclip
import pandas as pd
import random

import ctypes
import ctypes.wintypes as w


def assertEqual(result, param):
    pass


@pytest.mark.usefixtures("setup")
class Test_FullTextSearch:
    logger = LogGen.loggen()

    @pytest.mark.skip(reason="None")
    def test_SearchAndReset(self):
        self.logger.info("****TestCase TreatiesAndRules-001 - Validate Search and Reset***")
        self.logger.info("*****Login Successful****")
        self.logger.info("**** Treaties And Rules testing *****")
        self.navigator = Disputes(self.driver)
        self.navigator.clickOnDisputeDocuments()
        self.logger.info("Clicked on Dispute Documents")
        self.navigator.clickOnClientListing()
        time.sleep(2)
        myopen = open('jsonfiles\TPFind.json', 'r')
        jsondata = myopen.read()
        with open('jsonfiles\TPFind.json') as data_file:
            data = json.load(data_file)
            for v in data.values():
                searchvalue = v
                findSendData = self.driver.find_element(By.XPATH,
                                                        "//*[@id='txtDDSearch']")

                # findSendData.clear()
                time.sleep(2)
                findSendData.send_keys(searchvalue)
                time.sleep(3)
                self.navigator.clickOnSearch()
                found = self.driver.find_element(By.XPATH,
                                                 "//*[@id='txtDisputeCount']")
                print(found.text)
                self.logger.info(found.text + " Matches Found")
                time.sleep(3)
                self.navigator.clickOnReset()
                self.logger.info("Clicked on Reset")

