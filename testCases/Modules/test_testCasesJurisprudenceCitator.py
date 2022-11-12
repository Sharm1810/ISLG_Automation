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
from pageObjects.SubjectNavigator import SubjectNavigator
from pageObjects.JurisprudenceCitator import JurisprudenceCitator
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


@pytest.mark.usefixtures("setup")
class Test_JurisprudenceCitator:
    logger = LogGen.loggen()

    #@pytest.mark.skip(reason="None")
    def test_expandJurisprudence(self):
        self.logger.info("****TestCase JC-001 - Expand and Collapse Jurisprudence***")
        self.logger.info("*****Login Successful****")
        self.logger.info("**** Jurisprudence Citator testing *****")
        self.navigator = JurisprudenceCitator(self.driver)
        self.navigator.clickOnJurisprudenceMenu()
        time.sleep(2)
        #self.navigator.clickOnClientListing()
        self.logger.info("Jurisprudence menu is available")
        time.sleep(2)
        heading = self.navigator.getHeading()
        print(heading)
        self.logger.info(heading)
        self.navigator.clickOnFirstJurisprudence()
        self.logger.info("Expanded Jurisprudence")
        self.navigator.clickOnCollapse()
        self.logger.info("Collapsed Jurisprudence")

    #@pytest.mark.skip(reason="None")
    def test_copyCitation(self):
        self.logger.info("***TestCase JC-002 - Copy Citation***")
        self.navigator = JurisprudenceCitator(self.driver)
        self.navigator.clickOnJurisprudenceMenu()
        time.sleep(2)
        #self.navigator.clickOnClientListing()
        self.navigator.clickOnFirstJurisprudence()
        self.logger.info("Expanded Jurisprudence")
        self.navigator.clickOnInnerDropdown()
        time.sleep(2)
        self.navigator.clickOnCopyCitation()
        time.sleep(2)
        copyCitationToastMessage = self.driver.find_element(By.XPATH, "/html/body/div[7]/span[3]").text
        result = self.driver.execute_script("return arguments[0]", copyCitationToastMessage)
        self.logger.info(result)
        # # paste the copied citation to notepad
        # # open the file for write operation
        # f = open('citationJC.txt', 'w')
        # citationcopied = clipboard.paste()
        # self.logger.info(citationcopied + "  copied citation")
        # f.write(citationcopied)
        # # close the file
        # f.close()
        # # open the file for read
        # f = open('citationJC.txt', 'r')
        # # print the contents in console
        # print(f.read())
        # # close the file
        # f.close()

    #@pytest.mark.skip(reason="None")
    def test_addToResearchNotepad(self):
        self.logger.info("***TestCase JC-003 - Add To Research Notepad***")
        self.navigator = JurisprudenceCitator(self.driver)
        self.navigator.clickOnJurisprudenceMenu()
        time.sleep(2)
        #self.navigator.clickOnClientListing()
        self.navigator.clickOnFirstJurisprudence()
        self.logger.info("Expanded Jurisprudence")
        self.navigator.clickOnInnerDropdown()
        time.sleep(2)
        self.navigator.clickOnActions()
        self.logger.info("Clicked on Actions")
        time.sleep(2)
        self.navigator.clickOnAddToResearch()
        self.logger.info("Clicked on Research Notepad")
        time.sleep(2)
        self.navigator.clickOnResearchOption()
        self.logger.info("Selected the first research topic option")
        time.sleep(2)
        self.navigator.enterResearchComments()
        self.logger.info("Comments entered successfully")
        time.sleep(2)
        self.navigator.clickOnAddResearch()
        self.logger.info("Added to Research Topic")
        time.sleep(2)
        self.navigator.clickOnResearchEntireDocument()
        self.logger.info("Selected Entire Document option")
        time.sleep(2)
        self.navigator.clickOnResearchAddSecond()
        self.logger.info("Clicked on Add Research")
        time.sleep(2)
        researchToastMessage = self.driver.find_element(By.XPATH, "/html/body/div[7]/span[3]").text
        result = self.driver.execute_script("return arguments[0]", researchToastMessage)
        self.logger.info(result)

    #@pytest.mark.skip(reason="None")
    def test_documentComparison(self):
        self.logger.info("***TestCase JC-004 - Document Comparison***")
        self.navigator = JurisprudenceCitator(self.driver)
        self.navigator.clickOnJurisprudenceMenu()
        time.sleep(2)
        #self.navigator.clickOnClientListing()
        self.navigator.clickOnFirstJurisprudence()
        self.logger.info("Expanded Jurisprudence")
        self.navigator.clickOnInnerDropdown()
        time.sleep(2)
        self.navigator.clickOnActions()
        self.logger.info("Clicked on Actions")
        time.sleep(2)
        self.navigator.clickOnDocumentComparison()
        self.logger.info("Clicked on Document Comparison")
        time.sleep(2)
        self.navigator.clickOnDocumentComparisonGroup()
        self.logger.info("Clicked on Document Comparison Group")
        self.navigator.clickOnAddDocumentComparisonGroup()
        self.logger.info("Clicked on Add Comparison Group")
        time.sleep(2)
        comparisonToastMessage = self.driver.find_element(By.XPATH, "/html/body/div[7]/span[3]").text
        message = self.driver.execute_script("return arguments[0]", comparisonToastMessage)
        self.logger.info(message)

    #@pytest.mark.skip(reason="None")
    def test_followTopic(self):
        self.logger.info("***TestCase JC-005 - Follow Topic***")
        self.navigator = JurisprudenceCitator(self.driver)
        self.navigator.clickOnJurisprudenceMenu()
        time.sleep(2)
        #self.navigator.clickOnClientListing()
        self.navigator.clickOnFirstJurisprudence()
        self.logger.info("Expanded Jurisprudence")
        self.navigator.clickOnInnerDropdown()
        time.sleep(2)
        self.navigator.clickOnActions()
        self.logger.info("Clicked on Actions")
        time.sleep(2)
        self.navigator.clickOnFollowTopic()
        self.logger.info("Clicked on Follow Topic")
        time.sleep(2)
        followTopicToastMessage = self.driver.find_element(By.XPATH, "/html/body/div[7]/span[3]").text
        followMessage = self.driver.execute_script("return arguments[0]", followTopicToastMessage)
        self.logger.info(followMessage)

    #@pytest.mark.skip(reason="None")
    def test_copyLocation(self):
        self.logger.info("***TestCase JC-006 - Copy Location***")
        self.navigator = JurisprudenceCitator(self.driver)
        self.navigator.clickOnJurisprudenceMenu()
        time.sleep(2)
        #self.navigator.clickOnClientListing()
        self.navigator.clickOnFirstJurisprudence()
        self.logger.info("Expanded Jurisprudence")
        self.navigator.clickOnInnerDropdown()
        time.sleep(2)
        self.navigator.clickOnActions()
        time.sleep(2)
        self.navigator.clickOnCopyLocation()
        self.logger.info("Clicked on Copy Location")
        time.sleep(2)
        copyLocationToastMessage = self.driver.find_element(By.XPATH, "/html/body/div[7]/span[3]").text
        copyLocationMessage = self.driver.execute_script("return arguments[0]", copyLocationToastMessage)
        self.logger.info(copyLocationMessage)
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
    def test_allDisputeDetails(self):
        self.logger.info("***TestCase JC-007 - Dispute Details- All Dispute Details***")
        self.navigator = JurisprudenceCitator(self.driver)
        self.navigator.clickOnJurisprudenceMenu()
        time.sleep(2)
        #self.navigator.clickOnClientListing()
        self.navigator.clickOnFirstJurisprudence()
        self.logger.info("Expanded Jurisprudence")
        self.navigator.clickOnInnerDropdown()
        time.sleep(2)
        self.navigator.clickOnDisputeDetailsTab()
        self.logger.info("Clicked on Dispute Details Tab")
        time.sleep(2)
        self.navigator.clickOnAllDisputeDetails()
        self.logger.info("Clicked on All Dispute Details Button")
        parent_handle = self.driver.current_window_handle
        print(parent_handle)
        time.sleep(2)
        all_handles = self.driver.window_handles
        print(all_handles)
        for handle in all_handles:
            if handle != parent_handle:
                self.driver.switch_to.window(handle)
                time.sleep(2)
                getTextDetails = self.driver.find_element(By.XPATH,
                                                          "//*[@id='page-content']/div/div[1]/p/span[2]/strong").text
                self.logger.info(getTextDetails)
                self.driver.close()
        self.driver.switch_to.window(parent_handle)
        time.sleep(2)

    #@pytest.mark.skip(reason="None")
    def test_allDocumentsFromDispute(self):
        self.logger.info("***TestCase JC-008 -Dispute Details - All Documents From Dispute***")
        self.navigator = JurisprudenceCitator(self.driver)
        self.navigator.clickOnJurisprudenceMenu()
        time.sleep(2)
        #self.navigator.clickOnClientListing()
        self.navigator.clickOnFirstJurisprudence()
        self.logger.info("Expanded Jurisprudence")
        self.navigator.clickOnInnerDropdown()
        time.sleep(2)
        self.navigator.clickOnDisputeDetailsTab()
        self.logger.info("Clicked on Dispute Details Tab")
        time.sleep(2)
        self.navigator.clickOnAllDocumentsFromDispute()
        self.logger.info("Clicked on All Documents from Dispute")
        parent_handle = self.driver.current_window_handle
        print(parent_handle)
        time.sleep(2)
        all_handles = self.driver.window_handles
        print(all_handles)
        for handle in all_handles:
            if handle != parent_handle:
                self.driver.switch_to.window(handle)
                time.sleep(2)
                heading = self.driver.find_element(By.XPATH, "//*[@id='page-content']/div/div[1]/div/div[1]/h1").text
                self.logger.info(heading)
                citatorExpandedText = self.driver.find_element(By.XPATH,
                                                               "//div[@class='card__header card__header--no-border card__header--is-open']//a").text
                self.logger.info(citatorExpandedText)
                self.driver.close()
        self.driver.switch_to.window(parent_handle)

    #@pytest.mark.skip(reason="None")
    def test_expandProceedingDetails(self):
        self.logger.info("***TestCase JC-009 -Dispute Details - Expand/Collapse Proceeding Details***")
        self.navigator = JurisprudenceCitator(self.driver)
        self.navigator.clickOnJurisprudenceMenu()
        time.sleep(2)
        #self.navigator.clickOnClientListing()
        self.navigator.clickOnFirstJurisprudence()
        self.logger.info("Expanded Jurisprudence")
        self.navigator.clickOnInnerDropdown()
        time.sleep(2)
        self.navigator.clickOnDisputeDetailsTab()
        self.logger.info("Clicked on Dispute Details Tab")
        time.sleep(2)
        expandText = self.driver.find_element(By.XPATH, "(//div[@class='dropdown']//button//span)[1]").text
        self.logger.info(expandText + "Expand Proceeding Deatils dropdown is displayed as default")
        time.sleep(2)
        self.navigator.clickOnExpandProceedingDetails()
        self.logger.info("Clicked on Expand Proceeding Details Dropdown")
        time.sleep(2)
        self.navigator.clickOnExpandProceedingDetailsTribunal()
        parent_handle = self.driver.current_window_handle
        print(parent_handle)
        time.sleep(2)
        all_handles = self.driver.window_handles
        print(all_handles)
        for handle in all_handles:
            if handle != parent_handle:
                self.driver.switch_to.window(handle)
                time.sleep(2)
                navMenuTitle = self.driver.find_element(By.XPATH, "//*[@id='page-content']/div/div/div[1]/div/nav").text
                self.logger.info(navMenuTitle)
                heading2 = self.driver.find_element(By.XPATH,
                                                    "//*[@id='page-content-1']/div[1]/div[1]/div[1]/div[2]/h2").text
                self.logger.info(heading2)
                self.driver.close()
        self.driver.switch_to.window(parent_handle)

    def test_findAndReset(self):
        self.logger.info("****TestCase AC-009 - Validate Find and Reset***")
        self.navigator = JurisprudenceCitator(self.driver)
        self.navigator.clickOnJurisprudenceMenu()
        time.sleep(2)
        #self.navigator.clickOnClientListing()
        self.logger.info("Jurisprudence Citator menu is available")
        time.sleep(2)
        myopen = open('jsonfiles\JCFind.json', 'r')
        jsondata = myopen.read()
        with open('jsonfiles\JCFind.json') as data_file:
            data = json.load(data_file)
            for v in data.values():
                searchvalue = v
                findSendData = self.driver.find_element(By.XPATH,
                                                        "//*[@id='txtJurisprudenceSearch']")
                # findSendData.clear()
                time.sleep(2)
                findSendData.send_keys(searchvalue)
                self.navigator.clickOnFind()
                found = self.driver.find_element(By.CSS_SELECTOR,
                                                 "#search-popover-juris > p:nth-child(2)").get_attribute(
                    'textContent')
                self.logger.info(found + " Matches Found")
                time.sleep(3)
                self.navigator.clickOnReset()
                self.logger.info("Clicked on Reset")
        self.driver.quit()
