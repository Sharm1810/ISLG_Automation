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
    def test_01expandBranch(self):
        self.logger.info("****TestCase TermsPhrases-001 - Validate Full Case Analysis***")
        self.logger.info("*****Login Successful****")
        self.logger.info("**** Terms And Phrases testing *****")
        self.navigator = TermsAndPhrases(self.driver)
        self.navigator.clickOnTermsAndPhrases()
        time.sleep(2)
        # self.navigator.clickOnClientListing()
        self.logger.info("Terms And Phrases menu is available")
        heading = self.navigator.getHeading()
        print(heading)
        self.navigator.clickOnFirstBranch()
        self.logger.info("Expanded First Branch")
        time.sleep(2)
        self.navigator.clickOnExpandFirst()
        self.logger.info("Expanded First Branch")
        time.sleep(2)
        self.navigator.clickOnFullCaseAnalysis()
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
        self.driver.switch_to.window(parent_handle)
        time.sleep(2)

    #@pytest.mark.skip(reason="None")
    def test_02ViewInTermsAndPhrases(self):
        self.logger.info("****TestCase TermsPhrases-002 - Validate View in Terms And Phrases***")
        self.logger.info("*****Login Successful****")
        self.logger.info("**** Terms And Phrases testing *****")
        self.navigator = TermsAndPhrases(self.driver)
        self.navigator.clickOnTermsAndPhrases()
        time.sleep(2)
        # self.navigator.clickOnClientListing()
        self.logger.info("Terms And Phrases menu is available")
        heading = self.navigator.getHeading()
        print(heading)
        self.navigator.clickOnFirstBranch()
        self.logger.info("Expanded First Branch")
        time.sleep(2)
        self.navigator.clickOnExpandFirst()
        self.logger.info("Expanded First Branch")
        time.sleep(2)
        self.navigator.clickOnFullCaseAnalysis()
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
                time.sleep(2)
                self.navigator.clickOnViewAllTerms()
                self.logger.info("Clicked on View All Terms And Phrases link")
                time.sleep(2)
                self.navigator.clickOnViewInTermsAndPhrasesLink()
                self.logger.info("Clicked on View in TermsAndPhrases")
                time.sleep(2)
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
    def test_03AllDisputesDocuments(self):
        self.logger.info("****TestCase TermsPhrases-003 - Validate All Disputes Documents***")
        self.logger.info("*****Login Successful****")
        self.logger.info("**** Terms And Phrases testing *****")
        self.navigator = TermsAndPhrases(self.driver)
        self.navigator.clickOnTermsAndPhrases()
        time.sleep(2)
        # self.navigator.clickOnClientListing()
        self.logger.info("Terms And Phrases menu is available")
        heading = self.navigator.getHeading()
        print(heading)
        self.navigator.clickOnFirstBranch()
        self.logger.info("Expanded First Branch")
        time.sleep(2)
        self.navigator.clickOnExpandFirst()
        self.logger.info("Expanded First Branch")
        time.sleep(2)
        self.navigator.clickOnDisputeDetails()
        self.logger.info("Clicked on Dispute Details tab")
        time.sleep(2)
        self.navigator.clickOnAllDispute()
        self.logger.info("Clicked on All Documents from Dispute")
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
        self.driver.switch_to.window(parent_handle)
        time.sleep(2)

    #@pytest.mark.skip(reason="None")
    def test_04expandProceedingDetails(self):
        self.logger.info("****TestCase TermsPhrases-004 - Validate Expand Proceedings***")
        self.logger.info("*****Login Successful****")
        self.logger.info("**** Terms And Phrases testing *****")
        self.navigator = TermsAndPhrases(self.driver)
        self.navigator.clickOnTermsAndPhrases()
        time.sleep(2)
        # self.navigator.clickOnClientListing()
        self.logger.info("Terms And Phrases menu is available")
        heading = self.navigator.getHeading()
        print(heading)
        self.navigator.clickOnFirstBranch()
        self.logger.info("Expanded First Branch")
        time.sleep(2)
        self.navigator.clickOnExpandFirst()
        self.logger.info("Expanded First Branch")
        time.sleep(2)
        self.navigator.clickOnDisputeDetails()
        self.logger.info("Clicked on Dispute Details tab")
        time.sleep(2)
        self.navigator.clickOnExpandProceeding()
        self.logger.info("Clicked on Expand Proceeding Details")
        time.sleep(2)
        self.navigator.clickOnExpandProceeding()
        self.logger.info("Clicked on Collapse Proceeding Details")
        time.sleep(2)

    #@pytest.mark.skip(reason="None")
    def test_05allDisputeDetails(self):
        self.logger.info("****TestCase TermsPhrases-005 - Validate All Dispute Details link***")
        self.logger.info("*****Login Successful****")
        self.logger.info("**** Terms And Phrases testing *****")
        self.navigator = TermsAndPhrases(self.driver)
        self.navigator.clickOnTermsAndPhrases()
        time.sleep(2)
        # self.navigator.clickOnClientListing()
        self.logger.info("Terms And Phrases menu is available")
        heading = self.navigator.getHeading()
        print(heading)
        self.navigator.clickOnFirstBranch()
        self.logger.info("Expanded First Branch")
        time.sleep(2)
        self.navigator.clickOnExpandFirst()
        self.logger.info("Expanded First Branch")
        time.sleep(2)
        self.navigator.clickOnDisputeDetails()
        self.logger.info("Clicked on Dispute Details tab")
        time.sleep(2)
        self.navigator.clickOnAllDisputes()
        self.logger.info("Clicked on All Disputes")
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
        self.driver.switch_to.window(parent_handle)
        time.sleep(2)

    #@pytest.mark.skip(reason="None")
    def test_06downloadAllDocuments(self):
        self.logger.info("****TestCase TermsPhrases-006 - Validate Dispute Details - Download All Documents***")
        self.logger.info("*****Login Successful****")
        self.logger.info("**** Terms And Phrases testing *****")
        self.navigator = TermsAndPhrases(self.driver)
        self.navigator.clickOnTermsAndPhrases()
        time.sleep(2)
        # self.navigator.clickOnClientListing()
        self.logger.info("Terms And Phrases menu is available")
        heading = self.navigator.getHeading()
        print(heading)
        self.navigator.clickOnFirstBranch()
        self.logger.info("Expanded First Branch")
        time.sleep(2)
        self.navigator.clickOnExpandFirst()
        self.logger.info("Expanded First Branch")
        time.sleep(2)
        self.navigator.clickOnDisputeDetails()
        self.logger.info("Clicked on Dispute Details tab")
        time.sleep(2)
        self.navigator.clickOnAllDisputes()
        self.logger.info("Clicked on All Disputes")
        time.sleep(2)
        parent_handle = self.driver.current_window_handle
        print(parent_handle)
        time.sleep(2)
        all_handles = self.driver.window_handles
        print(all_handles)
        for handle in all_handles:
            if handle != parent_handle:
                self.driver.switch_to.window(handle)
                self.navigator.clickOnDownloadDocument()
                self.logger.info("Clicked on Download Document")
                time.sleep(2)
                self.navigator.clickOnStartDownload()
                self.logger.info("Clicked on Start Download")
                time.sleep(3)
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
    def test_07addToNotepad(self):
        self.logger.info("****TestCase TermsPhrases-007 - Validate Dispute Details - Add To Notepad***")
        self.logger.info("*****Login Successful****")
        self.logger.info("**** Terms And Phrases testing *****")
        self.navigator = TermsAndPhrases(self.driver)
        self.navigator.clickOnTermsAndPhrases()
        time.sleep(2)
        # self.navigator.clickOnClientListing()
        self.logger.info("Terms And Phrases menu is available")
        heading = self.navigator.getHeading()
        print(heading)
        self.navigator.clickOnFirstBranch()
        self.logger.info("Expanded First Branch")
        time.sleep(2)
        self.navigator.clickOnExpandFirst()
        self.logger.info("Expanded First Branch")
        time.sleep(2)
        self.navigator.clickOnDisputeDetails()
        self.logger.info("Clicked on Dispute Details tab")
        time.sleep(2)
        self.navigator.clickOnAllDisputes()
        self.logger.info("Clicked on All Disputes")
        time.sleep(2)
        parent_handle = self.driver.current_window_handle
        print(parent_handle)
        time.sleep(2)
        all_handles = self.driver.window_handles
        print(all_handles)
        for handle in all_handles:
            if handle != parent_handle:
                self.driver.switch_to.window(handle)
                self.navigator.clickOnNotepad()
                self.logger.info("Clicked on Notepad")
                time.sleep(2)
                self.navigator.selectResearchOption()
                self.logger.info("Selected an option")
                time.sleep(2)
                self.navigator.clickOnAddNotepad()
                self.logger.info("Clicked on Add Notepad")
                time.sleep(2)
                self.driver.close()
        self.driver.switch_to.window(parent_handle)
        time.sleep(2)

    #@pytest.mark.skip(reason="None")
    def test_08copyCitation(self):
        self.logger.info("****TestCase TermsPhrases-008 - Validate Dispute Details - Copy Citation***")
        self.logger.info("*****Login Successful****")
        self.logger.info("**** Terms And Phrases testing *****")
        self.navigator = TermsAndPhrases(self.driver)
        self.navigator.clickOnTermsAndPhrases()
        time.sleep(2)
        # self.navigator.clickOnClientListing()
        self.logger.info("Terms And Phrases menu is available")
        heading = self.navigator.getHeading()
        print(heading)
        self.navigator.clickOnFirstBranch()
        self.logger.info("Expanded First Branch")
        time.sleep(2)
        self.navigator.clickOnExpandFirst()
        self.logger.info("Expanded First Branch")
        time.sleep(2)
        self.navigator.clickOnDisputeDetails()
        self.logger.info("Clicked on Dispute Details tab")
        time.sleep(2)
        self.navigator.clickOnAllDisputes()
        self.logger.info("Clicked on All Disputes")
        time.sleep(2)
        parent_handle = self.driver.current_window_handle
        print(parent_handle)
        time.sleep(2)
        all_handles = self.driver.window_handles
        print(all_handles)
        for handle in all_handles:
            if handle != parent_handle:
                self.driver.switch_to.window(handle)
                self.navigator.clickOnCopyCitation()
                time.sleep(2)
                self.driver.close()
        self.driver.switch_to.window(parent_handle)
        time.sleep(2)

    #@pytest.mark.skip(reason="None")
    def test_09downloadDocument(self):
        self.logger.info("****TestCase TermsPhrases-009 - Validate Full Case Analysis - Download Document***")
        self.logger.info("*****Login Successful****")
        self.logger.info("**** Terms And Phrases testing *****")
        self.navigator = TermsAndPhrases(self.driver)
        self.navigator.clickOnTermsAndPhrases()
        time.sleep(2)
        # self.navigator.clickOnClientListing()
        self.logger.info("Terms And Phrases menu is available")
        heading = self.navigator.getHeading()
        print(heading)
        self.navigator.clickOnFirstBranch()
        self.logger.info("Expanded First Branch")
        time.sleep(2)
        self.navigator.clickOnExpandFirst()
        self.logger.info("Expanded First Branch")
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
                self.navigator.clickOnDownload()
                time.sleep(2)
                self.logger.info("Clicked on Download Document")
                self.driver.close()
        self.driver.switch_to.window(parent_handle)
        time.sleep(2)

    #@pytest.mark.skip(reason="None")
    def test_10addToDocumentComparison(self):
        self.logger.info("****TestCase TermsPhrases-010 - Validate Full Case Analysis - Add to Document Comparison***")
        self.logger.info("*****Login Successful****")
        self.logger.info("**** Terms And Phrases testing *****")
        self.navigator = TermsAndPhrases(self.driver)
        self.navigator.clickOnTermsAndPhrases()
        time.sleep(2)
        # self.navigator.clickOnClientListing()
        self.logger.info("Terms And Phrases menu is available")
        heading = self.navigator.getHeading()
        print(heading)
        self.navigator.clickOnFirstBranch()
        self.logger.info("Expanded First Branch")
        time.sleep(2)
        self.navigator.clickOnExpandFirst()
        self.logger.info("Expanded First Branch")
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
                self.navigator.clickOnDocumentComparison()
                time.sleep(2)
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
    def test_11researchNotepad(self):
            self.logger.info(
                "****TestCase TermsPhrases-011 - Validate Full Case Analysis - Add to Research Notepad***")
            self.logger.info("*****Login Successful****")
            self.logger.info("**** Terms And Phrases testing *****")
            self.navigator = TermsAndPhrases(self.driver)
            self.navigator.clickOnTermsAndPhrases()
            time.sleep(2)
            # self.navigator.clickOnClientListing()
            self.logger.info("Terms And Phrases menu is available")
            heading = self.navigator.getHeading()
            print(heading)
            self.navigator.clickOnFirstBranch()
            self.logger.info("Expanded First Branch")
            time.sleep(2)
            self.navigator.clickOnExpandFirst()
            self.logger.info("Expanded First Branch")
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
                    self.navigator.clickOnResearch()
                    self.logger.info("Full Case Analysis - Clicked on Research Notepad")
                    time.sleep(2)
                    self.navigator.selectResearchOption()
                    self.logger.info("Selected Research Option")
                    time.sleep(3)
                    self.navigator.clickOnAddNotepad()
                    self.logger.info("Clicked on Add to Notepad")
                    self.driver.close()
            self.driver.switch_to.window(parent_handle)
            time.sleep(2)

    #@pytest.mark.skip(reason="None")
    def test_12viewOriginalPdf(self):
        self.logger.info(
            "****TestCase TermsPhrases-012 - Validate Full Case Analysis - View Original PDF***")
        self.logger.info("*****Login Successful****")
        self.logger.info("**** Terms And Phrases testing *****")
        self.navigator = TermsAndPhrases(self.driver)
        self.navigator.clickOnTermsAndPhrases()
        time.sleep(2)
        # self.navigator.clickOnClientListing()
        self.logger.info("Terms And Phrases menu is available")
        heading = self.navigator.getHeading()
        print(heading)
        self.navigator.clickOnFirstBranch()
        self.logger.info("Expanded First Branch")
        time.sleep(2)
        self.navigator.clickOnExpandFirst()
        self.logger.info("Expanded First Branch")
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
                self.navigator.clickOnViewPDF()
                time.sleep(2)
                self.logger.info("Clicked on Original PDF")
                self.driver.close()
        self.driver.switch_to.window(parent_handle)
        time.sleep(2)

    #@pytest.mark.skip(reason="None")
    def test_13viewParagraphExcerpt(self):
        self.logger.info(
            "****TestCase TermsPhrases-013 - Validate Full Case Analysis - View Paragraph Excerpt***")
        self.logger.info("*****Login Successful****")
        self.logger.info("**** Terms And Phrases testing *****")
        self.navigator = TermsAndPhrases(self.driver)
        self.navigator.clickOnTermsAndPhrases()
        time.sleep(2)
        # self.navigator.clickOnClientListing()
        self.logger.info("Terms And Phrases menu is available")
        heading = self.navigator.getHeading()
        print(heading)
        self.navigator.clickOnFirstBranch()
        self.logger.info("Expanded First Branch")
        time.sleep(2)
        self.navigator.clickOnExpandFirst()
        self.logger.info("Expanded First Branch")
        time.sleep(2)
        self.navigator.clickOnFullCaseAnalysis()
        time.sleep(2)
        self.logger.info("Clicked on Full Case Analysis")
        self.navigator.clickOnExcerpt()
        time.sleep(2)
        self.logger.info("Clicked on Paragraph Excerpt")
        parent_handle = self.driver.current_window_handle
        print(parent_handle)
        time.sleep(2)
        all_handles = self.driver.window_handles
        print(all_handles)
        for handle in all_handles:
            if handle != parent_handle:
                self.driver.switch_to.window(handle)
                self.driver.close()
        self.driver.switch_to.window(parent_handle)
        time.sleep(2)


