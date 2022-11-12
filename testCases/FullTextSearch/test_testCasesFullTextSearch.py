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
    def test_SearchAndReset(self):
        try:
            self.logger.info("****TestCase Full Text Search-001 - Validate Search & Reset***")
            self.logger.info("*****Login Successful****")
            self.logger.info("**** Full Text Search testing *****")
            self.navigator = FullTextSearch(self.driver)
            self.navigator.clickOnFullTextSearchMenu()
            self.logger.info("Full Text Search menu was clicked")
            time.sleep(2)
            #self.navigator.clickOnClientListing()
            heading = self.navigator.getHeading()
            self.logger.info(heading)
            myopen = open('jsonfiles\FTSearch.json', 'r')
            jsondata = myopen.read()
            with open('jsonfiles\FTSearch.json') as data_file:
                data = json.load(data_file)
                for v in data.values():
                    searchvalue = v
                    findSendData = self.driver.find_element(By.XPATH,
                                                            "//*[@id='txtFTSSearch']")

                    # findSendData.clear()
                    time.sleep(2)
                    findSendData.send_keys(searchvalue)
                    time.sleep(2)
                    self.navigator.clickOnSearch()
                    found = self.driver.find_element(By.XPATH,
                                                     "//*[@id='page-content']/div/div[1]/div[5]/div[3]/div/div[1]/p/strong").text
                    print(found)
                    self.logger.info(found + " Matches Found")
                    time.sleep(2)
                    self.driver.find_element(By.CSS_SELECTOR,
                                             "#page-content > div > div > div.form__set.form__set--inline > div.form__group.form__group--wide > a").click()
                    self.logger.info("Clicked on Reset")
        except Exception:
            print("This test case failed")

    #@pytest.mark.skip(reason="None")
    def test_CopyCitation(self):
        self.logger.info("****TestCase Full Text Search-002 - Validate Copy Citation***")
        self.logger.info("*****Login Successful****")
        self.logger.info("**** Full Text Search testing *****")
        self.navigator = FullTextSearch(self.driver)
        self.navigator.clickOnFullTextSearchMenu()
        self.logger.info("Full Text Search menu was clicked")
        time.sleep(2)
        # self.navigator.clickOnClientListing()
        heading = self.navigator.getHeading()
        self.logger.info(heading)
        search = self.driver.find_element(By.XPATH, "//*[@id='txtFTSSearch']")
        search.send_keys("Countries")
        self.navigator.clickOnSearch()
        self.navigator.clickOnCopyCitation()
        time.sleep(2)
        self.logger.info("Clicked on Copy Citation")
        # citationToastMessage = self.driver.find_element(By.XPATH, "/html/body/div[8]/span[3]")
        # print(citationToastMessage.text())
        # result = self.driver.execute_script("return arguments[0]", citationToastMessage)
        # self.logger.info(citationToastMessage.text())
        # citation = clipboard.paste()
        # print(citation)
        # self.logger.info(citation + "  Citation copied")

    #@pytest.mark.skip(reason="None")
    def test_ResearchNotepad(self):
        self.logger.info("****TestCase Full Text Search-003 - Validate Research Notepad***")
        self.logger.info("*****Login Successful****")
        self.logger.info("**** Full Text Search testing *****")
        self.navigator = FullTextSearch(self.driver)
        self.navigator.clickOnFullTextSearchMenu()
        self.logger.info("Full Text Search menu was clicked")
        time.sleep(2)
        # self.navigator.clickOnClientListing()
        search = self.driver.find_element(By.XPATH, "//*[@id='txtFTSSearch']")
        search.send_keys("Countries")
        self.navigator.clickOnSearch()
        time.sleep(2)
        self.navigator.clickOnActions()
        self.logger.info("Clicked on Actions")
        time.sleep(2)
        self.navigator.clickOnResearchNotepad()
        self.logger.info("Clicked on Research Notepad")
        time.sleep(2)
        self.navigator.clickOnResearchTopic()
        self.logger.info("Clicked on Research Topic")
        time.sleep(2)
        self.navigator.clickOnResearchAdd()
        self.logger.info("Clicked on Research Add button")
        time.sleep(2)


    #@pytest.mark.skip(reason="None")
    def test_ViewDocument(self):
        self.logger.info("****TestCase Full Text Search-005 - Validate View Document***")
        self.logger.info("*****Login Successful****")
        self.logger.info("**** Full Text Search testing *****")
        self.navigator = FullTextSearch(self.driver)
        self.navigator.clickOnFullTextSearchMenu()
        self.logger.info("Full Text Search menu was clicked")
        time.sleep(2)
        #self.navigator.clickOnClientListing()
        search = self.driver.find_element(By.XPATH, "//*[@id='txtFTSSearch']")
        search.send_keys("Countries")
        self.navigator.clickOnSearch()
        time.sleep(2)
        self.navigator.clickOnBasicFilters()
        time.sleep(2)
        self.navigator.deselectArbitration()
        time.sleep(2)
        self.navigator.deselectDispute()
        time.sleep(2)
        self.navigator.submitSearch()
        time.sleep(2)
        tabText = self.driver.find_element(By.XPATH, "//div[@class='tabs__list']//a[1]").text
        print(tabText)
        #if tabText == "Treaty or Rules":
        viewDocument = self.driver.find_element(By.XPATH, "(//div[@class='document__footer-right']//a)[1]")
        self.driver.execute_script("arguments[0].click();", viewDocument)
        self.logger.info("Clicked on View Document")
        parent_handle = self.driver.current_window_handle
        all_handles = self.driver.window_handles
        print(all_handles)
        for handle in all_handles:
            if handle != parent_handle:
                self.driver.switch_to.window(handle)
                time.sleep(2)
                self.driver.close()
        self.driver.switch_to.window(parent_handle)
        time.sleep(2)

    #@pytest.mark.skip(reason="None")
    def test_AllWords(self):
        self.logger.info("****TestCase Full Text Search-006 - Validate All Words***")
        self.logger.info("*****Login Successful****")
        self.logger.info("**** Full Text Search testing *****")
        self.navigator = FullTextSearch(self.driver)
        self.navigator.clickOnFullTextSearchMenu()
        self.logger.info("Full Text Search menu was clicked")
        time.sleep(2)
        # self.navigator.clickOnClientListing()
        search = self.driver.find_element(By.XPATH, "//*[@id='txtFTSSearch']")
        search.send_keys("test")
        self.navigator.clickAllWordsOption()
        time.sleep(1)
        self.navigator.clickOnSearch()
        time.sleep(3)
        matchesFound = self.driver.find_element(By.XPATH,
                                                "//*[@id='page-content']/div/div[1]/div[5]/div[3]/div/div[1]/p/strong").text
        searchTextContaining = self.driver.find_element(By.XPATH, "//*[@id='containingCount']").text
        print(matchesFound + searchTextContaining)
        self.logger.info(matchesFound + searchTextContaining)

    #@pytest.mark.skip(reason="None")
    def test_AnyWords(self):
        self.logger.info("****TestCase Full Text Search-007 - Validate Any Words***")
        self.logger.info("*****Login Successful****")
        self.logger.info("**** Full Text Search testing *****")
        self.navigator = FullTextSearch(self.driver)
        self.navigator.clickOnFullTextSearchMenu()
        self.logger.info("Full Text Search menu was clicked")
        time.sleep(2)
        # self.navigator.clickOnClientListing()
        search = self.driver.find_element(By.XPATH, "//*[@id='txtFTSSearch']")
        search.send_keys("test")
        self.navigator.clickAnyWordsOption()
        time.sleep(1)
        self.navigator.clickOnSearch()
        time.sleep(3)
        matchesFound = self.driver.find_element(By.XPATH,
                                                "//*[@id='page-content']/div/div[1]/div[5]/div[3]/div/div[1]/p/strong").text
        searchTextContaining = self.driver.find_element(By.XPATH, "//*[@id='containingCount']").text
        print(matchesFound + searchTextContaining)
        self.logger.info(matchesFound + searchTextContaining)

    #@pytest.mark.skip(reason="None")
    def test_Boolean(self):
        self.logger.info("****TestCase Full Text Search-008 - Validate Boolean***")
        self.logger.info("*****Login Successful****")
        self.logger.info("**** Full Text Search testing *****")
        self.navigator = FullTextSearch(self.driver)
        self.navigator.clickOnFullTextSearchMenu()
        self.logger.info("Full Text Search menu was clicked")
        time.sleep(2)
        # self.navigator.clickOnClientListing()
        search = self.driver.find_element(By.XPATH, "//*[@id='txtFTSSearch']")
        search.send_keys("test")
        booleanOption = self.driver.find_element(By.XPATH,
                                                 "//*[@id='StaticFilters']/div[1]/div[1]/fieldset/label[3]/span/i").is_selected()
        self.logger.info(booleanOption)
        self.logger.info("Boolean option is selected by default")
        time.sleep(1)
        self.navigator.clickOnSearch()
        time.sleep(3)
        matchesFound = self.driver.find_element(By.XPATH,
                                                "//*[@id='page-content']/div/div[1]/div[5]/div[3]/div/div[1]/p/strong").text
        searchTextContaining = self.driver.find_element(By.XPATH, "//*[@id='containingCount']").text
        print(matchesFound + searchTextContaining)
        self.logger.info(matchesFound + searchTextContaining)

    #@pytest.mark.skip(reason="None")
    def test_DefaultliguisticAids(self):
        self.logger.info("****TestCase Full Text Search-009 - Validate default selection Linguistic Aids ***")
        self.logger.info("*****Login Successful****")
        self.logger.info("**** Full Text Search testing *****")
        self.navigator = FullTextSearch(self.driver)
        self.navigator.clickOnFullTextSearchMenu()
        self.logger.info("Full Text Search menu was clicked")
        time.sleep(2)
        # self.navigator.clickOnClientListing()
        time.sleep(2)
        stemmingChecked = self.driver.find_element(By.XPATH, "//*[@id='chkStemming']").is_selected()
        self.logger.info(stemmingChecked)
        fuzzyTypechecked = self.driver.find_element(By.XPATH, "//*[@id='chkFuzzyTypo']").is_selected()
        self.logger.info(fuzzyTypechecked)
        synonymsChecked = self.driver.find_element(By.XPATH, "//*[@id='chkSynonyms']")
        self.logger.info(synonymsChecked)
        amountFuzzyTypo = self.driver.find_element(By.XPATH, "//*[@id='fuzzy-typo']")
        amountTypo = amountFuzzyTypo.get_attribute('value')
        self.logger.info(amountTypo)

    #@pytest.mark.skip(reason="None")
    def test_BasicFilters(self):
        self.logger.info("****TestCase Full Text Search-010 - Validate Basic Filters Language and Dispute Dates ***")
        self.logger.info("*****Login Successful****")
        self.logger.info("**** Full Text Search testing *****")
        self.navigator = FullTextSearch(self.driver)
        self.navigator.clickOnFullTextSearchMenu()
        self.logger.info("Full Text Search menu was clicked")
        time.sleep(2)
        # self.navigator.clickOnClientListing()
        time.sleep(2)
        self.navigator.clickOnLanguage()
        time.sleep(3)
        searchLanguage = self.driver.find_elements(By.XPATH, "//*[@id='select2-select-language-results']//li")
        print(len(searchLanguage))
        for results in searchLanguage:
            print(results.text)
            self.logger.info(results.text)
            if results.text == "English":
                print("record found")
                results.click()
                time.sleep(4)
                break
        calendarpicker = self.driver.find_element(By.XPATH, "//*[@id='datepicker-from']")
        calendarpicker.click()
        calendarMonth = self.driver.find_elements(By.XPATH,
                                                  "/html/body/div[6]/div[2]/div[1]/table/thead/tr[1]/th[2]/select[1]//option")
        print(len(calendarMonth))
        for months in calendarMonth:
            print(months.text)
            self.logger.info(months.text)
            if months.text == "Jan":
                print("Month found")
                months.click()
                time.sleep(2)
                break
        calendarYear = self.driver.find_elements(By.XPATH,
                                                 "/html/body/div[6]/div[2]/div[1]/table/thead/tr[1]/th[2]/select[2]//option")
        print(len(calendarYear))
        for years in calendarYear:
            print(years.text)
            self.logger.info(years.text)
            if years.text == "2021":
                print("Year found")
                years.click()
                time.sleep(2)
                break
        calendarDate = self.driver.find_elements(By.XPATH, "/html/body/div[6]/div[2]/div[1]/table/tbody//tr//td")
        print(len(calendarDate))
        for date in calendarDate:
            print(date.text)
            self.logger.info(date.text)
            if date.text == "2":
                print("date found")
                date.click()
                time.sleep(2)
                break
        calendarToPicker = self.driver.find_element(By.XPATH, "//*[@id='datepicker-to']")
        calendarToPicker.click()
        calendarMonth = self.driver.find_elements(By.XPATH,
                                                  "/html/body/div[7]/div[2]/div[1]/table/thead/tr[1]/th[2]/select[1]//option")
        print(len(calendarMonth))
        for months in calendarMonth:
            print(months.text)
            self.logger.info(months.text)
            if months.text == "Dec":
                print("Month found")
                months.click()
                time.sleep(2)
                break
        calendarYear = self.driver.find_elements(By.XPATH,
                                                 "/html/body/div[7]/div[2]/div[1]/table/thead/tr[1]/th[2]/select[2]//option")
        print(len(calendarYear))
        for years in calendarYear:
            print(years.text)
            self.logger.info(years.text)
            if years.text == "2022":
                print("Year found")
                years.click()
                time.sleep(2)
                break
        calendarDate = self.driver.find_elements(By.XPATH, "/html/body/div[7]/div[2]/div[1]/table/tbody//tr//td")
        print(len(calendarDate))
        for date in calendarDate:
            print(date.text)
            self.logger.info(date.text)
            if date.text == "28":
                print("date found")
                date.click()
                time.sleep(2)
                break
        search = self.driver.find_element(By.XPATH, "//*[@id='txtFTSSearch']")
        search.send_keys("Interests")
        self.navigator.clickOnSearch()
        languageValue = self.driver.find_elements(By.XPATH, "//div[2][@class='document__meta-value']//strong")
        for results in languageValue:
            print(results.text)
            self.logger.info(results.text)
            self.logger.info(results.text)
            if results.text == "English":
                print("record found")
                results.click()
                time.sleep(4)
                break

    #@pytest.mark.skip(reason="None")
    def test_FilterDisputeDocuments(self):
        self.logger.info("****TestCase Full Text Search-011 - Validate Filter Dispute Documents ***")
        self.logger.info("*****Login Successful****")
        self.logger.info("**** Full Text Search testing *****")
        self.navigator = FullTextSearch(self.driver)
        self.navigator.clickOnFullTextSearchMenu()
        self.logger.info("Full Text Search menu was clicked")
        time.sleep(2)
        # self.navigator.clickOnClientListing()
        time.sleep(2)
        self.navigator.clickOnRespondentState()
        time.sleep(3)
        stateList = self.driver.find_elements(By.XPATH, "/html/body/span/span/span//ul//li")
        print(len(stateList))
        time.sleep(2)
        for results in stateList:
            print(results.text)
            self.logger.info(results.text)
            if results.text == "United States":
                print("State found")
                results.click()
                time.sleep(2)
                break
        self.navigator.clickOnApplicableInstruments()
        time.sleep(2)
        applicableInstruments = self.driver.find_elements(By.XPATH, "/html/body/span/span/span//ul//li")
        print(len(applicableInstruments))
        time.sleep(2)
        for results in applicableInstruments:
            print(results.text)
            self.logger.info(results.text)
            if results.text == "US-Vietnam Trade Relations Agreement (2000)":
                print("Applicable Instrument found")
                results.click()
                time.sleep(2)
                break
        self.navigator.clickOnArbitrationRules()
        time.sleep(2)
        arbitrationRules = self.driver.find_elements(By.XPATH, "/html/body/span/span/span//ul//li")
        print(len(arbitrationRules))
        time.sleep(2)
        for results in arbitrationRules:
            print(results.text)
            self.logger.info(results.text)
            if results.text == "ICC Rules of Arbitration (1998) (citation)":
                print("Arbitration Rules found")
                self.logger.info(results.text)
                results.click()
                time.sleep(2)
                break
        search = self.driver.find_element(By.XPATH, "//*[@id='txtFTSSearch']")
        search.send_keys("Interests")
        self.navigator.clickOnSearch()
        basicFilters = self.driver.find_element(By.XPATH, "//*[@id='page-content']/div/div[1]/div[5]/div[2]/div/button")
        basicFilters.click()
        self.logger.info("Clicked on Basic Filters")
        respondentStateCheck = self.driver.find_element(By.XPATH,
                                                        "//*[@id='search__filters']/div[1]/div[3]/div[1]/div/span/span[1]/span/ul/li[1]")
        print(respondentStateCheck.text)
        self.logger.info(respondentStateCheck.text)
        applicableTreatyCheck = self.driver.find_element(By.XPATH,
                                                         "//*[@id='search__filters']/div[1]/div[3]/div[2]/div/span/span[1]/span/ul/li[1]")
        print(applicableTreatyCheck.text)
        self.logger.info(applicableTreatyCheck.text)
        arbitrationRules = self.driver.find_element(By.XPATH,
                                                    "//*[@id='search__filters']/div[1]/div[3]/div[3]/div/span/span[1]/span/ul/li[1]")
        print(arbitrationRules.text)
        self.logger.info(arbitrationRules.text)
        closeBasicFiltersPopup = self.driver.find_element(By.XPATH, "//*[@id='search__filters']/button")
        closeBasicFiltersPopup.click()
        self.logger.info("Basic Filters popup closed")

    #@pytest.mark.skip(reason="None")
    def test_FilterByResearchTools(self):
        self.logger.info("****TestCase Full Text Search-013 - Validate Filter By Research Tools ***")
        self.logger.info("*****Login Successful****")
        self.logger.info("**** Full Text Search testing *****")
        self.navigator = FullTextSearch(self.driver)
        self.navigator.clickOnFullTextSearchMenu()
        self.logger.info("Full Text Search menu was clicked")
        time.sleep(2)
        # self.navigator.clickOnClientListing()
        time.sleep(2)
        testFind = self.driver.find_element(By.XPATH, "//*[@id='txtFTSSearch']")
        testFind.click()
        testFind.send_keys("test")
        self.navigator.clickOnSubject()
        self.logger.info("Clicked on Subject")
        time.sleep(2)
        subject = self.driver.find_elements(By.XPATH, "/html/body/span/span/span//ul//li")
        print(len(subject))
        time.sleep(2)
        for results in subject:
            print(results.text)
            self.logger.info(results.text)
            if results.text == "\"Clean hands\" doctrine":
                print("Subject found")
                self.logger.info(results.text)
                results.click()
                time.sleep(2)
                break
        self.navigator.clickOnTreatyInstrument()
        self.logger.info("Clicked on TreatyInstrument")
        time.sleep(2)
        treaty = self.driver.find_elements(By.XPATH, "/html/body/span/span/span//ul//li")
        print(len(treaty))
        time.sleep(2)
        for results in treaty:
            print(results.text)
            self.logger.info(results.text)
            if results.text == "Albania - United States BIT (1995) (excerpts)":
                print("Subject found")
                self.logger.info(results.text)
                results.click()
                time.sleep(2)
                break
        time.sleep(2)
        self.navigator.clickOnProvision()
        self.logger.info("Clicked on Provision")
        time.sleep(2)
        provision = self.driver.find_elements(By.XPATH, "/html/body/span/span/span//ul//li")
        time.sleep(2)
        # print(len(provision))
        time.sleep(2)
        for results in provision:
            print(results.text)
            self.logger.info(results.text)
            if results.text == "Article II(3)(a)":
                print("Provision found")
                self.logger.info(results.text)
                results.click()
                time.sleep(2)
                break
        search = self.driver.find_element(By.XPATH, "//*[@id='txtFTSSearch']")
        search.send_keys("Interests")
        self.navigator.clickOnSearch()
        basicFilters = self.driver.find_element(By.XPATH, "//*[@id='page-content']/div/div[1]/div[5]/div[2]/div/button")
        basicFilters.click()
        self.logger.info("Clicked on Basic Filters")
        subjectCheck = self.driver.find_element(By.XPATH,
                                                "//*[@id='search__filters']/div[1]/div[3]/div[4]/div[1]/div/div/span/span[1]/span")
        self.logger.info(subjectCheck.text)
        treatyInstrumentCheck = self.driver.find_element(By.XPATH,
                                                         "//*[@id='search__filters']/div[1]/div[3]/div[4]/div[1]/div/div/span/span[1]/span")
        self.logger.info(treatyInstrumentCheck)
        provisionCheck = self.driver.find_element(By.XPATH,
                                                  "//*[@id='search__filters']/div[1]/div[3]/div[4]/div[3]/div/div/span/span[1]/span/ul/li[2]/input")
        self.logger.info(provisionCheck.text)
        closeBasicFiltersPopup = self.driver.find_element(By.XPATH, "//*[@id='search__filters']/button")
        closeBasicFiltersPopup.click()
        self.logger.info("Basic Filters popup closed")
        found = self.driver.find_element(By.XPATH,
                                         "//*[@id='page-content']/div/div[1]/div[5]/div[3]/div/div[1]/p/strong")
        containing = self.driver.find_element(By.XPATH, "//*[@id='containingCount']")
        self.logger.info(found.text + containing.text)


    #@pytest.mark.skip(reason="None")
    def test_FullCaseAnalysis(self):
        self.logger.info("****TestCase Full Text Search-004 - Validate Full Case Analysis ***")
        self.logger.info("*****Login Successful****")
        self.logger.info("**** Full Text Search testing *****")
        self.navigator = FullTextSearch(self.driver)
        self.navigator.clickOnFullTextSearchMenu()
        self.logger.info("Full Text Search menu was clicked")
        time.sleep(2)
        #self.navigator.clickOnClientListing()
        search = self.driver.find_element(By.XPATH, "//*[@id='txtFTSSearch']")
        search.send_keys("Countries")
        self.navigator.clickOnSearch()
        time.sleep(3)
        tabText = self.driver.find_element(By.XPATH, "//div[@class='tabs__list']//a[1]").text
        print(tabText)
        # if tabText == "Dispute Document":
        # dispute = self.driver.find_element(By.XPATH, "(//div[@class='document__footer-right']//a)[1]")
        # self.driver.execute_script("arguments[0].scrollIntoView();", dispute)
        # self.driver.execute_script("arguments[0].click();", dispute)
        time.sleep(2)
        fullCase = self.driver.find_element(By.XPATH, "(//div[@class='document__footer-right']//a)[1]")
        self.driver.execute_script("arguments[0].click();", fullCase)
        self.logger.info("Clicked on Full Case Analysis")
        parent_handle = self.driver.current_window_handle
        all_handles = self.driver.window_handles
        print(all_handles)
        for handle in all_handles:
            if handle != parent_handle:
                self.driver.switch_to.window(handle)
                time.sleep(2)
                self.logger.info("Opened Full Case Analysis")
                self.driver.close()
        self.driver.switch_to.window(parent_handle)
        self.driver.quit()

