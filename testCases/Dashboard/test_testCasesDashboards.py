import sys
from telnetlib import EC
from urllib import request

import clipboard
import pytest
import time
import json
import allure

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select

from pageObjects.Dashboard import Dashboard
from pageObjects.LoginPage import LoginPage
from pageObjects.SubjectNavigator import SubjectNavigator
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
class Test_testCasesDashboard:
    logger = LogGen.loggen()

    #@pytest.mark.skip(reason="None")
    def test_createResearchTopic(self):
        self.logger.info("****TestCase Dashboard-001 - Validate Create ResearchTopic***")
        self.logger.info("*****Login Successful****")
        self.navigator = Dashboard(self.driver)
        self.navigator.clickOnResearchNotepad()
        self.logger.info("Clicked on Research Notepad Link from the Dashboard")
        # self.navigator.clickOnClientListing()
        self.navigator.clickOnResearchTopic()
        time.sleep(2)
        self.logger.info("Clicked on Create a New Research Topic button")
        self.navigator.sendKeysName()
        time.sleep(2)
        self.logger.info("Entered Name")
        self.navigator.sendKeysDescription()
        time.sleep(2)
        self.logger.info("Entered Description")
        self.navigator.clickOnCreateNewTopic()
        time.sleep(2)
        self.logger.info("Clicked on Create New Topic")
        time.sleep(2)
        self.navigator.clickOnResearchTopic()
        time.sleep(2)
        self.logger.info("Clicked on Create a New Research Topic button")
        self.navigator.sendKeysName()
        time.sleep(2)
        self.logger.info("Entered Name")
        self.navigator.sendKeysDescription()
        time.sleep(2)
        self.logger.info("Entered Description")
        self.navigator.clickOnCreateNewTopic()
        # #print(self.navigator.researchTopicToastMessage)
        # Validate creating topic that already exists.
        a = self.navigator.validateErrorMessageTopicAlreadyExists()
        print(a)
        self.logger.info(a)
        if a == "Topic name is already exists.":
            self.logger.info("Displayed the correct message   " + a)
        else:
            self.logger.info("Either the message is not displayed correctly or doesn't display any message")

        time.sleep(2)

    #@pytest.mark.skip(reason="None")
    def test_cancelResearchTopic(self):
        self.logger.info("****TestCase Dashboard-002 - Validate Cancel ResearchTopic***")
        self.logger.info("*****Login Successful****")
        self.navigator = Dashboard(self.driver)
        self.navigator.clickOnResearchNotepad()
        self.logger.info("Clicked on Research Notepad Link from the Dashboard")
        # self.navigator.clickOnClientListing()
        time.sleep(2)
        self.navigator.clickOnResearchTopic()
        time.sleep(2)
        self.logger.info("Clicked on Create a New Research Topic button")
        self.navigator.sendKeysName()
        time.sleep(2)
        self.logger.info("Entered Name")
        self.navigator.sendKeysDescription()
        time.sleep(1)
        self.logger.info("Entered Description")
        self.navigator.clickOnCancelresearch()
        self.logger.info("Clicked on Cancel")
        time.sleep(2)

    #@pytest.mark.skip(reason="None")
    def test_editResearchTopic(self):
        self.logger.info("****TestCase Dashboard-003 - Validate Edit ResearchTopic***")
        self.logger.info("*****Login Successful****")
        self.navigator = Dashboard(self.driver)
        self.navigator.clickOnResearchNotepad()
        self.logger.info("Clicked on Research Notepad Link from the Dashboard")
        # self.navigator.clickOnClientListing()
        time.sleep(2)
        self.navigator.clickOnEditResearch()
        time.sleep(2)
        self.navigator.clickOnSaveChanges()
        time.sleep(2)
        self.logger.info("Clicked on Save Changes")
        # Try to save changes with an empty topic name
        self.navigator.clickOnEditResearch()
        time.sleep(2)
        self.navigator.clearResearchTopicName()
        time.sleep(1)
        self.logger.info("Cleared the topic name")
        self.navigator.clickOnSaveChanges()
        time.sleep(2)
        requiredMessage = self.navigator.requiredMessageTopic()
        print(requiredMessage)
        self.logger.info(requiredMessage)
        if requiredMessage == "Please enter name.":
            self.logger.info("Displayed the correct message   " + requiredMessage)
        else:
            self.logger.info("Displayed the incorrect required message")
        if requiredMessage == "":
            self.logger.info("Empty Message is dispplayed")
        time.sleep(2)

    #@pytest.mark.skip(reason="None")
    def test_deleteResearchTopic(self):
        self.logger.info("****TestCase Dashboard-004 - Validate Delete ResearchTopic***")
        self.logger.info("*****Login Successful****")
        self.navigator = Dashboard(self.driver)
        self.navigator.clickOnResearchNotepad()
        self.logger.info("Clicked on Research Notepad Link from the Dashboard")
        time.sleep(2)
        # self.navigator.clickOnClientListing()
        # Before deleting get the text of the opic
        textResearchTopic = self.navigator.getTextResearchTopic()
        print(textResearchTopic)
        topicText = textResearchTopic
        self.logger.info("Research Topic 1st row from the table is    " + textResearchTopic)
        time.sleep(1)
        self.navigator.clickOnDeleteResearch()
        self.logger.info("Clicked on Delete Topic")
        time.sleep(2)
        self.navigator.clickOnConfirmDelete()
        self.logger.info("Clicked on Confirm Delete")
        time.sleep(2)
        self.navigator.clickOnSearchResearchTopic()
        time.sleep(2)
        enterSearch = self.driver.find_element(By.XPATH, "//*[@id='Serach']")
        enterSearch.send_keys(topicText)
        self.navigator.clickOnFindResearchTopic()
        time.sleep(2)
        noDataAvailable = self.driver.find_element(By.XPATH, "(//tr[@class='odd']//td)[1]").text
        print(noDataAvailable)
        if noDataAvailable == "No data available in table":
            self.logger.info("Displayed Message   " + noDataAvailable)
        else:
            self.logger.info("Message is not displayed correctly")
        time.sleep(2)

    #@pytest.mark.skip(reason="None")
    def test_searchResearchTopic(self):
        self.logger.info("****TestCase Dashboard-005 - Validate search Research topic***")
        self.logger.info("*****Login Successful****")
        self.navigator = Dashboard(self.driver)
        self.navigator.clickOnResearchNotepad()
        self.logger.info("Clicked on research Notepad")
        # self.navigator.clickOnClientListing()
        time.sleep(2)
        myopen = open('jsonfiles\searchTopic.json', 'r')
        jsondata = myopen.read()
        with open('jsonfiles\searchTopic.json') as data_file:
            data = json.load(data_file)
            for v in data.values():
                searchvalue = v
                findSendData = self.driver.find_element(By.XPATH,
                                                        "//*[@id='Serach']")
                self.driver.execute_script("arguments[0].click();", findSendData)
                time.sleep(2)
                findSendData.clear()
                time.sleep(1)
                findSendData.send_keys(searchvalue)
                time.sleep(2)
                findSendData.send_keys(Keys.RETURN)
                time.sleep(2)
                searchstr = self.driver.find_element(By.XPATH, "//*[@id='tblResearchNotepadTopicMaster_info']").text
                self.logger.info(searchstr)
        time.sleep(2)

    #@pytest.mark.skip(reason="None")
    def test_sortResearchTopic(self):
        self.logger.info("****TestCase Dashboard-006 - Validate Research topic Table - Sort by Topic Name***")
        self.logger.info("*****Login Successful****")
        self.navigator = Dashboard(self.driver)
        self.navigator.clickOnResearchNotepad()
        self.logger.info("Clicked on research Notepad")
        # self.navigator.clickOnClientListing()
        # get rows from Research Notepad table before sort
        rows = self.driver.find_elements(By.XPATH, "//div[@class='table__container']//div//table//tbody//tr")
        r = len(rows)
        print(r)
        for i in range(1, r + 1):
            getData = self.driver.find_element(By.XPATH, "//tr[" + str(i) + "]").text
            print(getData)
            self.logger.info(getData)
            time.sleep(2)
        clickOnTopicName = self.driver.find_element(By.XPATH, "//div[@class='table__wrapper']//table//thead//tr//th[1]")
        self.driver.execute_script("arguments[0].click();", clickOnTopicName)
        # get rows from Research Notepad table after sort by Ascending
        rows = self.driver.find_elements(By.XPATH, "//div[@class='table__container']//div//table//tbody//tr")
        r = len(rows)
        print(r)
        for i in range(1, r + 1):
            getData = self.driver.find_element(By.XPATH, "//tr[" + str(i) + "]").text
            print(getData)
            self.logger.info(getData)
            time.sleep(2)
        clickOnTopicName = self.driver.find_element(By.XPATH, "//div[@class='table__wrapper']//table//thead//tr//th[1]")
        self.driver.execute_script("arguments[0].click();", clickOnTopicName)
        # get rows from Research Notepad table after sort by Descending
        rows = self.driver.find_elements(By.XPATH, "//div[@class='table__container']//div//table//tbody//tr")
        r = len(rows)
        print(r)
        for i in range(1, r + 1):
            getData = self.driver.find_element(By.XPATH, "//tr[" + str(i) + "]").text
            print(getData)
            self.logger.info(getData)
            time.sleep(2)

    #@pytest.mark.skip(reason="None")
    def test_createDocumentComaprison(self):
        self.logger.info("****TestCase Dashboard-007- Validate Create DocumentComparison Group***")
        self.logger.info("*****Login Successful****")
        self.navigator = Dashboard(self.driver)
        self.navigator.clickOnDocumentComparison()
        self.logger.info("Clicked on Document Comparison link")
        # self.navigator.clickOnClientListing()
        time.sleep(2)
        self.navigator.clickOnCreateDocumentComparison()
        self.logger.info("Clicked on Create Document Comparison")
        time.sleep(2)
        self.navigator.sendKeysDocumentComparison()
        self.logger.info("Entered Comparison Name")
        time.sleep(2)
        self.navigator.sendKeysDocumentDescription()
        self.logger.info("Entered Description")
        time.sleep(2)
        self.navigator.clickOnCreateGroup()
        self.logger.info("Clicked on Create Group")
        time.sleep(2)
        self.navigator.clickOnDocumentComparison()
        self.logger.info("Clicked on Document Comparison link")
        self.navigator.clickOnCreateDocumentComparison()
        self.logger.info("Clicked on Create Document Comparison")
        time.sleep(2)
        self.navigator.clickOnCreateGroup()
        self.logger.info("Clicked on Create Group")
        time.sleep(2)
        validationText = self.driver.find_element(By.XPATH, "//*[@id='txtDocumentComparisionNameError']").text
        if validationText == "Please enter name.":
            self.logger.info("Validation Message  " + validationText + "  is displayed")
        else:
            self.logger.info("Displayed the incorrect required message")
        if validationText == "":
            self.logger.info("Empty Message is dispplayed")
        time.sleep(2)

    #@pytest.mark.skip(reason="None")
    def test_editDocumentComaprison(self):
        self.logger.info("****TestCase Dashboard-008 - Validate update document group***")
        self.logger.info("*****Login Successful****")
        self.navigator = Dashboard(self.driver)
        self.navigator.clickOnDocumentComparison()
        self.logger.info("Clicked on Document Comparison link")
        # self.navigator.clickOnClientListing()
        time.sleep(2)
        self.navigator.clickOnEditGroup()
        self.logger.info("Clicked on Edit Group")
        time.sleep(2)
        self.navigator.sendKeysUpdateGroup()
        self.logger.info("Cleared existing name and entered new name")
        time.sleep(2)
        self.navigator.clickOnSaveGroup()
        self.logger.info("Clicked on Save Group")
        time.sleep(2)
        self.logger.info("Clicked on Document Comparison link")
        # self.navigator.clickOnClientListing()
        time.sleep(2)
        self.navigator.clickOnEditGroup()
        self.logger.info("Clicked on Edit Group")
        time.sleep(2)
        groupName = self.driver.find_element(By.XPATH, "//*[@id='txtEditDocumentComparisionName']")
        groupName.clear()
        self.navigator.clickOnSaveGroup()
        self.logger.info("Clicked on Save Group")
        time.sleep(2)
        validationText = self.driver.find_element(By.XPATH, "//*[@id='txtDocumentComparisionNameError']").text
        if validationText == "Please enter name.":
            self.logger.info("Validation Message  " + validationText + "  is displayed")
        else:
            self.logger.info("Displayed the incorrect required message")
        if validationText == "":
            self.logger.info("Empty Message is dispplayed")
        time.sleep(2)

    #@pytest.mark.skip(reason="None")
    def test_deleteDocumentComaprison(self):
        self.logger.info("****TestCase Dashboard-009 - Validate delete document group***")
        self.logger.info("*****Login Successful****")
        self.navigator = Dashboard(self.driver)
        self.navigator.clickOnDocumentComparison()
        self.logger.info("Clicked on Document Comparison link")
        # self.navigator.clickOnClientListing()
        time.sleep(2)
        # Before deleting get the name of the Group
        textGroupName = self.navigator.getTextGroupName()
        print(textGroupName)
        groupNameText = textGroupName
        self.logger.info("Document Comparison Group Name- 1st row from the table is    " + textGroupName)
        time.sleep(1)
        self.navigator.clickOnDeleteGroup()
        self.logger.info("Clicked on Delete Group")
        time.sleep(2)
        self.navigator.clickOnConfirmDeleteGroup()
        self.logger.info("Clicked on Confirm Delete Group")
        time.sleep(2)
        self.navigator.clickOnSearchGroupName()
        time.sleep(2)
        enterSearch = self.driver.find_element(By.XPATH, "//*[@id='Serach']")
        enterSearch.send_keys(groupNameText)
        self.navigator.clickOnFindGroupName()
        time.sleep(2)
        noDataAvailable = self.driver.find_element(By.XPATH, "(//tr[@class='odd']//td)[1]").text
        print(noDataAvailable)
        if noDataAvailable == "No data available in table":
            self.logger.info("Displayed Message   " + noDataAvailable)
        else:
            self.logger.info("Message is not displayed correctly")
        time.sleep(2)

    #@pytest.mark.skip(reason="None")
    def test_searchGroupName(self):
        self.logger.info("****TestCase Dashboard-0010 - Validate search Group Name***")
        self.logger.info("*****Login Successful****")
        self.navigator = Dashboard(self.driver)
        self.navigator.clickOnDocumentComparison()
        self.logger.info("Clicked on research Notepad")
        # self.navigator.clickOnClientListing()
        time.sleep(2)
        myopen = open('jsonfiles\searchGroupName.json', 'r')
        jsondata = myopen.read()
        with open('jsonfiles\searchGroupName.json') as data_file:
            data = json.load(data_file)
            for v in data.values():
                searchvlaue = v
                findSendData = self.driver.find_element(By.XPATH,
                                                        "//*[@id='Serach']")
                self.driver.execute_script("arguments[0].click();", findSendData)
                time.sleep(2)
                findSendData.clear()
                time.sleep(1)
                findSendData.send_keys(searchvlaue)
                time.sleep(2)
                findSendData.send_keys(Keys.RETURN)
                time.sleep(2)
                searchstr = self.driver.find_element(By.XPATH, "//*[@id='tblDocumentComparisonMaster_info']").text
                self.logger.info(searchstr)
        time.sleep(2)

    #@pytest.mark.skip(reason="None")
    def test_cancelComparisonGroup(self):
        self.logger.info("****TestCase Dashboard-011 - Validate Cancel Document Comparison Group***")
        self.logger.info("*****Login Successful****")
        self.navigator = Dashboard(self.driver)
        self.navigator.clickOnDocumentComparison()
        self.logger.info("Clicked on Document Comparison link")
        # self.navigator.clickOnClientListing()
        time.sleep(2)
        self.navigator.clickOnCreateDocumentComparison()
        self.logger.info("Clicked on Create Document Comparison")
        time.sleep(2)
        self.navigator.sendKeysDocumentComparison()
        time.sleep(2)
        self.logger.info("Entered Comparison Name")
        time.sleep(1)
        self.navigator.sendKeysDocumentDescription()
        time.sleep(2)
        self.logger.info("Entered Description")
        time.sleep(1)
        self.navigator.clickOnCancelDocument()
        time.sleep(2)
        self.logger.info("Clicked on Cancel")
        time.sleep(2)
        # title = self.driver.find_element(By.XPATH, "//*[@id='page-content']/div/div[1]/div/div/div[1]/h1").text
        # assert "Google" in title

    #@pytest.mark.skip(reason="None")
    def test_Reset(self):
        self.logger.info("****TestCase Dashboard-012 - Validate Global Search- Reset Link***")
        self.navigator = Dashboard(self.driver)
        self.navigator.clickOnGlobalSearch()
        time.sleep(2)
        # self.navigator.clickOnReset()
        # time.sleep(2)
        self.navigator.clickOnKeyword()
        time.sleep(2)
        keysend = self.driver.find_element(By.XPATH, "//*[@id='globalsearchtext']")
        keysend.send_keys("Cairo")
        time.sleep(2)
        self.navigator.clickOnReset()
        time.sleep(2)

    #@pytest.mark.skip(reason="None")
    def test_GlobalSearch(self):
        self.logger.info("****TestCase Dashboard-013 - Validate Global Search- Subject Navigator***")
        self.navigator = Dashboard(self.driver)
        self.driver.find_element(By.XPATH, "//*[@id='Rslink']/li[1]/a/span").click()
        time.sleep(2)
        self.navigator.clickOnGlobalSearch()
        self.logger.info("Clicked on Global Search")
        time.sleep(2)
        self.navigator.clickOnKeyword()
        self.logger.info("Set focus on Search textbox")
        time.sleep(2)
        keysend = self.driver.find_element(By.XPATH, "//*[@id='globalsearchtext']")
        keysend.send_keys("cairo")
        self.logger.info("Key sent to the textbox")
        time.sleep(2)
        self.navigator.clickOnFind()
        time.sleep(2)
        self.logger.info("Clicked on Find")
        time.sleep(2)
        # Global Search Results- Check to see if any results are displayed for Subject Navigator
        parent_handle = self.driver.current_window_handle
        all_handles = self.driver.window_handles
        links = []
        the_links = self.driver.find_elements_by_link_text('View Results')
        all_handles = self.driver.window_handles
        print(all_handles)
        for element in the_links:
            for handle in all_handles:
                element.click()
                time.sleep(2)
                if handle != parent_handle:
                    self.driver.switch_to.window(handle)
                    time.sleep(3)
                    self.driver.close()
                    time.sleep(2)
                    break
        self.driver.switch_to.window(parent_handle)
        #validate find button without entering a keyword.
        time.sleep(2)
        clearTextBox = self.driver.find_element(By.XPATH, "//*[@id='globalsearchtext']")
        clearTextBox.clear()
        self.navigator.clickOnFind()
        requiredTextValidation = self.driver.find_element(By.XPATH, "//*[@id='validationmessage']/span").text
        if requiredTextValidation == "Please enter search keyword":
            self.logger.info("Validation message    "  + requiredTextValidation + "   is displayed")
        else:
            self.logger.info("No message is displayed.")
        self.driver.quit()




