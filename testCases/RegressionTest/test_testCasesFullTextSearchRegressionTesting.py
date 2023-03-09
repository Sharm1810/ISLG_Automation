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
from pageObjects.SubjectNavigator import SubjectNavigator
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
    def test_FullCaseAnalysis(self):
            self.logger.info("****TestCase Full Text Search-001 - Validate Full Case Analysis***")
            self.logger.info("*****Login Successful****")
            self.logger.info("**** Full Text Search testing *****")
            self.navigator = FullTextSearch(self.driver)
            self.navigator.clickOnFullTextSearchMenu()
            self.logger.info("Full Text Search menu was clicked")
            time.sleep(2)
            #self.navigator.clickOnClientListing()
            self.navigator.clickOnSearchFT()
            self.logger.info("Clicked on Search")
            time.sleep(2)
            self.navigator.clickOnFullCaseAnalysis()
            time.sleep(2)
            self.logger.info("Clicked on Full Case Analysis")
            parent_handle = self.driver.current_window_handle
            print(parent_handle)
            time.sleep(2)
            all_handles = self.driver.window_handles
            print(all_handles)
            for handle in all_handles:
                if handle != parent_handle:
                    self.driver.switch_to.window(handle)
                    time.sleep(2)
                    self.driver.close()
                    time.sleep(2)
            self.driver.switch_to.window(parent_handle)
            time.sleep(2)

    #@pytest.mark.skip(reason="None")
    def test_copyCitation(self):
            self.logger.info("****TestCase Full Text Search-002 - Validate Copy Citation***")
            self.logger.info("*****Login Successful****")
            self.logger.info("**** Full Text Search testing *****")
            self.navigator = FullTextSearch(self.driver)
            self.navigator.clickOnFullTextSearchMenu()
            self.logger.info("Full Text Search menu was clicked")
            time.sleep(2)
            #self.navigator.clickOnClientListing()
            self.navigator.clickOnSearchFT()
            self.logger.info("Clicked on Search")
            time.sleep(2)
            self.navigator.clickOnFullCaseAnalysis()
            time.sleep(2)
            self.logger.info("Clicked on Full Case Analysis")
            parent_handle = self.driver.current_window_handle
            print(parent_handle)
            time.sleep(2)
            all_handles = self.driver.window_handles
            print(all_handles)
            for handle in all_handles:
                if handle != parent_handle:
                    self.driver.switch_to.window(handle)
                    time.sleep(2)
                    self.navigator.clickOnCopyCitation()
                    time.sleep(2)
                    self.logger.info("Clicked on Copy Citation")
                    self.driver.close()
                    time.sleep(2)
            self.driver.switch_to.window(parent_handle)
            time.sleep(2)

    #@pytest.mark.skip(reason="None")
    def test_downloadDocument(self):
        self.logger.info("****TestCase Full Text Search-003 - Validate Download Document***")
        self.logger.info("*****Login Successful****")
        self.logger.info("**** Full Text Search testing *****")
        self.navigator = FullTextSearch(self.driver)
        self.navigator.clickOnFullTextSearchMenu()
        self.logger.info("Full Text Search menu was clicked")
        time.sleep(2)
        # self.navigator.clickOnClientListing()
        self.navigator.clickOnSearchFT()
        self.logger.info("Clicked on Search")
        time.sleep(2)
        self.navigator.clickOnFullCaseAnalysis()
        time.sleep(2)
        self.logger.info("Clicked on Full Case Analysis")
        parent_handle = self.driver.current_window_handle
        print(parent_handle)
        time.sleep(2)
        all_handles = self.driver.window_handles
        print(all_handles)
        for handle in all_handles:
            if handle != parent_handle:
                self.driver.switch_to.window(handle)
                time.sleep(2)
                self.navigator.clickOnDownloadDocument()
                time.sleep(2)
                self.logger.info("Clicked on Download Document")
                self.driver.close()
                time.sleep(5)
        self.driver.switch_to.window(parent_handle)
        time.sleep(2)

    #@pytest.mark.skip(reason="None")
    def test_addToNotepad(self):
        self.logger.info("****TestCase Full Text Search-004 - Validate Add to Notepad***")
        self.logger.info("*****Login Successful****")
        self.logger.info("**** Full Text Search testing *****")
        self.navigator = FullTextSearch(self.driver)
        self.navigator.clickOnFullTextSearchMenu()
        self.logger.info("Full Text Search menu was clicked")
        time.sleep(2)
        # self.navigator.clickOnClientListing()
        self.navigator.clickOnSearchFT()
        self.logger.info("Clicked on Search")
        time.sleep(2)
        self.navigator.clickOnFullCaseAnalysis()
        time.sleep(2)
        self.logger.info("Clicked on Full Case Analysis")
        parent_handle = self.driver.current_window_handle
        print(parent_handle)
        time.sleep(2)
        all_handles = self.driver.window_handles
        print(all_handles)
        for handle in all_handles:
            if handle != parent_handle:
                self.driver.switch_to.window(handle)
                time.sleep(3)
                self.navigator.clickOnAddNotepad()
                self.logger.info("Full Case Analysis - Clicked on Research Notepad")
                time.sleep(3)
                self.navigator.selectResearchOption()
                self.logger.info("Selected Research Option")
                time.sleep(3)
                self.navigator.clickOnAddNotepad()
                self.logger.info("Clicked on Add to Notepad")
                time.sleep(3)
                # researchOption = self.driver.find_element(By.XPATH, "(//label[@class='form__radio']//input)[1]")
                # self.driver.execute_script("arguments[0].click();", researchOption)
                self.logger.info("Clicked on Add to Notepad")
                self.driver.close()
        self.driver.switch_to.window(parent_handle)
        time.sleep(2)

    #@pytest.mark.skip(reason="None")
    def test_doucmentDetailsCopyCitation(self):
            self.logger.info("****TestCase Full Text Search-005 - Validate Document Details - Copy Citation***")
            self.logger.info("*****Login Successful****")
            self.logger.info("**** Full Text Search testing *****")
            self.navigator = FullTextSearch(self.driver)
            self.navigator.clickOnFullTextSearchMenu()
            self.logger.info("Full Text Search menu was clicked")
            time.sleep(2)
            # self.navigator.clickOnClientListing()
            self.navigator.clickOnSearchFT()
            self.logger.info("Clicked on Search")
            time.sleep(2)
            self.navigator.clickOnFullCaseAnalysis()
            time.sleep(2)
            self.logger.info("Clicked on Full Case Analysis")
            parent_handle = self.driver.current_window_handle
            print(parent_handle)
            time.sleep(2)
            all_handles = self.driver.window_handles
            print(all_handles)
            for handle in all_handles:
                if handle != parent_handle:
                    self.driver.switch_to.window(handle)
                    time.sleep(3)
                    self.navigator.clickOnExpandDocumentDetails()
                    time.sleep(2)
                    self.logger.info("Clicked on Expand Document Deatils")
                    copyCitation = self.driver.find_element(By.XPATH, "(//div[@class='document-details-view']//div//p//small//a)[1]")
                    self.driver.execute_script("arguments[0].click();", copyCitation)
                    #self.navigator.clickOnDisputeDetailsCopyCitaion()
                    time.sleep(2)
                    self.logger.info("Clicked on Copy Citation associated with Dispute Details")
                    time.sleep(1)
                    self.driver.close()
            self.driver.switch_to.window(parent_handle)
            time.sleep(2)



