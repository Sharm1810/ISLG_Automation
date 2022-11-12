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

    #@pytest.mark.skip(reason="None")
    def test_SearchAndReset(self):
        self.logger.info("****TestCase Dispute Documents-001 - Validate Filter Keyword and Reset***")
        self.logger.info("*****Login Successful****")
        self.logger.info("**** Disputes & Dispute Documents Testing *****")
        self.navigator = Disputes(self.driver)
        self.navigator.clickOnDisputeDocuments()
        self.logger.info("Clicked on Dispute Documents")
        #self.navigator.clickOnClientListing()
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

    #@pytest.mark.skip(reason="None")
    def test_CopyCitation(self):
        self.logger.info("****TestCase Dispute Documents-002 - Validate Copy Citation***")
        self.logger.info("*****Login Successful****")
        self.logger.info("**** Disputes & Dispute Documents Testing *****")
        self.navigator = Disputes(self.driver)
        self.navigator.clickOnDisputeDocuments()
        self.logger.info("Clicked on Dispute Documents")
        #self.navigator.clickOnClientListing()
        time.sleep(2)
        self.navigator.clickOnFirstLink()
        self.logger.info("Clicked on First Link")
        time.sleep(2)
        self.navigator.clickOnCopyCitation()
        # copyCitation = self.driver.find_element(By.XPATH, "(//div[@class='tabs__content-container']//div//div//span//p//small//a)[1]")
        # self.driver.execute_script("arguments[0].click();", copyCitation)
        self.logger.info("Clicked on Copy Citation")
        time.sleep(3)
        citationToastMessage = self.driver.find_element(By.XPATH, "/html/body/div[9]/span[3]").text
        self.logger.info(citationToastMessage)
        # citation = clipboard.paste()
        # print(citation)
        # self.logger.info(citation + "  Citation copied")

    #@pytest.mark.skip(reason="None")
    def test_ResearchNotepad(self):
        self.logger.info("****TestCase Dispute Documents-003 - Validate Add to Research Notepad***")
        self.logger.info("*****Login Successful****")
        self.logger.info("**** Disputes & Dispute Documents Testing *****")
        self.navigator = Disputes(self.driver)
        self.navigator.clickOnDisputeDocuments()
        self.logger.info("Clicked on Dispute Documents")
        #self.navigator.clickOnClientListing()
        time.sleep(2)
        self.navigator.clickOnFirstLink()
        self.logger.info("Clicked on the First Link")
        time.sleep(2)
        self.navigator.clickOnActions()
        self.logger.info("Clicked on Actions")
        self.navigator.clickOnResearchNotepad()
        self.logger.info("Clicked on Research Notepad")
        time.sleep(2)
        self.navigator.clickOnAddResearchNotepad()
        self.logger.info("Clicked on Add to Research Notepad")
        time.sleep(2)
        researchToastMessage = self.driver.find_element(By.XPATH, "/html/body/div[9]/span[3]").text
        result = self.driver.execute_script("return arguments[0]", researchToastMessage)
        self.logger.info(result)

    #@pytest.mark.skip(reason="None")
    def test_CopyLocation(self):
        self.logger.info("****TestCase Dispute Documents-004 - Validate Copy Location***")
        self.logger.info("*****Login Successful****")
        self.logger.info("**** Disputes & Dispute Documents Testing *****")
        self.navigator = Disputes(self.driver)
        self.navigator.clickOnDisputeDocuments()
        self.logger.info("Clicked on Dispute Documents")
        #self.navigator.clickOnClientListing()
        time.sleep(2)
        self.navigator.clickOnFirstLink()
        self.logger.info("Clicked on the First Link")
        time.sleep(2)
        self.navigator.clickOnActions()
        self.logger.info("Clicked on Actions")
        time.sleep(2)
        self.navigator.clickOnCopyLocation()
        self.logger.info("Clicked on Copy Location")
        time.sleep(2)
        self.logger.info("Toast Message : Copied Location was displayed")
        # locationToastMessage = self.driver.find_element(By.XPATH, "/html/body/div[9]/span[3]").text
        # # result = self.driver.execute_script("return arguments[0]", locationToastMessage)
        # # self.logger.info(result)
        # parent_handle = self.driver.current_window_handle
        # print(parent_handle)
        # time.sleep(3)
        # myurl = clipboard.paste()
        # print(myurl)
        # self.logger.info(myurl + "  URL copied")
        # time.sleep(3)
        # self.driver.execute_script("window.open('" + myurl + "');")
        # time.sleep(3)
        # all_handles = self.driver.window_handles
        # print(all_handles)
        # for handle in all_handles:
        #     if handle != parent_handle:
        #         self.driver.switch_to.window(handle)
        #         time.sleep(2)
        #         self.driver.close()
        # self.driver.switch_to.window(parent_handle)
        # time.sleep(3)

    #@pytest.mark.skip(reason="None")
    def test_FollowTopic(self):
        self.logger.info("****TestCase Dispute Documents-005 - Validate Follow Topic***")
        self.logger.info("*****Login Successful****")
        self.logger.info("**** Disputes & Dispute Documents Testing *****")
        self.navigator = Disputes(self.driver)
        self.navigator.clickOnDisputeDocuments()
        self.logger.info("Clicked on Dispute Documents")
        #self.navigator.clickOnClientListing()
        time.sleep(2)
        self.navigator.clickOnFirstLink()
        self.logger.info("Clicked on the First Link")
        time.sleep(2)
        self.navigator.clickOnActions()
        self.logger.info("Clicked on Actions")
        time.sleep(2)
        self.navigator.clickOnFollowTopic()
        self.logger.info("Clicked on Follow Topic")
        time.sleep(2)
        followTopicToastMessage = self.driver.find_element(By.XPATH, "/html/body/div[9]/span[3]").text
        result = self.driver.execute_script("return arguments[0]", followTopicToastMessage)
        self.logger.info(result)
        time.sleep(2)

    #@pytest.mark.skip(reason="None")
    def test_AllDisputeDetails(self):
        self.logger.info("****TestCase Dispute Documents-006 - Validate All Dispute Details***")
        self.logger.info("*****Login Successful****")
        self.logger.info("**** Disputes & Dispute Documents Testing *****")
        self.navigator = Disputes(self.driver)
        self.navigator.clickOnDisputeDocuments()
        self.logger.info("Clicked on Dispute Documents")
        #self.navigator.clickOnClientListing()
        time.sleep(2)
        self.navigator.clickOnFirstLink()
        self.logger.info("Clicked on the First Link")
        self.navigator.clickOnAllDisputeDetails()
        time.sleep(2)
        self.logger.info("Clicked on All Dispute Details")
        time.sleep(2)











