import sys
from telnetlib import EC

import clipboard
import ddt
import pytest
import time
import json

import tk
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select

from pageObjects.JurisprudenceCitator import JurisprudenceCitator
from pageObjects.LoginPage import LoginPage
from pageObjects.SubjectNavigator import SubjectNavigator
from pageObjects.TermsAndPhrases import TermsAndPhrases
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
class Test_TermsAndPhrases:
    logger = LogGen.loggen()

    #@pytest.mark.skip(reason="None")
    def test_expandBranch(self):
        self.logger.info("****TestCase TermsPhrases-001 - Expands the First Branch***")
        self.logger.info("*****Login Successful****")
        self.logger.info("**** Terms And Phrases testing *****")
        self.navigator = TermsAndPhrases(self.driver)
        self.navigator.clickOnTermsAndPhrases()
        time.sleep(2)
        #self.navigator.clickOnClientListing()
        self.logger.info("Terms And Phrases menu is available")
        heading = self.navigator.getHeading()
        print(heading)
        self.navigator.clickOnFirstBranch()
        self.logger.info("Expanded First Branch")
        self.navigator.clickOnFirstBranch()
        self.logger.info("Collapsed Branch")
        self.navigator.clickOnFourthBranch()
        self.logger.info("Expanded Fourth Branch")
        self.navigator.clickOnFourthBranch()
        self.logger.info("Collapsed Branch")
        self.navigator.clickOnTwentiethBranch()
        self.logger.info("Expanded Twentieth Branch")
        self.navigator.clickOnTwentiethBranch()
        self.logger.info("Collapsed Branch")
        self.navigator.clickOnTwentySixthBranch()
        self.logger.info("Expanded TwentySixth Branch")
        self.navigator.clickOnTwentySixthBranch()
        self.logger.info("Collapsed Branch")
        time.sleep(2)


    #@pytest.mark.skip(reason="None")
    def test_addToResearchNotepad(self):
        self.logger.info("****TestCase TermsPhrases-002 - Add to Research Notepad***")
        self.logger.info("*****Login Successful****")
        self.logger.info("**** Terms And Phrases testing *****")
        self.navigator = TermsAndPhrases(self.driver)
        self.navigator.clickOnTermsAndPhrases()
        time.sleep(2)
        #self.navigator.clickOnClientListing()
        self.logger.info("Terms And Phrases menu is available")
        time.sleep(2)
        heading = self.navigator.getHeading()
        print(heading)
        self.logger.info(heading)
        self.navigator.clickOnFirstBranch()
        self.logger.info("Expanded First Branch")
        time.sleep(2)
        self.navigator.clickOnActions()
        self.logger.info("Clicked on Actions")
        time.sleep(2)
        self.navigator.clickOnAddtoResearchNotepad()
        self.logger.info("Clicked on Research Notepad")
        time.sleep(2)
        self.navigator.clickOnResearchTopicOption()
        self.logger.info("Selected the first option")
        time.sleep(2)
        self.navigator.clickOnAddResearch()
        self.logger.info("Clicked on Add Button")
        time.sleep(2)
        self.navigator.clickOnAddResearchTopicOption2()
        self.logger.info("Selected Entire Document")
        time.sleep(2)
        self.navigator.clickOnAddResearchButton2()
        self.logger.info("Clicked on Add Button")
        time.sleep(2)
        toastMessage = self.navigator.getToastMessageResearch()
        self.logger.info(toastMessage)

    #@pytest.mark.skip(reason="None")
    def test_copyLocation(self):
        self.logger.info("****TestCase AC-003 - Verify Copy Location***")
        self.navigator = TermsAndPhrases(self.driver)
        self.navigator.clickOnTermsAndPhrases()
        #self.navigator.clickOnClientListing()
        self.navigator.clickOnFirstBranch()
        self.logger.info("Expanded First Branch")
        time.sleep(2)
        self.navigator.clickOnActions()
        time.sleep(2)
        self.navigator.clickOnCopyLocation()
        self.logger.info("Clicked on Copy Location")
        time.sleep(2)
        # stringtext = pyperclip.paste()  # text will have the content of clipboard
        # print(stringtext)
        # self.driver.close()

    #@pytest.mark.skip(reason="None")
    def test_followTopic(self):
        self.logger.info("***TestCase TermsPhrases-004 - Follow Topic***")
        self.navigator = TermsAndPhrases(self.driver)
        self.navigator.clickOnTermsAndPhrases()
        time.sleep(2)
        #self.navigator.clickOnClientListing()
        self.navigator.clickOnFirstBranch()
        self.logger.info("Expandeded First Branch")
        time.sleep(2)
        self.navigator.clickOnActions()
        time.sleep(2)
        #self.navigator.clickOnFollowTopic()
        follow=self.driver.find_element(By.XPATH, "(//div[@class='card__actions dropdown']//div//label//span//span//i)[1]")
        self.driver.execute_script("arguments[0].click();", follow)
        self.logger.info("Clicked on Follow Topic")
        time.sleep(2)
        followTopicToastMessage = self.driver.find_element(By.XPATH, "/html/body/div[7]/span[3]").text
        followTopicMessage = self.driver.execute_script("return arguments[0]", followTopicToastMessage)
        self.logger.info(followTopicMessage)

    #@pytest.mark.skip(reason="None")
    def test_findAndReset(self):
        self.logger.info("****TestCase PC-005 - Validate Find and Reset***")
        self.navigator = TermsAndPhrases(self.driver)
        self.navigator.clickOnTermsAndPhrases()
        time.sleep(2)
        #self.navigator.clickOnClientListing()
        self.logger.info("Terms And Phrases menu is available")
        time.sleep(2)
        myopen = open('jsonfiles\TPFind.json', 'r')
        jsondata = myopen.read()
        with open('jsonfiles\TPFind.json') as data_file:
            data = json.load(data_file)
            for v in data.values():
                searchvalue = v
                findSendData = self.driver.find_element(By.XPATH,
                                                        "//*[@id='txtTermPhraseSearch']")

                # findSendData.clear()
                time.sleep(2)
                findSendData.send_keys(searchvalue)
                time.sleep(3)
                self.navigator.clickOnFind()
                found = self.driver.find_element(By.XPATH,
                                                 "//*[@id='matcheCnt']").text
                print(found)
                self.logger.info(found + " Matches Found")
                time.sleep(3)
                self.navigator.clickOnReset()
                self.logger.info("Clicked on Reset")

    #@pytest.mark.skip(reason="None")
    def test_fullCaseAnalysis(self):
        self.logger.info("***TestCase TermsPhrases-005 - Full Case Analysis***")
        self.navigator = TermsAndPhrases(self.driver)
        self.navigator.clickOnTermsAndPhrases()
        time.sleep(2)
        #self.navigator.clickOnClientListing()
        self.navigator.clickOnFirstBranch()
        self.logger.info("Expandeded First Branch")
        time.sleep(2)
        self.navigator.clickOnFullCaseAnalysis()
        time.sleep(2)
        parent_handle = self.driver.current_window_handle
        print(parent_handle)
        all_handles = self.driver.window_handles
        print(all_handles)
        for handle in all_handles:
            if handle != parent_handle:
                self.driver.switch_to.window(handle)
                time.sleep(2)
                text = self.driver.find_element(By.XPATH, "//*[@id='document-view']/nav/ul/li[5]").text
                self.logger.info(text)
                self.driver.close()
        self.driver.switch_to.window(parent_handle)
        time.sleep(2)

    #@pytest.mark.skip(reason="None")
    def test_copyCitation(self):
        self.logger.info("***TestCase TermsPhrases-006 - Copy Citation***")
        self.navigator = TermsAndPhrases(self.driver)
        self.navigator.clickOnTermsAndPhrases()
        #self.navigator.clickOnClientListing()
        time.sleep(2)
        self.navigator.clickOnFirstBranch()
        time.sleep(2)
        self.navigator.clickOnExpandCard()
        time.sleep(2)
        self.navigator.clickOnCopyCitation()
        time.sleep(2)
        copyCitationToastMessage = self.driver.find_element(By.XPATH, "/html/body/div[7]/span[3]").text
        result = self.driver.execute_script("return arguments[0]", copyCitationToastMessage)
        self.logger.info(result)
        #paste the copied citation to notepad
        #open the file for write operation
        # f = open('citationTP.txt', 'w')
        # citationcopied = clipboard.paste()
        # self.logger.info(citationcopied + "  copied citation")
        # f.write(citationcopied)
        # #close the file
        # f.close()
        # #open the file for read
        # f = open('citationTP.txt', 'r')
        # # print the contents in console
        # print(f.read())
        # # # # close the file
        # f.close()

    #@pytest.mark.skip(reason="None")
    def test_cataloguedSN(self):
        self.logger.info("***TestCase TermsPhrases-007 - Catalogue Subject Navigator**")
        self.navigator = TermsAndPhrases(self.driver)
        self.navigator.clickOnTermsAndPhrases()
        #self.navigator.clickOnClientListing()
        time.sleep(2)
        self.navigator.clickOnFirstBranch()
        time.sleep(2)
        self.navigator.clickOnExpandCard()
        time.sleep(2)
        self.navigator.clickOnCatalogued()
        self.logger.info("Clicked on Catalogued Subject Navigator")
        time.sleep(2)
        element = self.driver.find_element(By.XPATH, "(//p[@class='pCatalogued']//a)[1]").text
        print(element)
        self.logger.info(element)

    #@pytest.mark.skip(reason="None")
    def test_copyExcerpt(self):
        self.logger.info("***TestCase TermsPhrases-008 - Copy Excerpt**")
        self.navigator = TermsAndPhrases(self.driver)
        self.navigator.clickOnTermsAndPhrases()
        #self.navigator.clickOnClientListing()
        time.sleep(2)
        self.navigator.clickOnFirstBranch()
        time.sleep(2)
        self.navigator.clickOnExpandCard()
        time.sleep(2)
        self.navigator.clickOnParagraphExcerpt()
        time.sleep(2)
        self.logger.info("clicked on a paragraph excerpt")
        self.navigator.clickOnCopyExcerpt()
        time.sleep(3)
        self.logger.info("Clicked on Copy Excerpt")
        copyCitationToastMessage = self.driver.find_element(By.XPATH, "/html/body/div[7]/span[3]").text
        time.sleep(3)
        #result = self.driver.execute_script("return arguments[0]", copyCitationToastMessage)
        print(copyCitationToastMessage)

    #@pytest.mark.skip(reason="None")
    def test_textLink(self):
        self.logger.info("***TestCase TermsPhrases-009 - Text Link validation**")
        self.navigator = TermsAndPhrases(self.driver)
        self.navigator.clickOnTermsAndPhrases()
        #self.navigator.clickOnClientListing()
        time.sleep(2)
        self.navigator.clickOnFirstBranch()
        self.logger.info("Clicked on the first branch")
        # result = self.driver.find_element(By.XPATH, "(//a[@class='link__text termSourceBookmarkTitle'])[1]").text
        # print(result)
        time.sleep(2)
        self.navigator.clickOnTextLink()
        self.logger.info("Clicked on a text link")
        parent_handle = self.driver.current_window_handle
        print(parent_handle)
        all_handles = self.driver.window_handles
        print(all_handles)
        for handle in all_handles:
            if handle != parent_handle:
                self.driver.switch_to.window(handle)
                time.sleep(2)
                # text = self.driver.find_element(By.XPATH, "//*[@id='select-cases-citing']").text
                # self.logger.info(text)
                # # if text== result:
                # #     self.logger.info("Pass")
                self.driver.close()
        self.driver.switch_to.window(parent_handle)
        time.sleep(2)
        self.driver.quit()
