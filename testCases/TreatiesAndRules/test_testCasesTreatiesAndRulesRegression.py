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
    def test_downloadDocument(self):
        self.logger.info("****TestCase TreatiesAndRules-001 - Validate Download Document***")
        self.logger.info("*****Login Successful****")
        self.logger.info("**** Treaties And Rules testing *****")
        self.navigator = TreatiesAndRules(self.driver)
        self.navigator.clickOnTreatiesAndRules()
        self.logger.info("Clicked on  Treaties And Rules")
        time.sleep(2)
        self.navigator.clickOnExpandFirstLink()
        self.logger.info("Expanded the first Arbitration Rule")
        time.sleep(2)
        self.navigator.clickOnFirstLink()
        time.sleep(2)
        self.logger.info("Clicked on First Link")
        self.navigator.clickOnDownloadDocument()
        time.sleep(4)
        self.logger.info("Clicked on Download Document")
        time.sleep(2)

    #@pytest.mark.skip(reason="None")
    def test_addToDocumentComparison(self):
            self.logger.info("****TestCase TreatiesAndRules-002 - Validate Add to Document Comparison***")
            self.logger.info("*****Login Successful****")
            self.logger.info("**** Treaties And Rules testing *****")
            self.navigator = TreatiesAndRules(self.driver)
            self.navigator.clickOnTreatiesAndRules()
            self.logger.info("Clicked on  Treaties And Rules")
            time.sleep(2)
            self.navigator.clickOnExpandFirstLink()
            self.logger.info("Expanded the first Arbitration Rule")
            time.sleep(2)
            self.navigator.clickOnFirstLink()
            time.sleep(2)
            self.logger.info("Clicked on First Link")
            self.navigator.clickOnDocumentCompare()
            time.sleep(2)
            self.logger.info("Clicked on Download Document")
            self.navigator.selectGroupOption()
            time.sleep(2)
            self.logger.info("Selected the first group option")
            self.navigator.clickOnAddDocument()
            time.sleep(2)

    #@pytest.mark.skip(reason="None")
    def test_researchNotepad(self):
        self.logger.info("****TestCase TreatiesAndRules-003 - Validate Research Notepad***")
        self.logger.info("*****Login Successful****")
        self.logger.info("**** Treaties And Rules testing *****")
        self.navigator = TreatiesAndRules(self.driver)
        self.navigator.clickOnTreatiesAndRules()
        self.logger.info("Clicked on  Treaties And Rules")
        time.sleep(2)
        self.navigator.clickOnExpandFirstLink()
        self.logger.info("Expanded the first Arbitration Rule")
        time.sleep(2)
        self.navigator.clickOnFirstLink()
        time.sleep(2)
        self.logger.info("Clicked on First Link")
        self.navigator.clickOnResearch()
        time.sleep(2)
        self.logger.info("Clicked on Add to Notepad")
        cancleResearch = self.driver.find_element(By.XPATH, "//*[@id='btn-Cancel']")
        cancleResearch.click()
        time.sleep(2)

    #@pytest.mark.skip(reason="None")
    def test_copyCitation(self):
            self.logger.info("****TestCase TreatiesAndRules-004 - Validate Copy Citation***")
            self.logger.info("*****Login Successful****")
            self.logger.info("**** Treaties And Rules testing *****")
            self.navigator = TreatiesAndRules(self.driver)
            self.navigator.clickOnTreatiesAndRules()
            self.logger.info("Clicked on  Treaties And Rules")
            time.sleep(2)
            self.navigator.clickOnExpandFirstLink()
            self.logger.info("Expanded the first Arbitration Rule")
            time.sleep(2)
            self.navigator.clickOnFirstLink()
            time.sleep(2)
            self.logger.info("Clicked on First Link")
            self.navigator.clickOnCopyCitation()
            time.sleep(2)
            self.logger.info("Clicked on Copy Citation")
            time.sleep(2)


    #@pytest.mark.skip(reason="None")
    def test_viewOriginialPDF(self):
        self.logger.info("****TestCase TreatiesAndRules-005 - Validate View Original PDF***")
        self.logger.info("*****Login Successful****")
        self.logger.info("**** Treaties And Rules testing *****")
        self.navigator = TreatiesAndRules(self.driver)
        self.navigator.clickOnTreatiesAndRules()
        self.logger.info("Clicked on  Treaties And Rules")
        time.sleep(2)
        self.navigator.clickOnExpandFirstLink()
        self.logger.info("Expanded the first Arbitration Rule")
        time.sleep(2)
        self.navigator.clickOnFirstLink()
        time.sleep(2)
        self.logger.info("Clicked on First Link")
        self.navigator.clickOnViewPDF()
        time.sleep(2)
        self.logger.info("Clicked on View Original PDF")
        time.sleep(2)

    #@pytest.mark.skip(reason="None")
    def test_InstrumentDetailsAddtoDocument(self):
            self.logger.info("****TestCase TreatiesAndRules-006 - Validate Instrument Details - Document Comparison***")
            self.logger.info("*****Login Successful****")
            self.logger.info("**** Treaties And Rules testing *****")
            self.navigator = TreatiesAndRules(self.driver)
            self.navigator.clickOnTreatiesAndRules()
            self.logger.info("Clicked on  Treaties And Rules")
            time.sleep(2)
            self.navigator.clickOnExpandFirstLink()
            self.logger.info("Expanded the first Arbitration Rule")
            time.sleep(2)
            self.navigator.clickOnInstrumentDetails()
            time.sleep(2)
            self.logger.info("Clicked on Instrument Details")
            time.sleep(2)
            self.navigator.clickOnInstrumentDetailsLink()
            self.logger.info("Clicked on First Link under Instrument Details")
            time.sleep(2)
            self.navigator.clickOnDocumentCompare()
            time.sleep(2)
            self.logger.info("Clicked on Download Document")
            self.navigator.selectGroupOption()
            time.sleep(2)
            self.logger.info("Selected the first group option")
            self.navigator.clickOnAddDocument()
            time.sleep(2)

    #@pytest.mark.skip(reason="None")
    def test_instrumentDetailsResearchNotepad(self):
        self.logger.info("****TestCase TreatiesAndRules-007 - Validate Instrument Details -Research Notepad***")
        self.logger.info("*****Login Successful****")
        self.logger.info("**** Treaties And Rules testing *****")
        self.navigator = TreatiesAndRules(self.driver)
        self.navigator.clickOnTreatiesAndRules()
        self.logger.info("Clicked on  Treaties And Rules")
        time.sleep(2)
        self.navigator.clickOnExpandFirstLink()
        self.logger.info("Expanded the first Arbitration Rule")
        time.sleep(2)
        self.navigator.clickOnInstrumentDetails()
        time.sleep(2)
        self.logger.info("Clicked on Instrument Details")
        time.sleep(2)
        self.navigator.clickOnInstrumentDetailsLink()
        self.logger.info("Clicked on First Link under Instrument Details")
        time.sleep(2)
        # self.navigator.clickOnResearch()
        # time.sleep(2)
        # self.logger.info("Clicked on Add to Notepad")
        # cancleResearch = self.driver.find_element(By.XPATH, "//*[@id='btn-Cancel']")
        # cancleResearch.click()
        time.sleep(2)
        # self.navigator.selectResearchOption()
        # time.sleep(2)
        # self.logger.info("Selected Research Option")
        # self.navigator.clickOnAddNotepad()
        # self.logger.info("Clicked on Add Notepad")
        # time.sleep(2)

    #@pytest.mark.skip(reason="None")
    def test_instrumnetDetailsdownloadDocument(self):
        self.logger.info("****TestCase TreatiesAndRules-008 - Instrument Details -Validate Download Document***")
        self.logger.info("*****Login Successful****")
        self.logger.info("**** Treaties And Rules testing *****")
        self.navigator = TreatiesAndRules(self.driver)
        self.navigator.clickOnTreatiesAndRules()
        self.logger.info("Clicked on  Treaties And Rules")
        time.sleep(2)
        self.navigator.clickOnExpandFirstLink()
        self.logger.info("Expanded the first Arbitration Rule")
        self.navigator.clickOnInstrumentDetails()
        time.sleep(2)
        self.logger.info("Clicked on Instrument Details")
        time.sleep(2)
        self.navigator.clickOnInstrumentDetailsLink()
        self.logger.info("Clicked on First Link under Instrument Details")
        time.sleep(2)
        self.navigator.clickOnDownloadDocument()
        time.sleep(4)
        self.logger.info("Clicked on Download Document")
        time.sleep(2)

    #@pytest.mark.skip(reason="None")
    def test_instrumentDetailsviewOriginialPDF(self):
        self.logger.info("****TestCase TreatiesAndRules-009 - Instrument Details - Validate View Original PDF***")
        self.logger.info("*****Login Successful****")
        self.logger.info("**** Treaties And Rules testing *****")
        self.navigator = TreatiesAndRules(self.driver)
        self.navigator.clickOnTreatiesAndRules()
        self.logger.info("Clicked on  Treaties And Rules")
        time.sleep(2)
        self.navigator.clickOnExpandFirstLink()
        self.logger.info("Expanded the first Arbitration Rule")
        time.sleep(2)
        self.navigator.clickOnInstrumentDetails()
        time.sleep(2)
        self.logger.info("Clicked on Instrument Details")
        time.sleep(2)
        self.navigator.clickOnInstrumentDetailsLink()
        self.logger.info("Clicked on First Link under Instrument Details")
        time.sleep(2)
        self.navigator.clickOnViewPDF()
        time.sleep(2)
        self.logger.info("Clicked on View Original PDF")
        time.sleep(2)

    #@pytest.mark.skip(reason="None")
    def test_instrumentDetailscopyCitation(self):
        self.logger.info("****TestCase TreatiesAndRules-010 - Instrument Details -Validate Copy Citation***")
        self.logger.info("*****Login Successful****")
        self.logger.info("**** Treaties And Rules testing *****")
        self.navigator = TreatiesAndRules(self.driver)
        self.navigator.clickOnTreatiesAndRules()
        self.logger.info("Clicked on  Treaties And Rules")
        time.sleep(2)
        self.navigator.clickOnExpandFirstLink()
        self.logger.info("Expanded the first Arbitration Rule")
        time.sleep(2)
        self.navigator.clickOnInstrumentDetails()
        time.sleep(2)
        self.logger.info("Clicked on Instrument Details")
        time.sleep(2)
        self.navigator.clickOnInstrumentDetailsLink()
        self.logger.info("Clicked on First Link under Instrument Details")
        time.sleep(2)
        self.navigator.clickOnCopyCitation()
        time.sleep(2)
        self.logger.info("Clicked on Copy Citation")
        time.sleep(2)



