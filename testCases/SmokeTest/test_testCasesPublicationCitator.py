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
from pageObjects.PublicationCitator import PublicationCitator
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


def assertEqual(result, param):
    pass


@pytest.mark.usefixtures("setup")
class Test_PublicationCitator:
    logger = LogGen.loggen()

    #@pytest.mark.skip(reason="None")
    def test_expandPublicationCitator(self):
        self.logger.info("****TestCase PC-001 - Expand and Collapse Publication Citator***")
        self.logger.info("*****Login Successful****")
        self.logger.info("**** Publication Citator testing *****")
        self.navigator = PublicationCitator(self.driver)
        self.navigator.clickOnPublicationCitator()
        time.sleep(2)
        #self.navigator.clickOnClientListing()
        time.sleep(5)
        self.logger.info("Publication Citator menu is available")
        time.sleep(2)
        heading = self.navigator.getHeading()
        print(heading)
        self.logger.info(heading)
        self.navigator.clickOnFirstPublication()
        self.logger.info("Expanded Publication Citator")
        time.sleep(2)
        self.navigator.clickOnCollapse()
        self.logger.info("Collapsed Publication Citator")

    #@pytest.mark.skip(reason="None")
    def test_copyCitation(self):
        self.logger.info("***TestCase PC-002 - Copy Citation***")
        self.navigator = PublicationCitator(self.driver)
        self.navigator.clickOnPublicationCitator()
        # self.navigator.clickOnClientListing()
        time.sleep(2)
        self.navigator.clickOnFirstPublication()
        time.sleep(2)
        self.navigator.clickOnCopyCitation()
        time.sleep(2)
        copyCitationToastMessage = self.driver.find_element(By.XPATH, "/html/body/div[7]/span[3]").text
        #result = self.driver.execute_script("return arguments[0]", copyCitationToastMessage)
        self.logger.info(copyCitationToastMessage)
        # # paste the copied citation to notepad
        # # open the file for write operation
        # f = open('citationPC.txt', 'w')
        # citationcopied = clipboard.paste()
        # self.logger.info(citationcopied + "  copied citation")
        # f.write(citationcopied)
        # # # close the file
        # f.close()
        # # # open the file for read
        # f = open('citationPC.txt', 'r')
        # # # print the contents in console
        # print(f.read())
        # # # close the file
        # f.close()

    #@pytest.mark.skip(reason="None")
    def test_addToResearchNotepad(self):
        self.logger.info("***TestCase PC-003 - Add To Research Notepad***")
        self.navigator = PublicationCitator(self.driver)
        self.navigator.clickOnPublicationCitator()
        time.sleep(2)
        #self.navigator.clickOnClientListing()
        self.navigator.clickOnFirstPublication()
        self.logger.info("Expanded Publication Citator")
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
        self.navigator.clickOnResearchOption2()
        self.logger.info("Selected Entire Document option")
        time.sleep(2)
        self.navigator.clickOnResearchOptionAdd2()
        self.logger.info("Clicked on Add Research")
        time.sleep(2)
        researchToastMessage = self.driver.find_element(By.XPATH, "/html/body/div[7]/span[3]").text
        result = self.driver.execute_script("return arguments[0]", researchToastMessage)
        self.logger.info(result)

    #@pytest.mark.skip(reason="None")
    def test_copyLocation(self):
        self.logger.info("****TestCase PC-004 - Verify Copy Location***")
        self.navigator = PublicationCitator(self.driver)
        self.navigator.clickOnPublicationCitator()
        time.sleep(2)
        #self.navigator.clickOnClientListing()
        self.navigator.clickOnFirstPublication()
        self.logger.info("Expanded Publication Citator")
        time.sleep(2)
        self.navigator.clickOnActions()
        self.logger.info("Clicked on Actions")
        time.sleep(2)
        self.navigator.clickOnCopyLocation()
        self.logger.info("Clicked on Copy Location")
        time.sleep(2)
        parent_handle = self.driver.current_window_handle
        print(parent_handle)
        time.sleep(3)
        myurl = clipboard.paste()
        # print(myurl)
        # self.logger.info(myurl + "  URL copied")
        # self.driver.execute_script("window.open('" + myurl + "');")
        # time.sleep(2)
        all_handles = self.driver.window_handles
        # print(all_handles)
        for handle in all_handles:
            if handle != parent_handle:
                self.driver.switch_to.window(handle)
                time.sleep(2)
                self.driver.close()
        self.driver.switch_to.window(parent_handle)
        time.sleep(2)

    #@pytest.mark.skip(reason="None")
    def test_followTopic(self):
        self.logger.info("***TestCase PC-005 - Follow Topic***")
        self.navigator = PublicationCitator(self.driver)
        self.navigator.clickOnPublicationCitator()
        time.sleep(2)
        #self.navigator.clickOnClientListing()
        self.navigator.clickOnFirstPublication()
        self.logger.info("Expanded Publication Citator")
        time.sleep(2)
        self.navigator.clickOnActions()
        self.logger.info("Clicked on Actions")
        time.sleep(2)
        self.navigator.clickOnFollowTopic()
        self.logger.info("Clicked on Follow Topic")
        time.sleep(2)
        #followTopicToastMessage = self.driver.find_element(By.XPATH, "/html/body/div[7]/span[3]").text
        #followMessage = self.driver.execute_script("return arguments[0]", followTopicToastMessage)
        self.logger.info("Toast Message - you have followed topic is displayed")
        self.navigator.clickOnActions()
        time.sleep(2)
        # followtopicstate = self.driver.find_element(By.XPATH,
        #                                             "(//div[@class='card__actions dropdown']//label//input)[1]")
        # elementdisabled = followtopicstate.get_property('disabled')
        # print(elementdisabled)
        # self.logger.info(elementdisabled)
        # self.logger.info("follow topic is disabled")
        # time.sleep(2)

    #@pytest.mark.skip(reason="None")
    def test_BooksSubmenu(self):
        self.logger.info("***TestCase PC-006 - Books Sub menu***")
        self.navigator = PublicationCitator(self.driver)
        self.navigator.clickOnPublicationCitator()
        time.sleep(2)
        #self.navigator.clickOnClientListing()
        self.navigator.clickOnBooks()
        self.logger.info("Clicked on Books Sub Menu")
        result = self.driver.find_element(By.XPATH, "//*[@id='publication-filter-dropdown-control']/span[1]").text
        self.logger.info(result)
        matchesFound = self.driver.find_element(By.XPATH, "//*[@id='page-content']/div/div/div[4]/div[1]/p/strong").text
        self.logger.info(matchesFound)
        print(matchesFound)
        self.navigator.clickOnBooksFirstPublication()
        time.sleep(2)
        self.logger.info("Expanded Publication Citator")
        # Type validation

    #@pytest.mark.skip(reason="None")
    def test_DictionarySubmenu(self):
        self.logger.info("***TestCase PC-007 - Dictionary/Encyclopedia Sub menu***")
        self.navigator = PublicationCitator(self.driver)
        self.navigator.clickOnPublicationCitator()
        time.sleep(2)
        #self.navigator.clickOnClientListing()
        self.navigator.clickOnDictionary()
        self.logger.info("Clicked on Dictionary/Encyclopedia Sub Menu")
        result = self.driver.find_element(By.XPATH, "//*[@id='publication-filter-dropdown-control']/span[1]").text
        self.logger.info(result)
        matchesFound = self.driver.find_element(By.XPATH, "//*[@id='page-content']/div/div/div[4]/div[1]/p/strong").text
        self.logger.info(matchesFound)
        print(matchesFound)
        self.navigator.clickOnBooksFirstPublication()
        time.sleep(2)
        self.logger.info("Expanded Publication Citator")
        # Type validation

    #@pytest.mark.skip(reason="None")
    def test_NewsSubmenu(self):
        self.logger.info("***TestCase PC-008 - News/Online Source Sub menu***")
        self.navigator = PublicationCitator(self.driver)
        self.navigator.clickOnPublicationCitator()
        time.sleep(2)
        #self.navigator.clickOnClientListing()
        self.navigator.clickOnNewsOnline()
        self.logger.info("Clicked on News/Online Source Sub Menu")
        result = self.driver.find_element(By.XPATH, "//*[@id='publication-filter-dropdown-control']/span[1]").text
        self.logger.info(result)
        matchesFound = self.driver.find_element(By.XPATH, "//*[@id='page-content']/div/div/div[4]/div[1]/p/strong").text
        self.logger.info(matchesFound)
        print(matchesFound)
        self.navigator.clickOnBooksFirstPublication()
        time.sleep(2)
        self.logger.info("Expanded Publication Citator")
        # Type validation

    #@pytest.mark.skip(reason="None")
    def test_OtherSubmenu(self):
        self.logger.info("***TestCase PC-009 - Other Sub menu***")
        self.navigator = PublicationCitator(self.driver)
        self.navigator.clickOnPublicationCitator()
        time.sleep(2)
        #self.navigator.clickOnClientListing()
        self.navigator.clickOnOther()
        self.logger.info("Clicked on Other Sub Menu")
        result = self.driver.find_element(By.XPATH, "//*[@id='publication-filter-dropdown-control']/span[1]").text
        self.logger.info(result)
        matchesFound = self.driver.find_element(By.XPATH, "//*[@id='page-content']/div/div/div[4]/div[1]/p/strong").text
        self.logger.info(matchesFound)
        print(matchesFound)
        #self.navigator.clickOnBooksFirstPublication()
        time.sleep(2)
        self.logger.info("Expanded Publication Citator")
        # Type validation

    #@pytest.mark.skip(reason="None")
    def test_Periodicals(self):
        self.logger.info("***TestCase PC-010 - Periodicals Sub menu***")
        self.navigator = PublicationCitator(self.driver)
        self.navigator.clickOnPublicationCitator()
        time.sleep(2)
        #self.navigator.clickOnClientListing()
        self.navigator.clickOnPeriodicals()
        self.logger.info("Clicked on Other Sub Menu")
        result = self.driver.find_element(By.XPATH, "//*[@id='publication-filter-dropdown-control']/span[1]").text
        self.logger.info(result)
        matchesFound = self.driver.find_element(By.XPATH, "//*[@id='page-content']/div/div/div[4]/div[1]/p/strong").text
        self.logger.info(matchesFound)
        print(matchesFound)
        #self.navigator.clickOnBooksFirstPublication()
        time.sleep(2)
        self.logger.info("Expanded Publication Citator")
        # Type validation

    #@pytest.mark.skip(reason="None")
    def test_findAndReset(self):
        self.logger.info("****TestCase PC-011 - Validate Find and Reset***")
        self.navigator = PublicationCitator(self.driver)
        self.navigator.clickOnPublicationCitator()
        time.sleep(2)
        #self.navigator.clickOnClientListing()
        self.logger.info("PublicationCitator menu is available")
        time.sleep(2)
        myopen = open('jsonfiles\PCFind.json', 'r')
        jsondata = myopen.read()
        with open('jsonfiles\PCFind.json') as data_file:
            data = json.load(data_file)
            for v in data.values():
                searchvalue = v
                findSendData = self.driver.find_element(By.XPATH,
                                                        "//*[@id='search-publication']")

                # findSendData.clear()
                time.sleep(2)
                findSendData.send_keys(searchvalue)
                time.sleep(3)
                self.driver.find_element(By.XPATH, "//*[@id='page-content']/div/div").click()
                self.navigator.clickOnFind()
                time.sleep(3)
                found = self.driver.find_element(By.XPATH,
                                                 "//*[@id='search-popover']//p//strong//span").get_attribute(
                    'textContent')
                print(found)
                self.logger.info(found + " Matches Found")
                time.sleep(3)
                self.navigator.clickOnReset()
                self.logger.info("Clicked on Reset")
        time.sleep(2)

