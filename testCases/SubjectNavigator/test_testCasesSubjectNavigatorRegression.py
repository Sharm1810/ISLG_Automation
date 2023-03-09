import time
from urllib.request import Request, urlopen

import pytest
import softest
from selenium.webdriver.common.by import By

from pageObjects.ArticleCitator import ArticleCitator
from pageObjects.JurisprudenceCitator import JurisprudenceCitator
from pageObjects.PublicationCitator import PublicationCitator
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
class Test_testCasesSubjectNavigatorRegression(softest.TestCase):
    logger = LogGen.loggen()

    # @pytest.mark.skip(reason="None")
    def test_crossReferences(self):
        self.logger.info("****TestCase SN-001 - Validate Cross References***")
        self.logger.info("*****Login Successful****")
        self.logger.info("**** Subject Navigator testing *****")
        self.navigator = SubjectNavigator(self.driver)
        self.navigator.clickOnSubjectNavigatormenu()
        time.sleep(2)
        # self.navigator.clickOnClientListing()
        self.logger.info("Subject Navigator menu is available")
        time.sleep(2)
        self.navigator.expandBranch()
        time.sleep(2)
        self.logger.info("Clicked on Expand branch associated with the first Branch")
        self.navigator.clickOnFirstLinkMainBranch()
        time.sleep(2)
        # check if Cross References Title is present
        crossRef = self.navigator.crossReferences()
        print(crossRef)
        clickOnFirstLink = self.driver.find_element(By.XPATH, "(//div[@class='card-list']//ul//li//a)[1]")
        if crossRef == "cross references":
            # click on the first link
            self.driver.execute_script("arguments[0].click();", clickOnFirstLink)
            time.sleep(2)
        else:
            self.logger.info("No Cross References are displayed")
        time.sleep(2)

    #@pytest.mark.skip(reason="None")
    def test_FullCaseAnalysis(self):
        self.logger.info("****TestCase SN-002 - Validate Full Case Analysis- Cross References***")
        self.logger.info("*****Login Successful****")
        self.logger.info("**** Subject Navigator testing *****")
        self.navigator = SubjectNavigator(self.driver)
        self.navigator.clickOnSubjectNavigatormenu()
        time.sleep(2)
        # self.navigator.clickOnClientListing()
        self.logger.info("Subject Navigator menu is available")
        time.sleep(2)
        self.navigator.expandBranch()
        time.sleep(2)
        self.logger.info("Clicked on Expand branch associated with the first Branch")
        the_links = self.driver.find_elements_by_link_text('Expand all')
        for element in the_links:
            self.driver.execute_script("arguments[0].click();", element)
            time.sleep(5)
        # full_caseLink = self.driver.find_element(By.TAG_NAME, "em")
        # emText= full_caseLink.text
        # print(emText)
        # Click on Link -InnerCardHeader
        self.navigator.clickOnInnerCardHeader()
        time.sleep(2)
        self.logger.info("Clicked on InnerCard Header Link")
        self.navigator.clickOnInnerFirstLink()
        time.sleep(2)
        self.logger.info("Clicked on first link to view the Full Case Analysis")
        time.sleep(2)
        self.navigator.clickOnFullCaseAnalysis()
        time.sleep(2)
        self.logger.info("Clicked on Full Case Analysis")
        time.sleep(2)
        parent_handle = self.driver.current_window_handle
        print(parent_handle)
        time.sleep(2)
        all_handles = self.driver.window_handles
        print(all_handles)
        for handle in all_handles:
            if handle != parent_handle:
                self.driver.switch_to.window(handle)
                self.driver.close()
        time.sleep(2)
        self.driver.switch_to.window(parent_handle)

    #@pytest.mark.skip(reason="None")
    def test_SubjectNavigatorLink(self):
        self.logger.info("****TestCase SN-003 - Validate Full Case Analysis- Subject Navigator***")
        self.logger.info("*****Login Successful****")
        self.logger.info("**** Subject Navigator testing *****")
        self.navigator = SubjectNavigator(self.driver)
        self.navigator.clickOnSubjectNavigatormenu()
        time.sleep(2)
        # self.navigator.clickOnClientListing()
        self.logger.info("Subject Navigator menu is available")
        time.sleep(2)
        self.navigator.expandBranch()
        time.sleep(2)
        self.logger.info("Clicked on Expand branch associated with the first Branch")
        the_links = self.driver.find_elements_by_link_text('Expand all')
        for element in the_links:
            self.driver.execute_script("arguments[0].click();", element)
            time.sleep(5)
        self.navigator.clickOnInnerCardHeader()
        time.sleep(2)
        self.logger.info("Clicked on InnerCard Header Link")
        self.navigator.clickOnInnerFirstLink()
        time.sleep(2)
        self.logger.info("Clicked on first link to view the Full Case Analysis")
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
                viewLink = self.driver.find_element(By.XPATH, "//div[@class='document__sidebar']//div[3]//button")
                self.driver.execute_script("arguments[0].click();", viewLink)
                time.sleep(2)
                self.logger.info("Clicked on Link")
                self.navigator.clickOnViewSubjectNavigator()
                time.sleep(2)
                self.logger.info("Clicked on View Subject Navigator Link")
                self.driver.switch_to.window(self.driver.window_handles[2])
                self.driver.close()
                time.sleep(3)
                self.driver.switch_to.window(handle)
                time.sleep(3)
                self.driver.switch_to.window(self.driver.window_handles[1])
                self.driver.close()
                self.driver.switch_to.window(self.driver.window_handles[0])
        self.driver.switch_to.window(parent_handle)
        time.sleep(2)

    #@pytest.mark.skip(reason="None")
    def test_copyCitation(self):
        self.logger.info("****TestCase SN-004 - Validate Full Case Analysis- Copy Citator***")
        self.logger.info("*****Login Successful****")
        self.logger.info("**** Subject Navigator testing *****")
        self.navigator = SubjectNavigator(self.driver)
        self.navigator.clickOnSubjectNavigatormenu()
        time.sleep(2)
        # self.navigator.clickOnClientListing()
        self.logger.info("Subject Navigator menu is available")
        time.sleep(2)
        self.navigator.expandBranch()
        time.sleep(2)
        self.logger.info("Clicked on Expand branch associated with the first Branch")
        the_links = self.driver.find_elements_by_link_text('Expand all')
        for element in the_links:
            self.driver.execute_script("arguments[0].click();", element)
            time.sleep(5)
        self.navigator.clickOnInnerCardHeader()
        time.sleep(2)
        self.logger.info("Clicked on InnerCard Header Link")
        self.navigator.clickOnInnerFirstLink()
        time.sleep(2)
        self.logger.info("Clicked on first link to view the Full Case Analysis")
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
        self.driver.switch_to.window(parent_handle)
        time.sleep(2)

    #@pytest.mark.skip(reason="None")
    def test_viewPDF(self):
        self.logger.info("****TestCase SN-005 - Validate Full Case Analysis- View PDF***")
        self.logger.info("*****Login Successful****")
        self.logger.info("**** Subject Navigator testing *****")
        self.navigator = SubjectNavigator(self.driver)
        self.navigator.clickOnSubjectNavigatormenu()
        time.sleep(2)
        # self.navigator.clickOnClientListing()
        self.logger.info("Subject Navigator menu is available")
        time.sleep(2)
        self.navigator.expandBranch()
        time.sleep(2)
        self.logger.info("Clicked on Expand branch associated with the first Branch")
        the_links = self.driver.find_elements_by_link_text('Expand all')
        for element in the_links:
            self.driver.execute_script("arguments[0].click();", element)
            time.sleep(5)
        self.navigator.clickOnInnerCardHeader()
        time.sleep(2)
        self.logger.info("Clicked on InnerCard Header Link")
        self.navigator.clickOnInnerFirstLink()
        time.sleep(2)
        self.logger.info("Clicked on first link to view the Full Case Analysis")
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
                self.navigator.clickOnViewPDF()
                time.sleep(2)
                self.logger.info("Clicked on Original PDF")
                self.driver.close()
        self.driver.switch_to.window(parent_handle)
        time.sleep(2)

    #@pytest.mark.skip(reason="None")
    def test_downloadDocument(self):
        self.logger.info("****TestCase SN-006 - Validate Full Case Analysis- Download Document***")
        self.logger.info("*****Login Successful****")
        self.logger.info("**** Subject Navigator testing *****")
        self.navigator = SubjectNavigator(self.driver)
        self.navigator.clickOnSubjectNavigatormenu()
        time.sleep(2)
        # self.navigator.clickOnClientListing()
        self.logger.info("Subject Navigator menu is available")
        time.sleep(2)
        self.navigator.expandBranch()
        time.sleep(2)
        self.logger.info("Clicked on Expand branch associated with the first Branch")
        the_links = self.driver.find_elements_by_link_text('Expand all')
        for element in the_links:
            self.driver.execute_script("arguments[0].click();", element)
            time.sleep(5)
        self.navigator.clickOnInnerCardHeader()
        time.sleep(2)
        self.logger.info("Clicked on InnerCard Header Link")
        self.navigator.clickOnInnerFirstLink()
        time.sleep(2)
        self.logger.info("Clicked on first link to view the Full Case Analysis")
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
                time.sleep(3)
                self.logger.info("Clicked on Download Document")
                self.driver.close()
        self.driver.switch_to.window(parent_handle)
        time.sleep(2)

    #@pytest.mark.skip(reason="None")
    def test_documentComparison(self):
        self.logger.info("****TestCase SN-007 - Validate Full Case Analysis- Add to Document Comparison***")
        self.logger.info("*****Login Successful****")
        self.logger.info("**** Subject Navigator testing *****")
        self.navigator = SubjectNavigator(self.driver)
        self.navigator.clickOnSubjectNavigatormenu()
        time.sleep(2)
        # self.navigator.clickOnClientListing()
        self.logger.info("Subject Navigator menu is available")
        time.sleep(2)
        self.navigator.expandBranch()
        time.sleep(2)
        self.logger.info("Clicked on Expand branch associated with the first Branch")
        the_links = self.driver.find_elements_by_link_text('Expand all')
        for element in the_links:
            self.driver.execute_script("arguments[0].click();", element)
            time.sleep(5)
        self.navigator.clickOnInnerCardHeader()
        time.sleep(2)
        self.logger.info("Clicked on InnerCard Header Link")
        self.navigator.clickOnInnerFirstLink()
        time.sleep(2)
        self.logger.info("Clicked on first link to view the Full Case Analysis")
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
                self.navigator.clickOnDocumentComparison()
                time.sleep(3)
                self.logger.info("Clicked on Document Comparison")
                self.navigator.selectDocumentComparisonOption()
                time.sleep(2)
                self.logger.info("Selected the first document comparison option")
                self.navigator.clickOnAddDocumentCompare()
                time.sleep(2)
                self.driver.close()
        self.driver.switch_to.window(parent_handle)
        time.sleep(2)

    #@pytest.mark.skip(reason="None")
    def test_researchNotepad(self):
        self.logger.info("****TestCase SN-008 - Validate Full Case Analysis- Add to Research Notepad***")
        self.logger.info("*****Login Successful****")
        self.logger.info("**** Subject Navigator testing *****")
        self.navigator = SubjectNavigator(self.driver)
        self.navigator.clickOnSubjectNavigatormenu()
        time.sleep(2)
        # self.navigator.clickOnClientListing()
        self.logger.info("Subject Navigator menu is available")
        time.sleep(2)
        self.navigator.expandBranch()
        time.sleep(2)
        self.logger.info("Clicked on Expand branch associated with the first Branch")
        the_links = self.driver.find_elements_by_link_text('Expand all')
        for element in the_links:
            self.driver.execute_script("arguments[0].click();", element)
            time.sleep(5)
        self.navigator.clickOnInnerCardHeader()
        time.sleep(2)
        self.logger.info("Clicked on InnerCard Header Link")
        self.navigator.clickOnInnerFirstLink()
        time.sleep(2)
        self.logger.info("Clicked on first link to view the Full Case Analysis")
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
                self.navigator.clickOnResearch()
                self.logger.info("Full Case Analysis - Clicked on Research Notepad")
                time.sleep(2)
                self.navigator.selectResearchOption()
                self.logger.info("Selected Research Option")
                time.sleep(3)
                self.navigator.clickOnAddNotepad()
                self.logger.info("Clicked on Add to Notepad")
                time.sleep(3)
                self.driver.close()
        self.driver.switch_to.window(parent_handle)
        time.sleep(2)
