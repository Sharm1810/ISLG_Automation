import sys
from telnetlib import EC

import clipboard
import ddt
import pytest
import time
import json

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select

from pageObjects.LoginPage import LoginPage
from pageObjects.TreatiesAndRules import TreatiesAndRules
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import requests
import string
import pyperclip
import pandas as pd
import random
import os.path


@pytest.mark.usefixtures("setup")
class Test_Reports:
    logger = LogGen.loggen()

    #@pytest.mark.skip(reason="None")
    def test_SearchAndReset(self):
        self.logger.info("****TestCase TreatiesAndRules-001 - Validate Search and Reset***")
        self.logger.info("*****Login Successful****")
        self.logger.info("**** Treaties And Rules testing *****")
        self.navigator = TreatiesAndRules(self.driver)
        self.navigator.clickOnTreatiesAndRules()
        self.logger.info("Treaties And Rules menu was clicked")
        time.sleep(2)
        #self.navigator.clickOnClientListing()
        time.sleep(2)
        myopen = open('jsonfiles\TPFind.json', 'r')
        jsondata = myopen.read()
        with open('jsonfiles\TPFind.json') as data_file:
            data = json.load(data_file)
            for v in data.values():
                searchvalue = v
                findSendData = self.driver.find_element(By.XPATH,
                                                        "//*[@id='txtTreatyRuleSearch']")

                # findSendData.clear()
                time.sleep(2)
                findSendData.send_keys(searchvalue)
                time.sleep(3)
                self.navigator.clickOnFind()
                found = self.driver.find_element(By.XPATH,
                                                 "//*[@id='spanMatch']")
                print(found.text)
                self.logger.info(found.text + " Matches Found")
                time.sleep(3)
                self.navigator.clickOnReset()
                self.logger.info("Clicked on Reset")

    #@pytest.mark.skip(reason="None")
    def test_FilterType(self):
        self.logger.info("****TestCase TreatiesAndRules-002 - Validate Filter Type***")
        self.logger.info("*****Login Successful****")
        self.logger.info("**** Treaties And Rules testing *****")
        self.navigator = TreatiesAndRules(self.driver)
        self.navigator.clickOnTreatiesAndRules()
        self.logger.info("Treaties And Rules menu was clicked")
        time.sleep(2)
        #self.navigator.clickOnClientListing()
        time.sleep(2)
        self.navigator.clickOnFilterType()
        self.logger.info("Clicked on Filter Type")
        arbitrationRulesFilter = self.driver.find_element(By.XPATH,
                                                          "//*[@id='filter-dropdown']/p[1]/button[1]")
        self.driver.execute_script("arguments[0].click();", arbitrationRulesFilter)
        filterArbitrationRules = self.driver.find_element(By.XPATH, "//*[@id='dvTreatiesAndRulesData']/h2[1]")
        filterArbitrationRulesText = filterArbitrationRules.text
        assert "Arbitration Rules" == filterArbitrationRulesText
        self.logger.info(filterArbitrationRulesText + " is displayed")
        matchesFound = self.driver.find_element(By.XPATH, "//*[@id='spanMatch']")
        self.logger.info(matchesFound.text)
        time.sleep(2)
        internationalTreatiesRulesFilter = self.driver.find_element(By.XPATH,
                                                                    "//*[@id='filter-dropdown']/p[1]/button[2]")
        self.driver.execute_script("arguments[0].click();", internationalTreatiesRulesFilter)
        filterInternationalTreatiesRules = self.driver.find_element(By.XPATH, "//*[@id='dvTreatiesAndRulesData']/h2[2]")
        filterInternationalTreatiesText = filterInternationalTreatiesRules.text
        assert "International Treaties & Rules" == filterInternationalTreatiesText
        self.logger.info(filterInternationalTreatiesText + " is displayed")
        matchesFound = self.driver.find_element(By.XPATH, "//*[@id='spanMatch']")
        self.logger.info(matchesFound.text)
        time.sleep(2)
        naftaFilter = self.driver.find_element(By.XPATH, "//*[@id='filter-dropdown']/p[1]/button[5]")
        self.driver.execute_script("arguments[0].click();", naftaFilter)
        filterNafta = self.driver.find_element(By.XPATH, "//*[@id='dvTreatiesAndRulesData']/h2[5]")
        naftaHeading = filterNafta.text
        assert "NAFTA" == naftaHeading
        self.logger.info(matchesFound.text)
        self.navigator.clickOnClearFilters()

    #@pytest.mark.skip(reason="None")
    def test_ResearchNotepad(self):
        self.logger.info("****TestCase TreatiesAndRules-003 - Validate Research Notepad***")
        self.logger.info("*****Login Successful****")
        self.logger.info("**** Treaties And Rules testing *****")
        self.navigator = TreatiesAndRules(self.driver)
        self.navigator.clickOnTreatiesAndRules()
        self.logger.info("Treaties And Rules menu was clicked")
        time.sleep(2)
        #self.navigator.clickOnClientListing()
        self.navigator.clickOnExpandFirstLink()
        self.logger.info("Expanded the first Arbitration Rule")
        self.navigator.clickOnActions()
        self.logger.info("Clicked on Actions")
        self.navigator.clickOnResearchNotepad()
        self.logger.info("Clicked on Research Notepad")
        self.navigator.clickOnAddResearchNotepad()
        time.sleep(2)
        researchToastMessage = self.driver.find_element(By.XPATH, "/html/body/div[7]/span[3]").text
        result = self.driver.execute_script("return arguments[0]", researchToastMessage)
        self.logger.info(result)

    #@pytest.mark.skip(reason="None")
    def test_CopyLocation(self):
        self.logger.info("****TestCase TreatiesAndRules-004 - Validate Copy Location***")
        self.logger.info("*****Login Successful****")
        self.logger.info("**** Treaties And Rules testing *****")
        self.navigator = TreatiesAndRules(self.driver)
        self.navigator.clickOnTreatiesAndRules()
        self.logger.info("Treaties And Rules menu was clicked")
        time.sleep(2)
        #self.navigator.clickOnClientListing()
        self.navigator.clickOnExpandFirstLink()
        self.logger.info("Expanded the first link")
        self.navigator.clickOnActions()
        self.logger.info("Clicked on Actions")
        self.navigator.clickOnCopyLocation()
        self.logger.info("Clicked on Copy Location")
        time.sleep(2)
        locationToastMessage = self.driver.find_element(By.XPATH, "/html/body/div[7]/span[3]").text
        result = self.driver.execute_script("return arguments[0]", locationToastMessage)
        self.logger.info(result)
        # parent_handle = self.driver.current_window_handle
        # print(parent_handle)
        # time.sleep(3)
        # myurl = clipboard.paste()
        # print(myurl)
        # self.logger.info(myurl + "  URL copied")
        # self.driver.execute_script("window.open('" + myurl + "');")
        # time.sleep(2)
        # all_handles = self.driver.window_handles
        # print(all_handles)
        # for handle in all_handles:
        #     if handle != parent_handle:
        #         self.driver.switch_to.window(handle)
        #         time.sleep(2)
        #         self.driver.close()
        # self.driver.switch_to.window(parent_handle)
        # time.sleep(2)

    #@pytest.mark.skip(reason="None")
    def test_FollowTopic(self):
        self.logger.info("****TestCase TreatiesAndRules-005 - Validate Follow Topic***")
        self.logger.info("*****Login Successful****")
        self.logger.info("**** Treaties And Rules testing *****")
        self.navigator = TreatiesAndRules(self.driver)
        self.navigator.clickOnTreatiesAndRules()
        self.logger.info("Treaties And Rules menu was clicked")
        time.sleep(2)
        #self.navigator.clickOnClientListing()
        self.navigator.clickOnExpandFirstLink()
        self.logger.info("Expanded the first link")
        time.sleep(2)
        self.navigator.clickOnActions()
        self.logger.info("Clicked on Actions")
        time.sleep(2)
        self.navigator.clickOnFollowTopic()
        time.sleep(2)
        followTopicToastMessage = self.driver.find_element(By.XPATH, "/html/body/div[7]/span[3]").text
        result = self.driver.execute_script("return arguments[0]", followTopicToastMessage)
        self.logger.info(result)

    #@pytest.mark.skip(reason="None")
    def test_CopyCitation(self):
        self.logger.info("****TestCase TreatiesAndRules-006 - Validate Copy Citation***")
        self.logger.info("*****Login Successful****")
        self.logger.info("**** Treaties And Rules testing *****")
        self.navigator = TreatiesAndRules(self.driver)
        self.navigator.clickOnTreatiesAndRules()
        self.logger.info("Treaties And Rules menu was clicked")
        time.sleep(2)
       #self.navigator.clickOnClientListing()
        self.navigator.clickOnExpandFirstLink()
        self.logger.info("Expanded the first link")
        self.navigator.clickOnCopyCitation()
        time.sleep(2)
        citationToastMessage = self.driver.find_element(By.XPATH, "/html/body/div[7]/span[3]").text
        result = self.driver.execute_script("return arguments[0]", citationToastMessage)
        self.logger.info(result)
        citation = clipboard.paste()
        print(citation)
        self.logger.info(citation + "  Citation copied")

    #@pytest.mark.skip(reason="None")
    def test_InstrumentDetailsCopyCitation(self):
        self.logger.info("****TestCase TreatiesAndRules-007 - Instrument Details -Validate Copy Citation***")
        self.logger.info("*****Login Successful****")
        self.logger.info("**** Treaties And Rules testing *****")
        self.navigator = TreatiesAndRules(self.driver)
        self.navigator.clickOnTreatiesAndRules()
        self.logger.info("Treaties And Rules menu was clicked")
        time.sleep(2)
        #self.navigator.clickOnClientListing()
        self.navigator.clickOnExpandFirstLink()
        self.logger.info("Expanded the first link")
        self.navigator.clickOnInstrumentDetails()
        self.logger.info("Clicked on Instrument Details Tab")
        self.navigator.clickOnCopyCitation()
        self.logger.info("Clicked on Copy Citation")
        time.sleep(2)
        citationToastMessage = self.driver.find_element(By.XPATH, "/html/body/div[7]/span[3]").text
        result = self.driver.execute_script("return arguments[0]", citationToastMessage)
        self.logger.info(result)
        # citation = clipboard.paste()
        # print(citation)
        # self.logger.info(citation + "  Citation copied")

    #@pytest.mark.skip(reason="None")
    def test_DocumentComparison(self):
        self.logger.info("****TestCase TreatiesAndRules-008 - Validate Add To Document Comparison***")
        self.logger.info("*****Login Successful****")
        self.logger.info("**** Treaties And Rules testing *****")
        self.navigator = TreatiesAndRules(self.driver)
        self.navigator.clickOnTreatiesAndRules()
        self.logger.info("Treaties And Rules menu was clicked")
        time.sleep(2)
        #self.navigator.clickOnClientListing()
        self.navigator.clickOnExpandThirdLink()
        self.logger.info("Clicked on the Third Link")
        self.navigator.clickOnActions()
        self.logger.info("Clicked on Actions")
        self.navigator.clickOnDocumentComparison()
        self.logger.info("Clicked on Document Comparison")
        time.sleep(2)
        documentToastMessage = self.driver.find_element(By.XPATH, "/html/body/div[7]/span[3]").text
        result = self.driver.execute_script("return arguments[0]", documentToastMessage)
        self.logger.info(result)
        self.driver.quit()











