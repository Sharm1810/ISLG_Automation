import sys
from telnetlib import EC

import clipboard
import pytest
import time
import json




import softest
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select

from pageObjects.ArticleCitator import ArticleCitator
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
class Test_testCasesArticleRegression(softest.TestCase):
    logger = LogGen.loggen()

    #@pytest.mark.skip(reason="None")
    def test_metaDataLinks(self):
        self.logger.info("****TestCase AC-001 - Verify Navigation links***")
        self.logger.info("*****Login Successful****")
        self.logger.info("**** Article Citator testing *****")
        self.navigator = ArticleCitator(self.driver)
        #self.navigator = ArticleCitatorExtended(self.driver)
        self.navigator.clickOnArticleCitatormenu()
        time.sleep(2)
        #self.navigator.clickOnClientListing()
        self.logger.info("Article Citator menu is available")
        time.sleep(2)
        self.driver.execute_script("window.scrollBy(0,500)", "")
        time.sleep(2)
        # Click on the first branch to expand
        self.navigator.clickOnexpandBranch()
        self.logger.info("First Branch is expanded")
        time.sleep(2)
        self.navigator.clickOnSeeAll()
        time.sleep(2)
        self.navigator.clickOnFullCase()
        time.sleep(2)
        parent_handle = self.driver.current_window_handle
        print(parent_handle)
        time.sleep(2)
        all_handles = self.driver.window_handles
        print(all_handles)
        for handle in all_handles:
            if handle != parent_handle:
                self.driver.switch_to.window(handle)
                time.sleep(2)
                getext = self.driver.find_element(By.XPATH, "//*[@id='document-view']/div[1]/p/span[2]/strong")
                text = getext.get_attribute('text')
                self.logger.info(text)
                time.sleep(3)
                # assert text in text
                # time.sleep(1)
                # getLinktext = self.driver.find_element(By.XPATH, "//*[@id='document-view']/div[1]/p/span[3]/strong/a")
                # linktext = getLinktext.get_attribute('text')
                # self.logger.info(linktext)
                # time.sleep(3)
                # assert linktext in linktext
                time.sleep(1)
                self.driver.close()
        self.driver.switch_to.window(parent_handle)

    #@pytest.mark.skip(reason="None")
    def test_AdddocumentComparison(self):
        self.logger.info("****TestCase AC-002 - Verify Add to Document Comparison***")
        self.logger.info("*****Login Successful****")
        self.logger.info("**** Article Citator testing *****")
        self.navigator = ArticleCitator(self.driver)
        #self.navigator = ArticleCitatorExtended(self.driver)
        self.navigator.clickOnArticleCitatormenu()
        time.sleep(2)
        #self.navigator.clickOnClientListing()
        self.logger.info("Article Citator menu is available")
        time.sleep(2)
        self.driver.execute_script("window.scrollBy(0,500)", "")
        time.sleep(2)
        # Click on the first branch to expand
        self.navigator.clickOnexpandBranch()
        self.logger.info("First Branch is expanded")
        time.sleep(2)
        self.navigator.clickOnSeeAll()
        time.sleep(2)
        self.navigator.clickOnFullCase()
        time.sleep(2)
        parent_handle = self.driver.current_window_handle
        print(parent_handle)
        time.sleep(2)
        all_handles = self.driver.window_handles
        print(all_handles)
        for handle in all_handles:
            if handle != parent_handle:
                self.driver.switch_to.window(handle)
                time.sleep(3)
                self.navigator.addToDocumentComparison()
                # clickdocument = self.driver.find_element(By.XPATH, "//button[@title='Add to Document Comparison']")
                # self.driver.execute_script("arguments[0].click();", clickdocument)
                time.sleep(3)
                self.logger.info("Full Case Analysis - Clicked on Add to Document Comparison")
                self.navigator.selectDocumentComparisonOption()
                time.sleep(2)
                self.logger.info("Selected the first document comparison option")
                self.navigator.clickOnAddDocumentCompare()
                time.sleep(2)
                self.logger.info("Added to Document Comparison")
                self.driver.close()
        self.driver.switch_to.window(parent_handle)

    #@pytest.mark.skip(reason="None")
    def test_CanceldocumentComparison(self):
        self.logger.info("****TestCase AC-003 - Verify Cancel Add to Document Comparison***")
        self.logger.info("*****Login Successful****")
        self.logger.info("**** Article Citator testing *****")
        self.navigator = ArticleCitator(self.driver)
        self.navigator.clickOnArticleCitatormenu()
        time.sleep(2)
        #self.navigator.clickOnClientListing()
        self.logger.info("Article Citator menu is available")
        time.sleep(2)
        self.driver.execute_script("window.scrollBy(0,500)", "")
        time.sleep(2)
        # Click on the first branch to expand
        self.navigator.clickOnexpandBranch()
        self.logger.info("First Branch is expanded")
        time.sleep(2)
        self.navigator.clickOnSeeAll()
        time.sleep(2)
        self.navigator.clickOnFullCase()
        time.sleep(2)
        parent_handle = self.driver.current_window_handle
        print(parent_handle)
        time.sleep(2)
        all_handles = self.driver.window_handles
        print(all_handles)
        for handle in all_handles:
            if handle != parent_handle:
                self.driver.switch_to.window(handle)
                time.sleep(3)
                self.navigator.addToDocumentComparison()
                # clickdocument = self.driver.find_element(By.XPATH, "//button[@title='Add to Document Comparison']")
                # self.driver.execute_script("arguments[0].click();", clickdocument)
                time.sleep(3)
                self.logger.info("Full Case Analysis - Clicked on Add to Document Comparison")
                self.navigator.selectDocumentComparisonOption()
                time.sleep(2)
                self.logger.info("Selected the first document comparison option")
                self.navigator.clickOnCancelCompare()
                time.sleep(2)
                self.logger.info("Clicked on Cancel and Closed the Add to Document Comparison screen")
                self.driver.close()
        self.driver.switch_to.window(parent_handle)



    #@pytest.mark.skip(reason="None")
    def test_SeeAllGroups(self):
        self.logger.info("****TestCase AC-004 - Verify See All groups- Add to Document Comparison***")
        self.logger.info("*****Login Successful****")
        self.logger.info("**** Article Citator testing *****")
        self.navigator = ArticleCitator(self.driver)
        self.navigator.clickOnArticleCitatormenu()
        time.sleep(2)
        # self.navigator.clickOnClientListing()
        self.logger.info("Article Citator menu is available")
        time.sleep(2)
        self.driver.execute_script("window.scrollBy(0,500)", "")
        time.sleep(2)
        # Click on the first branch to expand
        self.navigator.clickOnexpandBranch()
        self.logger.info("First Branch is expanded")
        time.sleep(2)
        self.navigator.clickOnSeeAll()
        time.sleep(2)
        self.navigator.clickOnFullCase()
        time.sleep(2)
        parent_handle = self.driver.current_window_handle
        print(parent_handle)
        time.sleep(2)
        all_handles = self.driver.window_handles
        print(all_handles)
        for handle in all_handles:
            if handle != parent_handle:
                self.driver.switch_to.window(handle)
                time.sleep(3)
                self.navigator.addToDocumentComparison()
                time.sleep(3)
                self.logger.info("Full Case Analysis - Clicked on Add to Document Comparison")
                # self.navigator.clickOnSeeAllGroups()
                # self.logger.info("Clicked on See All Groups")
                # time.sleep(2)
                # for handle in all_handles:
                #     if handle != parent_handle:
                #         self.driver.switch_to.window(handle)
                #         time.sleep(2)
                #         title = self.driver.find_element(By.XPATH, "//*[@id='page-content']/div/div[1]/div/div/div[1]/h1")
                #         heading = title.get_attribute('text')
                #         self.logger.info(heading)
                #         time.sleep(2)
                #         self.driver.close()
                self.driver.close()
        self.driver.switch_to.window(parent_handle)


    #@pytest.mark.skip(reason="None")
    def test_Notepad(self):
        self.logger.info("****TestCase AC-005 - Verify Research Notepad- Add to ResearchNotepad***")
        self.logger.info("*****Login Successful****")
        self.logger.info("**** Article Citator testing *****")
        self.navigator = ArticleCitator(self.driver)
        self.navigator.clickOnArticleCitatormenu()
        time.sleep(2)
        # self.navigator.clickOnClientListing()
        self.logger.info("Article Citator menu is available")
        time.sleep(2)
        self.driver.execute_script("window.scrollBy(0,500)", "")
        time.sleep(2)
        # Click on the first branch to expand
        self.navigator.clickOnexpandBranch()
        self.logger.info("First Branch is expanded")
        time.sleep(2)
        self.navigator.clickOnSeeAll()
        time.sleep(2)
        self.navigator.clickOnFullCase()
        time.sleep(2)
        parent_handle = self.driver.current_window_handle
        print(parent_handle)
        time.sleep(2)
        all_handles = self.driver.window_handles
        print(all_handles)
        for handle in all_handles:
            if handle != parent_handle:
                self.driver.switch_to.window(handle)
                time.sleep(3)
                self.navigator.clickOnResearch()
                self.logger.info("Full Case Analysis - Clicked on Research Notepad")
                time.sleep(2)
                self.navigator.selectResearchOption()
                time.sleep(2)
                self.navigator.clickOnAddNotepad()
                # researchOption = self.driver.find_element(By.XPATH, "(//label[@class='form__radio']//input)[1]")
                # self.driver.execute_script("arguments[0].click();", researchOption)
                time.sleep(2)
                self.logger.info("Clicked on Add to Notepad")
                self.driver.close()
        self.driver.switch_to.window(parent_handle)

    #@pytest.mark.skip(reason="None")
    def test_SeeAllTopics(self):
        self.logger.info("****TestCase AC-006 - Verify Research Notepad- See All Topics***")
        self.logger.info("*****Login Successful****")
        self.logger.info("**** Article Citator testing *****")
        self.navigator = ArticleCitator(self.driver)
        self.navigator.clickOnArticleCitatormenu()
        time.sleep(2)
        # self.navigator.clickOnClientListing()
        self.logger.info("Article Citator menu is available")
        time.sleep(2)
        self.driver.execute_script("window.scrollBy(0,500)", "")
        time.sleep(2)
        # Click on the first branch to expand
        self.navigator.clickOnexpandBranch()
        self.logger.info("First Branch is expanded")
        time.sleep(2)
        self.navigator.clickOnSeeAll()
        time.sleep(2)
        self.navigator.clickOnFullCase()
        time.sleep(2)
        parent_handle = self.driver.current_window_handle
        print(parent_handle)
        time.sleep(2)
        all_handles = self.driver.window_handles
        print(all_handles)
        for handle in all_handles:
            if handle != parent_handle:
                self.driver.switch_to.window(handle)
                time.sleep(3)
                self.navigator.clickOnResearch()
                self.logger.info("Full Case Analysis - Clicked on Research Notepad")
                time.sleep(2)
                self.navigator.selectResearchOption()
                time.sleep(2)
                self.navigator.clickOnSeeAllTopics()
                time.sleep(2)
                title = self.driver.find_element(By.XPATH, "/html/head/title")
                print(title.text)
                self.driver.get('https://app.investorstatelawguide.com/ResearchNotepad')
                print(self.driver.title)
                assert 'Research Notepad' in self.driver.title
                self.logger.info(self.driver.title)
                time.sleep(2)
                self.driver.close()
                self.driver.switch_to.window(handle)
                #self.driver.switch_to.window(parent_handle)
                self.driver.close()
        self.driver.switch_to.window(parent_handle)
        time.sleep(2)
        self.navigator.clickOnArticleCitatormenu()
        time.sleep(2)

    @pytest.mark.skip(reason="None")
    def test_closeResearchNotepad(self):
        self.logger.info("****TestCase AC-007 - Verify Research Notepad- Close Research Notepad***")
        self.logger.info("*****Login Successful****")
        self.logger.info("**** Article Citator testing *****")
        self.navigator = ArticleCitator(self.driver)
        self.navigator.clickOnArticleCitatormenu()
        time.sleep(2)
        # self.navigator.clickOnClientListing()
        self.logger.info("Article Citator menu is available")
        time.sleep(2)
        self.driver.execute_script("window.scrollBy(0,500)", "")
        time.sleep(2)
        # Click on the first branch to expand
        self.navigator.clickOnexpandBranch()
        self.logger.info("First Branch is expanded")
        time.sleep(2)
        self.navigator.clickOnSeeAll()
        time.sleep(2)
        self.navigator.clickOnFullCase()
        time.sleep(2)
        parent_handle = self.driver.current_window_handle
        print(parent_handle)
        time.sleep(2)
        all_handles = self.driver.window_handles
        print(all_handles)
        for handle in all_handles:
            if handle != parent_handle:
                self.driver.switch_to.window(handle)
                time.sleep(3)
                self.navigator.clickOnResearch()
                self.logger.info("Full Case Analysis - Clicked on Research Notepad")
                time.sleep(2)
                self.navigator.selectResearchOption()
                # time.sleep(2)
                # self.navigator.clickOnCloseResearchNotepad()
                # time.sleep(1)
                # self.logger.info("Closed research Notepad popup")
                time.sleep(2)
                self.driver.close()
        self.driver.switch_to.window(parent_handle)



    @pytest.mark.skip(reason="None")
    def test_createResearchTopic(self):
        self.logger.info("****TestCase AC-008 - Verify Research Notepad- Create New Research Topic***")
        self.logger.info("*****Login Successful****")
        self.logger.info("**** Article Citator testing *****")
        self.navigator = ArticleCitator(self.driver)
        self.navigator.clickOnArticleCitatormenu()
        time.sleep(2)
        # self.navigator.clickOnClientListing()
        self.logger.info("Article Citator menu is available")
        time.sleep(2)
        self.driver.execute_script("window.scrollBy(0,500)", "")
        time.sleep(2)
        # Click on the first branch to expand
        self.navigator.clickOnexpandBranch()
        self.logger.info("First Branch is expanded")
        time.sleep(2)
        self.navigator.clickOnSeeAll()
        time.sleep(2)
        self.navigator.clickOnFullCase()
        time.sleep(2)
        parent_handle = self.driver.current_window_handle
        print(parent_handle)
        time.sleep(2)
        all_handles = self.driver.window_handles
        print(all_handles)
        for handle in all_handles:
            if handle != parent_handle:
                self.driver.switch_to.window(handle)
                time.sleep(3)
                self.navigator.clickOnResearch()
                self.logger.info("Full Case Analysis - Clicked on Research Notepad")
                time.sleep(2)
                self.navigator.selectResearchOption()
                time.sleep(2)
                self.navigator.clickOnCreateResearchTopic()
                time.sleep(2)
                self.logger.info("Clicked on Create New Research Topic")
                time.sleep(2)
                self.navigator.sendTopic()
                time.sleep(2)
                self.logger.info("Topic is entered")
                time.sleep(1)
                self.navigator.clickOnSave()
                time.sleep(2)
                self.logger.info("Clicked on Save Topic")
                time.sleep(1)
                selectedText = self.driver.find_element(By.XPATH, "//*[@id='popup-add-to-rn']/div[1]/div[2]/div/ul/li[1]/label")
                time.sleep(2)
                topicText = selectedText.get_attribute("title")
                print(topicText)
                time.sleep(1)
                self.logger.info("Entered Topic equals the first option label  " + topicText)
                time.sleep(2)
                self.driver.close()
        self.driver.switch_to.window(parent_handle)


    @pytest.mark.skip(reason="None")
    def test_copyCitation(self):
        self.logger.info("****TestCase AC-009 - Verify Copy Citation***")
        self.logger.info("*****Login Successful****")
        self.logger.info("**** Article Citator testing *****")
        self.navigator = ArticleCitator(self.driver)
        self.navigator.clickOnArticleCitatormenu()
        time.sleep(2)
        # self.navigator.clickOnClientListing()
        self.logger.info("Article Citator menu is available")
        time.sleep(2)
        self.driver.execute_script("window.scrollBy(0,500)", "")
        time.sleep(2)
        # Click on the first branch to expand
        self.navigator.clickOnexpandBranch()
        self.logger.info("First Branch is expanded")
        time.sleep(2)
        self.navigator.clickOnSeeAll()
        time.sleep(2)
        self.navigator.clickOnFullCase()
        time.sleep(2)
        parent_handle = self.driver.current_window_handle
        print(parent_handle)
        time.sleep(2)
        all_handles = self.driver.window_handles
        print(all_handles)
        for handle in all_handles:
            if handle != parent_handle:
                self.driver.switch_to.window(handle)
                time.sleep(3)
                self.navigator.clickOnCopyCitationLink()
                time.sleep(2)
                self.logger.info("Clicked on Copy Citation Link")
                time.sleep(1)
                self.logger.info("Toast Message - Citation Copied to clipboard")
                time.sleep(2)
                self.driver.close()
        self.driver.switch_to.window(parent_handle)


    @pytest.mark.skip(reason="None")
    def test_downloadDocumentLink(self):
            self.logger.info("****TestCase AC-010 - Verify Download Document***")
            self.logger.info("*****Login Successful****")
            self.logger.info("**** Article Citator testing *****")
            self.navigator = ArticleCitator(self.driver)
            self.navigator.clickOnArticleCitatormenu()
            time.sleep(2)
            # self.navigator.clickOnClientListing()
            self.logger.info("Article Citator menu is available")
            time.sleep(2)
            self.driver.execute_script("window.scrollBy(0,500)", "")
            time.sleep(2)
            # Click on the first branch to expand
            self.navigator.clickOnexpandBranch()
            self.logger.info("First Branch is expanded")
            time.sleep(2)
            self.navigator.clickOnSeeAll()
            time.sleep(2)
            self.navigator.clickOnFullCase()
            time.sleep(2)
            parent_handle = self.driver.current_window_handle
            print(parent_handle)
            time.sleep(2)
            all_handles = self.driver.window_handles
            print(all_handles)
            for handle in all_handles:
                if handle != parent_handle:
                    self.driver.switch_to.window(handle)
                    time.sleep(2)
                    self.navigator.clickOnDownloadDocumentLink()
                    time.sleep(3)
                    self.logger.info("Clicked on Download Document")
                    self.driver.close()
            #self.driver.switch_to.window(parent_handle)
            #self.driver.close()

    @pytest.mark.skip(reason="None")
    def test_viewPDF(self):
        self.logger.info("****TestCase AC-011 - Verify View PDF***")
        self.logger.info("*****Login Successful****")
        self.logger.info("**** Article Citator testing *****")
        self.navigator = ArticleCitator(self.driver)
        self.navigator.clickOnArticleCitatormenu()
        time.sleep(2)
        # self.navigator.clickOnClientListing()
        self.logger.info("Article Citator menu is available")
        time.sleep(2)
        self.driver.execute_script("window.scrollBy(0,500)", "")
        time.sleep(2)
        # Click on the first branch to expand
        self.navigator.clickOnexpandBranch()
        self.logger.info("First Branch is expanded")
        time.sleep(2)
        self.navigator.clickOnSeeAll()
        time.sleep(2)
        self.navigator.clickOnFullCase()
        time.sleep(2)
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
                self.navigator.clickOnViewPDF()
                time.sleep(2)
                self.logger.info("Clicked on View PDF link")
                self.driver.close()
        self.driver.switch_to.window(parent_handle)
        # self.driver.close()

    @pytest.mark.skip(reason="None")
    def test_SubjectNavigatorNavigation(self):
        self.logger.info("****TestCase AC-012 - Verify Subject Navigator from the navigation menu***")
        self.logger.info("*****Login Successful****")
        self.logger.info("**** Article Citator testing *****")
        self.navigator = ArticleCitator(self.driver)
        self.navigator.clickOnArticleCitatormenu()
        time.sleep(2)
        # self.navigator.clickOnClientListing()
        self.logger.info("Article Citator menu is available")
        time.sleep(2)
        self.driver.execute_script("window.scrollBy(0,500)", "")
        time.sleep(2)
        # Click on the first branch to expand
        self.navigator.clickOnexpandBranch()
        self.logger.info("First Branch is expanded")
        time.sleep(2)
        self.navigator.clickOnSeeAll()
        time.sleep(2)
        self.navigator.clickOnFullCase()
        time.sleep(2)
        parent_handle = self.driver.current_window_handle
        print(parent_handle)
        time.sleep(2)
        all_handles = self.driver.window_handles
        print(all_handles)
        for handle in all_handles:
            if handle != parent_handle:
                self.driver.switch_to.window(handle)
                time.sleep(2)
                self.navigator.clickOnSubjectNavigatorMenu()
                time.sleep(2)
                self.logger.info("Clicked on Subject Navigator menu")
                self.navigator.clickOnSubjectNavigatorLink()
                time.sleep(2)
                self.logger.info("Exapnded first link under Subject Navigator")
                time.sleep(2)
                self.driver.close()
        self.driver.switch_to.window(parent_handle)
        # self.driver.close()

    @pytest.mark.skip(reason="None")
    def test_PublicationNavigation(self):
        self.logger.info("****TestCase AC-014 - Verify Publication Citator from the navigation menu***")
        self.logger.info("*****Login Successful****")
        self.logger.info("**** Article Citator testing *****")
        self.navigator = ArticleCitator(self.driver)
        self.navigator.clickOnArticleCitatormenu()
        time.sleep(2)
        # self.navigator.clickOnClientListing()
        self.logger.info("Article Citator menu is available")
        time.sleep(2)
        self.driver.execute_script("window.scrollBy(0,500)", "")
        time.sleep(2)
        # Click on the first branch to expand
        self.navigator.clickOnexpandBranch()
        self.logger.info("First Branch is expanded")
        time.sleep(2)
        self.navigator.clickOnSeeAll()
        time.sleep(2)
        self.navigator.clickOnFullCase()
        time.sleep(2)
        parent_handle = self.driver.current_window_handle
        print(parent_handle)
        time.sleep(2)
        all_handles = self.driver.window_handles
        print(all_handles)
        for handle in all_handles:
            if handle != parent_handle:
                self.driver.switch_to.window(handle)
                time.sleep(2)
                self.navigator.clickOnPublicationCitatorMenu()
                time.sleep(2)
                self.logger.info("Clicked on Publication Citator menu")
                self.navigator.clickOnPublicationLink()
                time.sleep(2)
                self.logger.info("Expanded first link under Publication Citator")
                time.sleep(2)
                # self.driver.close()
        # self.driver.switch_to.window(parent_handle)
        # self.driver.close()

    @pytest.mark.skip(reason="None")
    def test_JurisprudenceNavigation(self):
        self.logger.info("****TestCase AC-013 - Verify Jurisprudence Citator from the navigation menu***")
        self.logger.info("*****Login Successful****")
        self.logger.info("**** Article Citator testing *****")
        self.navigator = ArticleCitator(self.driver)
        self.navigator.clickOnArticleCitatormenu()
        time.sleep(2)
        # self.navigator.clickOnClientListing()
        self.logger.info("Article Citator menu is available")
        time.sleep(2)
        self.driver.execute_script("window.scrollBy(0,500)", "")
        time.sleep(2)
        # Click on the first branch to expand
        self.navigator.clickOnexpandBranch()
        self.logger.info("First Branch is expanded")
        time.sleep(2)
        self.navigator.clickOnSeeAll()
        time.sleep(2)
        self.navigator.clickOnFullCase()
        time.sleep(2)
        parent_handle = self.driver.current_window_handle
        print(parent_handle)
        time.sleep(2)
        all_handles = self.driver.window_handles
        print(all_handles)
        for handle in all_handles:
            if handle != parent_handle:
                self.driver.switch_to.window(handle)
                time.sleep(2)
                self.navigator.clickOnJurisprudenceNavigatorMenu()
                time.sleep(2)
                self.logger.info("Clicked on Jurisprudence menu")
                self.navigator.clickOnJurisprudenceLink()
                time.sleep(2)
                self.logger.info("Expanded first link under Jurisprudence Citator")
                time.sleep(2)
                # self.driver.close()
        # self.driver.switch_to.window(parent_handle)
        # self.driver.close()

    @pytest.mark.skip(reason="None")
    def test_TermsAndPhrasesNavigation(self):
        self.logger.info("****TestCase AC-015 - Verify Terms & Phrases from the navigation menu***")
        self.logger.info("*****Login Successful****")
        self.logger.info("**** Article Citator testing *****")
        self.navigator = ArticleCitator(self.driver)
        self.navigator.clickOnArticleCitatormenu()
        time.sleep(2)
        # self.navigator.clickOnClientListing()
        self.logger.info("Article Citator menu is available")
        time.sleep(2)
        self.driver.execute_script("window.scrollBy(0,500)", "")
        time.sleep(2)
        # Click on the first branch to expand
        self.navigator.clickOnexpandBranch()
        self.logger.info("First Branch is expanded")
        time.sleep(2)
        self.navigator.clickOnSeeAll()
        time.sleep(2)
        self.navigator.clickOnFullCase()
        time.sleep(2)
        parent_handle = self.driver.current_window_handle
        print(parent_handle)
        time.sleep(2)
        all_handles = self.driver.window_handles
        print(all_handles)
        for handle in all_handles:
            if handle != parent_handle:
                self.driver.switch_to.window(handle)
                time.sleep(2)
                self.navigator.clickOnTermsAndPhrasesMenu()
                time.sleep(2)
                self.logger.info("Clicked on Terms And Phrases menu")
                self.navigator.clickOnTermsAndPhrasesLink()
                time.sleep(2)
                self.logger.info("Expanded first link under Terms And Phrases")
                time.sleep(2)
                self.driver.close()
        # self.driver.switch_to.window(parent_handle)
        # self.driver.close()

    @pytest.mark.skip(reason="None")
    def test_KeywordSearchNavigation(self):
        self.logger.info("****TestCase AC-016 - Verify Keyword Search from the navigation menu***")
        self.logger.info("*****Login Successful****")
        self.logger.info("**** Article Citator testing *****")
        self.navigator = ArticleCitator(self.driver)
        self.navigator.clickOnArticleCitatormenu()
        time.sleep(2)
        # self.navigator.clickOnClientListing()
        self.logger.info("Article Citator menu is available")
        time.sleep(2)
        self.driver.execute_script("window.scrollBy(0,500)", "")
        time.sleep(2)
        # Click on the first branch to expand
        self.navigator.clickOnexpandBranch()
        self.logger.info("First Branch is expanded")
        time.sleep(2)
        self.navigator.clickOnSeeAll()
        time.sleep(2)
        self.navigator.clickOnFullCase()
        time.sleep(2)
        parent_handle = self.driver.current_window_handle
        print(parent_handle)
        time.sleep(2)
        all_handles = self.driver.window_handles
        print(all_handles)
        for handle in all_handles:
            if handle != parent_handle:
                self.driver.switch_to.window(handle)
                time.sleep(2)
                self.navigator.clickOnKeywordSearch()
                time.sleep(2)
                self.logger.info("Clicked on Keyword Search menu")
                time.sleep(2)
                self.navigator.clickOnKeywordSearchEntry()
                time.sleep(2)
                self.logger.info("Entered Keyword search")
                self.navigator.clickOnSearchButton()
                time.sleep(2)
                self.logger.info("Clicked on Search")
                # self.driver.close()

        # self.driver.switch_to.window(parent_handle)
        # self.driver.close()

    @pytest.mark.skip(reason="None")
    def test_FullTextSearch(self):
        self.logger.info("****TestCase AC-017 - Verify Go To Full Text Search***")
        self.logger.info("*****Login Successful****")
        self.logger.info("**** Article Citator testing *****")
        self.navigator = ArticleCitator(self.driver)
        self.navigator.clickOnArticleCitatormenu()
        time.sleep(2)
        # self.navigator.clickOnClientListing()
        self.logger.info("Article Citator menu is available")
        time.sleep(2)
        self.driver.execute_script("window.scrollBy(0,500)", "")
        time.sleep(2)
        # Click on the first branch to expand
        self.navigator.clickOnexpandBranch()
        self.logger.info("First Branch is expanded")
        time.sleep(2)
        self.navigator.clickOnSeeAll()
        time.sleep(2)
        self.navigator.clickOnFullCase()
        time.sleep(2)
        parent_handle = self.driver.current_window_handle
        print(parent_handle)
        time.sleep(2)
        all_handles = self.driver.window_handles
        print(all_handles)
        for handle in all_handles:
            if handle != parent_handle:
                self.driver.switch_to.window(handle)
                time.sleep(2)
                self.navigator.clickOnKeywordSearch()
                time.sleep(2)
                self.logger.info("Clicked on Keyword Search menu")
                time.sleep(2)
                self.navigator.clickOnKeywordSearchEntry()
                time.sleep(2)
                self.logger.info("Entered Keyword search")
                self.navigator.clickOnSearchButton()
                time.sleep(2)
                self.logger.info("Clicked on Search")
                self.navigator.clickOnGoToFullTextSearch()
                time.sleep(2)
                self.logger.info("Clicked on Go To Full Text search link")
                self.driver.close()
        self.driver.switch_to.window(parent_handle)
        # self.driver.close()

