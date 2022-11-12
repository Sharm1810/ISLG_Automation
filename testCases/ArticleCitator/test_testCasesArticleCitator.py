import sys
from telnetlib import EC

import clipboard
import pytest
import time
import json

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select

from pageObjects.LoginPage import LoginPage
from pageObjects.SubjectNavigator import SubjectNavigator
from pageObjects.Article import ArticleCitator
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
class Test_testCasesArticleCitator:
    logger = LogGen.loggen()

    # This method adds the document to researchNotepad

    @pytest.mark.skip(reason="None")
    def test_addtoResearch(self):
        self.logger.info("****TestCase AC-001 - Verify Add to Research***")
        self.logger.info("*****Login Successful****")
        self.logger.info("**** Article Citator testing *****")
        self.navigator = ArticleCitator(self.driver)
        self.navigator.clickOnArticleCitatormenu()
        time.sleep(2)
        self.navigator.clickOnClientListing()
        self.logger.info("Article Citator menu is available")
        time.sleep(2)
        self.driver.execute_script("window.scrollBy(0,500)", "")
        time.sleep(2)
        # Click on the first branch to expand
        self.navigator.clickOnexpandBranch()
        self.logger.info("First Branch is expanded")
        self.navigator.clickOnActions()
        self.logger.info("Clicked on Actions")
        self.navigator.clickOnResearchNotepad()
        self.logger.info("Clicked on Research Notepad")
        self.navigator.clickOnResearchTopicOption()
        self.logger.info("Selected the option")
        self.navigator.clickOnAddResearch()
        self.logger.info("Clicked on Add Research")
        self.navigator.clickOnEntireDocument()
        self.logger.info("Selected Entire Document option")
        self.navigator.clickOnEntireDocumentAdd()
        self.logger.info("Clicked on Add")
        text = self.driver.find_element(By.XPATH, "/html/body/div[7]/span[3]").text
        self.logger.info("Displayed message " + text)

    # This method adds the document to Document Comparison
    @pytest.mark.skip(reason="None")
    def test_documentComparison(self):
        self.logger.info("****TestCase AC-002 - Verify Document to Comparison***")
        self.navigator = ArticleCitator(self.driver)
        self.navigator.clickOnArticleCitatormenu()
        #self.navigator.clickOnClientListing()
        self.navigator.clickOnexpandBranch()
        self.logger.info("First Branch is expanded")
        self.navigator.clickOnActions()
        self.logger.info("Clicked on Actions")
        self.navigator.clickOnDocumentComparison()
        self.logger.info("Clicked On Document Comparison")
        self.navigator.selectDocumentComparisonOption()
        self.logger.info("Selected the first option")
        self.navigator.clickOnAddDocumentComparison()
        self.logger.info("Clicked on Add Document Comparison")
        documentText = self.driver.find_element(By.XPATH, "/html/body/div[7]/span[3]").text
        self.logger.info("Displayed message" + documentText)

    # This method copies Location
    @pytest.mark.skip(reason="None")
    def test_copyLocation(self):
        self.logger.info("****TestCase AC-003 - Verify Copy Location***")
        self.navigator = ArticleCitator(self.driver)
        self.navigator.clickOnArticleCitatormenu()
        #self.navigator.clickOnClientListing()
        self.navigator.clickOnexpandBranch()
        self.logger.info("First Branch is expanded")
        self.navigator.clickOnActions()
        self.logger.info("Clicked on Actions")
        self.navigator.clickOnCopyLocation()
        self.logger.info("Clicked on Copy Location")
        parent_handle = self.driver.current_window_handle
        print(parent_handle)
        # test = self.driver.find_element_by_xpath("//input[@title='Search']")
        time.sleep(3)
        myurl = clipboard.paste()
        print(myurl)
        self.logger.info(myurl + "  URL copied")
        self.driver.execute_script("window.open('" + myurl + "');")
        time.sleep(2)
        all_handles = self.driver.window_handles
        print(all_handles)
        for handle in all_handles:
            if handle != parent_handle:
                self.driver.switch_to.window(handle)
                time.sleep(2)
                self.driver.close()
        self.driver.switch_to.window(parent_handle)
        time.sleep(2)

    # This method Follows Topic
    @pytest.mark.skip(reason="None")
    def test_followTopic(self):
        self.logger.info("****TestCase AC-004 - Verify Follow Topic***")
        self.navigator = ArticleCitator(self.driver)
        self.navigator.clickOnArticleCitatormenu()
        self.navigator.clickOnClientListing()
        self.navigator.clickOnexpandBranch()
        self.logger.info("First Branch is expanded")
        self.navigator.clickOnActions()
        self.logger.info("Clicked on Actions")
        self.navigator.clickOnFollowTopic()
        self.logger.info("Clicked on Follow Topic")
        followTopicText = self.driver.find_element(By.XPATH, "/html/body/div[7]/span[3]").text
        self.logger.info("Displayed message" + followTopicText)
        self.navigator.clickOnActions()
        self.navigator.clickOnActions()
        # Need to check this later. There is also a bug associated with this
        # followtopicstate = self.driver.find_element_by_xpath("//*[contains(@title, 'Follow Topic')]")
        # elementdisabled = followtopicstate.get_property('disabled')
        # print(elementdisabled)
        # self.logger.info(elementdisabled)
        # self.logger.info("follow topic is disabled")

    # This method checks for Provision tab and Instrument Details tab not present when clicked on collapse.
    @pytest.mark.skip(reason="None")
    def test_collapse(self):
        self.logger.info("****TestCase AC-005 - Verify Collapse- Provision tab and Instrumentation Deatils***")
        self.logger.info("*****Login Successful****")
        self.logger.info("**** Subject Navigator testing *****")
        self.navigator = ArticleCitator(self.driver)
        self.navigator.clickOnArticleCitatormenu()
        time.sleep(2)
        #self.navigator.clickOnClientListing()
        self.logger.info("Article Citator menu is available")
        time.sleep(2)
        self.driver.execute_script("window.scrollBy(0,1800)", "")
        time.sleep(2)
        # Click on the first branch to expand
        self.navigator.clickOnexpandThirtyFirstBranch()
        self.logger.info("Thirty First Branch is expanded")
        clickOnCollapse = self.driver.find_element(By.XPATH, "//*[@id='page-content']/div/div[5]/div/div[26]//div//div//div//button//i[2]")
        self.driver.execute_script("arguments[0].click();", clickOnCollapse)
        #self.navigator.clickOnCollapse()
        #try:
        provisionTab = self.driver.find_element(By.XPATH, "//div[@class='tabs__list hide-compact']//a[@id='item-list-item-card-3-tab-1']").text
        if(len(provisionTab)==0):
            print("yes")
            self.logger.info("Provision Tab is not displayed when clicked on collapse")
        #except Exception('ElementNotVisibleException'):
        instrumentDetails = self.driver.find_element(By.XPATH, "//div[@class='tabs__list hide-compact']//a[@id='item-list-item-card-3-tab-2']").text
        if(len(instrumentDetails)==0):
            print(instrumentDetails)
            self.logger.info("Instruments Tab is not displayed when clicked on collapse")

       # try:
            #self.navigator.checkInstrumentDetails()
       # except Exception('ElementNotVisibleException'):
            #self.logger.info("Instrument Details Tab is not displayed when clicked on collapse")

    @pytest.mark.skip(reason="None")
    def test_provisionTab(self):
        self.logger.info("****TestCase AC-006 - Verify Provision Tab***")
        self.logger.info("*****Login Successful****")
        self.logger.info("**** Subject Navigator testing *****")
        self.navigator = ArticleCitator(self.driver)
        self.navigator.clickOnArticleCitatormenu()
        time.sleep(2)
        #self.navigator.clickOnClientListing()
        self.logger.info("Article Citator menu is available")
        time.sleep(2)
        self.driver.execute_script("window.scrollBy(0,1800)", "")
        time.sleep(2)
        # Click on the first branch to expand
        self.navigator.clickOnexpandThirtyFirstBranch()
        self.logger.info("Thirty First Branch is expanded")
        provisionTab = self.driver.find_element(By.XPATH,
                                                "//div[@class='tabs__list hide-compact']//a[@id='item-list-item-card-3-tab-1']")
        self.driver.execute_script("arguments[0].click();", provisionTab)
        #self.navigator.clickOnProvisionTab()
        #self.logger.info("Clicking on Provision tab")
        copyCitation = self.driver.find_element(By.XPATH, "//*[@id='item-list-item-card-3-tab-1-content']/div/div[1]/div[1]/p/small/a")
        self.driver.execute_script("arguments[0].click();", copyCitation)
        #self.navigator.clickOnCopyCitation()
        self.logger.info(self.navigator.getToastMessageCopyCitation())
        # paste the copied citation to notepad
        # open the file for write operation
        f = open('citation.txt', 'w')
        citationcopied = clipboard.paste()
        self.logger.info(citationcopied + "  copied citation")
        f.write(citationcopied)
        # close the file
        f.close()
        # open the file for read
        f = open('citation.txt', 'r')
        # print the contents in console
        print(f.read())
        # close the file
        f.close()

    # This test case is related to the Find in Provision tab
    @pytest.mark.skip(reason="None")
    def test_provisionTabFind(self):
        self.logger.info("****TestCase AC-007 - Verify Find in Provision Tab***")
        self.navigator = ArticleCitator(self.driver)
        self.navigator.clickOnArticleCitatormenu()
        time.sleep(2)
        # self.navigator.clickOnClientListing()
        self.logger.info("Article Citator menu is available")
        time.sleep(2)
        self.driver.execute_script("window.scrollBy(0,1800)", "")
        time.sleep(2)
        # Click on the first branch to expand
        self.navigator.clickOnexpandThirtyFirstBranch()
        self.logger.info("Thirty First Branch is expanded")
        #self.navigator.clickOnProvisionTab()
        self.logger.info("Clicking on Provision tab")
        #findSendData = self.driver.find_element(By.XPATH, "//*[@id='provisiondata_10701']/div/div/div[2]/div/input")
        #findSendData.send_keys("Generally")
        myopen = open('jsonfiles\provisiontabfind.json', 'r')
        jsondata = myopen.read()
        with open('jsonfiles\provisiontabfind.json') as data_file:
            data = json.load(data_file)
            for v in data.values():
                searchvlaue = v
                #findSendData = self.driver.find_element(By.XPATH,
                                                        #"//div[@id='provisiondata_10697']//div//div//div//div//input[@data-sourceid='10697']")
                findSendData = self.driver.find_element(By.XPATH, "//div[@id='provisiondata_10697']//div//div//div//div//input[@data-sourceid='10697']")
                findSendData.clear()
                findSendData.send_keys(searchvlaue)
                self.driver.find_element(By.XPATH, "//div[@id='provisiondata_10697']//div//div//div//div//button//i[@data-sourceid='10697']").click()
                searchstr = self.driver.find_element(By.XPATH, "//li[@class='Display paginateli']").text
                self.logger.info(searchstr)
                # searchstrnotfound = self.driver.find_element(By.XPATH, "//p[@wfd-invisible='true']//strong[contains(text(),'No records found.')]")

    # This is to validate Instrument Details tab
    @pytest.mark.skip(reason="None")
    def test_instrumentDetailsTab(self):
        self.logger.info("****TestCase AC-008 - Verify Instrument Deatils Tab***")
        self.navigator = ArticleCitator(self.driver)
        self.navigator.clickOnArticleCitatormenu()
        time.sleep(2)
        # self.navigator.clickOnClientListing()
        self.logger.info("Article Citator menu is available")
        time.sleep(2)
        self.driver.execute_script("window.scrollBy(0,1800)", "")
        time.sleep(2)
        # Click on the first branch to expand
        self.navigator.clickOnexpandThirtyFirstBranch()
        self.logger.info("Thirty First Branch is expanded")
        self.navigator.clickOnInstrumentDetailsTab()
        self.logger.info("Clicked on Instrument Details Tab")

    #@pytest.mark.skip(reason="None")
    def test_find(self):
        self.logger.info("****TestCase AC-009 - Validate Find and Reset***")
        self.navigator = ArticleCitator(self.driver)
        self.navigator.clickOnArticleCitatormenu()
        time.sleep(2)
        self.navigator.clickOnClientListing()
        self.logger.info("Article Citator menu is available")
        time.sleep(2)
        myopen = open('jsonfiles\provisiontabfind.json', 'r')
        jsondata = myopen.read()
        with open('jsonfiles\Find.json') as data_file:
            data = json.load(data_file)
            for v in data.values():
                searchvalue = v
                findSendData = self.driver.find_element(By.XPATH,
                                                        "//input[@id='search-articlecitator']")
                # findSendData.clear()
                time.sleep(2)
                findSendData.send_keys(searchvalue)
                self.navigator.clickOnFind()
                found = self.driver.find_element(By.CSS_SELECTOR,
                                                 "#search-popover > p:nth-child(2) > strong > span").get_attribute(
                    'textContent')
                self.logger.info(found + " Matches Found")
                time.sleep(2)
                self.navigator.clickOnReset()

    @pytest.mark.skip(reason="None")
    def test_fullCaseAnalysis(self):
        self.logger.info("****TestCase AC-010 - Validate Full Case Analysis***")
        self.navigator = ArticleCitator(self.driver)
        self.navigator.clickOnArticleCitatormenu()
        time.sleep(2)
        #self.navigator.clickOnClientListing()
        self.driver.execute_script("window.scrollBy(0,1800)", "")
        time.sleep(2)
        # Click on the first branch to expand
        self.navigator.clickOnexpandThirtyFirstBranch()
        self.logger.info("Thirty First Branch is expanded")
        clickSeeAll = self.driver.find_element(By.XPATH, "//*[@id='item-list-item-card-1361-dropdown-content-control']/span[1]/strong/span")
        self.driver.execute_script("arguments[0].click();", clickSeeAll)
        clickOnFullCase = self.driver.find_element(By.XPATH, "//div[@class='dropdown__content dropdown__content--padded']//div[1]//div[2]//div[2]//div[1]//div[1]//div[3]//div[2]//a[1]")
        self.driver.execute_script("arguments[0].scrollIntoView();", clickOnFullCase)
        self.driver.execute_script("arguments[0].click();", clickOnFullCase)
        parent_handle = self.driver.current_window_handle
        all_handles = self.driver.window_handles
        print(all_handles)
        for handle in all_handles:
            if handle != parent_handle:
                self.driver.switch_to.window(handle)
                time.sleep(2)
                textarticle = getArticleCitator = self.driver.find_element(By.CSS_SELECTOR, "#document-view > nav > ul > li.active.ac > a")
                textarticlecitator = textarticle.text
                assert "Article Citator" == textarticlecitator
                self.logger.info("Article Citator is displayed")
                self.driver.close()

        self.driver.switch_to.window(parent_handle)

    @pytest.mark.skip(reason="None")
    def test_provisionExtract(self):
        self.logger.info("****TestCase AC-011 - Validate Provision Extract***")
        self.navigator = ArticleCitator(self.driver)
        self.navigator.clickOnArticleCitatormenu()
        time.sleep(2)
        #self.navigator.clickOnClientListing()
        self.driver.execute_script("window.scrollBy(0,1800)", "")
        time.sleep(2)
        # Click on the first branch to expand
        self.navigator.clickOnexpandThirtyFirstBranch()
        self.logger.info("Thirty First Branch is expanded")
        provisionExtract = self.driver.find_element(By.XPATH, "//*[@id='prvMaster_1361']/a[1]/span")
        self.driver.execute_script("arguments[0].click();", provisionExtract)
        extractText = self.driver.find_element(By.XPATH, "//*[@id='popup-prv-extract']/div[1]/div[1]/div/span/span")
        provisiontext = extractText.text
        self.logger.info("Document Extract for Provision: " + provisiontext)
        time.sleep(2)
        closeProvision = self.driver.find_element(By.XPATH, "//*[@id='popup-prv-extract']/div[1]/div[1]/button")
        self.driver.execute_script("arguments[0].click();", closeProvision)

    @pytest.mark.skip(reason="None")
    def test_filterType(self):
        self.logger.info("****TestCase AC-012 - Validate Filter Type and Clear Filters***")
        self.navigator = ArticleCitator(self.driver)
        self.navigator.clickOnArticleCitatormenu()
        time.sleep(2)
        #self.navigator.clickOnClientListing()
        filterTypeExpand = self.driver.find_element(By.XPATH, "//*[@id='articlecitator-filter-dropdown-control']")
        self.driver.execute_script("arguments[0].click();", filterTypeExpand)
        self.logger.info("Filter Type is expanded")
        #Arbitration Rules Filter Type
        arbitrationRulesFilter = self.driver.find_element(By.XPATH, "//*[@id='articlecitator-filter-dropdown']/p[1]/button[1]")
        self.driver.execute_script("arguments[0].click();", arbitrationRulesFilter)
        filterArbitrationRules = self.driver.find_element(By.XPATH, "//*[@id='page-content']/div/div[5]/h2")
        filterArbitrationRulesText = filterArbitrationRules.text
        assert "Arbitration Rules" == filterArbitrationRulesText
        self.logger.info(filterArbitrationRulesText + " is displayed")
        #self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        #International Treaties & Rules Filter Type
        internationalTreatiesFilter = self.driver.find_element(By.XPATH, "//*[@id='articlecitator-filter-dropdown']/p[1]/button[2]")
        self.driver.execute_script("arguments[0].click();", internationalTreatiesFilter)
        filterInternationTreaties = self.driver.find_element(By.XPATH, "//*[@id='page-content']/div/div[6]/h2")
        filterInternationTreatiesText = filterInternationTreaties.text
        assert "International Treaties & Rules" == filterInternationTreatiesText
        self.logger.info(filterInternationTreatiesText + " is displayed")
        #Bilateral Investment Treaties (BITs) filter type
        bilateralInvestmentFilter = self.driver.find_element(By.XPATH, "// *[ @ id = 'articlecitator-filter-dropdown'] / p[1] / button[3]")
        self.driver.execute_script("arguments[0].click();", bilateralInvestmentFilter)
        filterBiLateral = self.driver.find_element(By.XPATH, "//*[@id='page-content']/div/div[7]/h2")
        filterBilateralText = filterBiLateral.text
        assert "Bilateral Investment Treaties (BITs)" == filterBilateralText
        self.logger.info(filterBilateralText + " is displayed")
        #Free Trade Agreement (FTAs)
        freeTradeFilter = self.driver.find_element(By.XPATH, "//*[@id='articlecitator-filter-dropdown']/p[1]/button[4]")
        self.driver.execute_script("arguments[0].click();", freeTradeFilter)
        filterFreeTrade = self.driver.find_element(By.XPATH, "//*[@id='page-content']/div/div[8]/h2")
        filterFreeTradeText = filterFreeTrade.text
        assert "Free Trade Agreement (FTAs)" == filterFreeTradeText
        self.logger.info(filterFreeTradeText + "  is displayed")
        #NAFTA
        naftaFilter = self.driver.find_element(By.XPATH, "//*[@id='articlecitator-filter-dropdown']/p[1]/button[5]")
        self.driver.execute_script("arguments[0].click();", naftaFilter)
        filterNafta = self.driver.find_element(By.XPATH, "//*[@id='page-content']/div/div[9]/h2")
        filterNaftaText = filterNafta.text
        assert "NAFTA" == filterNaftaText
        self.logger.info(filterNaftaText + " is displayed")
        #Regional/Sectoral Agreements
        regionalFilter = self.driver.find_element(By.XPATH, "//*[@id='articlecitator-filter-dropdown']/p[1]/button[6]")
        self.driver.execute_script("arguments[0].click();", regionalFilter)
        filterRegional = self.driver.find_element(By.XPATH, "//*[@id='page-content']/div/div[10]/h2")
        filterRegionalText = filterRegional.text
        assert "Regional/Sectoral Agreements" == filterRegionalText
        self.logger.info(filterRegionalText + "  is displayed")
        #National Investment Law
        nationalInvestmentFilter = self.driver.find_element(By.XPATH, "//*[@id='articlecitator-filter-dropdown-control']/span[7]")
        self.driver.execute_script("arguments[0].click();", nationalInvestmentFilter)
        #filterNationalInvestment = self.driver.find_element(By.XPATH, "")
        #Other
        otherFilter = self.driver.find_element(By.XPATH, "//*[@id='articlecitator-filter-dropdown']/p[1]/button[8]")
        self.driver.execute_script("arguments[0].click();", otherFilter)
        filterOther = self.driver.find_element(By.XPATH, "//*[@id='page-content']/div/div[11]/h2")
        filterOtherText = filterOther.text
        assert "Other" == filterOtherText
        self.logger.info(filterOtherText + "  is displayed")
        #Clear Filters
        clearFilters = self.driver.find_element(By.XPATH, "//*[@id='clear-filters']")
        self.driver.execute_script("arguments[0].click();", clearFilters)
        #Need validation but for now its good


    @pytest.mark.skip(reason="Takes longer to retrieve records")
    def test_testextract(self):
        self.logger.info("****TestCase AC-009 - Validate Find and Reset***")
        self.navigator = ArticleCitator(self.driver)
        self.navigator.clickOnArticleCitatormenu()
        time.sleep(2)
        self.navigator.clickOnClientListing()
        self.logger.info("Article Citator menu is available")
        time.sleep(2)
        current_url = self.driver.current_url
        print(current_url)
        # get requests
        response = requests.get(current_url)
        # check status code of the request
        response.status_code
        #create soup object
        soup = BeautifulSoup(response.content, 'html.parser')
        print(soup)
        #result items(starting)
        list_items = soup.findAll('div', {'class': 'ACCardData'})
        print(len(list_items))


