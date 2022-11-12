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
from pageObjects.Reports import Reports
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

chromeOptions = Options()
chromeOptions.add_experimental_option("pref", {"download.default_directory": "C:\DownloadedFiles"})
def assertEqual(result, param):
    pass



@pytest.mark.usefixtures("setup")
class Test_Reports:
    logger = LogGen.loggen()



    #@pytest.mark.skip(reason="None")
    def test_ViewReports(self):
        self.logger.info("****TestCase ISLG Reports-001 - Validate View All Reports***")
        self.logger.info("*****Login Successful****")
        self.logger.info("**** ISLG Reports testing *****")
        self.navigator = Reports(self.driver)
        self.navigator.clickOnISLGReports()
        self.logger.info("ISLG Reports menu was clicked")
        time.sleep(2)
        self.navigator.clickOnClientListing()
        self.navigator.clickOnselectReport()
        time.sleep(2)
        reportSelection = self.driver.find_elements(By.XPATH, "//*[@id='ui-id-4']")
        print(len(reportSelection))
        for results in reportSelection:
            print(results.text)
            self.logger.info(results.text)
            if results.text == "Annulment (Commitee Member)":
                print("record found")
                results.click()
                time.sleep(4)
                break
        self.navigator.clickOnViewAllReports()
        time.sleep(2)
        resultsFound = self.driver.find_element(By.XPATH, "//*[@id='divAllReport']/div/div[3]/div/div/div[1]/p[1]/a")
        print(resultsFound.text)
        resultsNoOfPages = self.driver.find_element(By.XPATH, "//*[@id='divAllReport']/div/div[4]/div/div/div/div[1]/p")
        self.logger.info(resultsFound.text + "  " + resultsNoOfPages.text)
        time.sleep(2)

    #@pytest.mark.skip(reason="None")
    def test_ViewAllDispute(self):
        self.logger.info("****TestCase ISLG Reports-002 - Validate View All Dispute***")
        self.logger.info("*****Login Successful****")
        self.logger.info("**** ISLG Reports testing *****")
        self.navigator = Reports(self.driver)
        self.navigator.clickOnISLGReports()
        self.logger.info("ISLG Reports menu was clicked")
        time.sleep(2)
        #self.navigator.clickOnClientListing()
        self.navigator.clickOnViewAllDispute()
        self.logger.info("Clicked on View All Dispute")
        time.sleep(2)
        navigationData = self.driver.find_element(By.XPATH, "//*[@id='page-content']/div/div/div/div/nav")
        self.logger.info(navigationData.text)
        resultsPerPage = self.driver.find_element(By.XPATH, "//*[@id='PageSize']")
        self.logger.info(resultsPerPage.text)
        validateFirstReportLink = self.driver.find_element(By.XPATH,
                                                           "//*[@id='divAllCAtegory']/div/div[3]/div[1]/div/div[1]/p[1]/a")
        time.sleep(2)
        validateFirstReportLink.click()
        self.logger.info("Clicked on the First Report Link")
        time.sleep(2)
        validateCaseName = self.driver.find_element(By.XPATH, "//*[@id='divIndividualReportDetails']/div[1]/div[1]/div")
        self.logger.info(validateCaseName.text)
        validateShortTitle = self.driver.find_element(By.XPATH,
                                                      "//*[@id='divIndividualReportDetails']/div[3]/div[1]/div")
        self.logger.info(validateShortTitle.text)
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//*[@id='page-content']/div/div/div[1]/div/nav/a[1]").click()
        self.logger.info("Clicked on to navigate to the ISLG Reports page")
        time.sleep(2)

    @pytest.mark.skip(reason="None")
    def test_ViewComparisonReports(self):
        self.logger.info("****TestCase ISLG Reports-003 - Validate View Comparison Reports***")
        self.logger.info("*****Login Successful****")
        self.logger.info("**** ISLG Reports testing *****")
        self.navigator = Reports(self.driver)
        self.navigator.clickOnISLGReports()
        self.logger.info("ISLG Reports menu was clicked")
        time.sleep(2)
        #self.navigator.clickOnClientListing()
        self.navigator.clickOnViewComparisonReport()
        clickOnFirstReportLink = self.driver.find_element(By.XPATH,
                                                          "//*[@id='page-content-1']/div[2]/div[1]/div[1]//a[1]")
        clickOnFirstReportLink.click()
        self.logger.info("Clicked on the First Link")
        time.sleep(2)
        navigationMenuData = self.driver.find_element(By.XPATH, "//*[@id='dv-single-report']/div[1]/div/nav")
        self.logger.info(navigationMenuData.text)
        time.sleep(2)
        reportsHeading = self.driver.find_element(By.XPATH, "//*[@id='page-content-1']/div/div/div[2]/div/p[1]/strong")
        self.logger.info(reportsHeading.text)
        # self.driver.find_element(By.XPATH, "//*[@id='dv-single-report']/div[1]/div/nav/a[1]").click()
        # self.logger.info("Clicked on to navigate to the ISLG Reports page")
        time.sleep(2)

    #@pytest.mark.skip(reason="None")
    def test_ViewIndividualReports(self):
        self.logger.info("****TestCase ISLG Reports-004 - Validate View Individual Reports***")
        self.logger.info("*****Login Successful****")
        self.logger.info("**** ISLG Reports testing *****")
        self.navigator = Reports(self.driver)
        self.navigator.clickOnISLGReports()
        self.logger.info("ISLG Reports menu was clicked")
        time.sleep(2)
        #self.navigator.clickOnClientListing()
        self.navigator.clickOnDisputeSelection()
        time.sleep(3)
        searchReports = self.driver.find_elements(By.XPATH, "//*[@id='ui-id-1']/li")
        print(len(searchReports))
        for results in searchReports:
            print(results.text)
            self.logger.info(results.text)
            if results.text == "Antin v. Spain":
                print("record found")
                results.click()
                time.sleep(4)
                break
            self.logger.info(results.text)
        self.navigator.clickOnViewIndividualReports()
        self.logger.info("Clicked on View Individual Reports")
        navigationBreadCrumb = self.driver.find_element(By.XPATH, "//*[@id='page-content']/div/div/div[1]")
        self.logger.info(navigationBreadCrumb.text)
        islgreports = self.driver.find_element(By.XPATH, "//*[@id='page-content']/div/div/div[1]/div/nav/a[1]/span")
        islgreports.click()
        self.logger.info("Clicked on to navigate to the ISLG Reports home")

    #@pytest.mark.skip(reason="None")
    def test_ViewComparisonReportsPeople(self):
        self.logger.info("****TestCase ISLG Reports-005 - Validate View People Comparison Reports***")
        self.logger.info("*****Login Successful****")
        self.logger.info("**** ISLG Reports testing *****")
        self.navigator = Reports(self.driver)
        self.navigator.clickOnISLGReports()
        self.logger.info("ISLG Reports menu was clicked")
        time.sleep(2)
        #self.navigator.clickOnClientListing()
        self.navigator.clickOnPeopleComparisonReports()
        self.logger.info("Clicked on People - View Comparison Reports")
        firstReportLink = self.driver.find_element(By.XPATH, "//*[@id='page-content-1']/div[2]/div[1]/div/a[1]")
        firstReportLink.click()
        self.logger.info("Clicked on the First Report Link")
        time.sleep(2)
        navigationBreadCrumbs = self.driver.find_element(By.XPATH, "//*[@id='dv-single-report']/div[1]/div/nav")
        self.logger.info(navigationBreadCrumbs.text)
        nameLink = self.driver.find_element(By.XPATH, "//*[@id='tblReportTable']/tbody/tr[2]/td[1]/a")
        nameLink.click()
        name = nameLink.text
        print(name)
        self.logger.info(name)
        self.logger.info("Clicked on the first name link")
        self.logger.info(nameLink.text)
        parent_handle = self.driver.current_window_handle
        print(parent_handle)
        time.sleep(2)
        all_handles = self.driver.window_handles
        print(all_handles)
        for handle in all_handles:
            if handle != parent_handle:
                self.driver.switch_to.window(handle)
                time.sleep(2)
                expand = self.driver.find_element(By.XPATH, "//*[@id='item--details-control']/span[1]")
                expand.click()
                self.logger.info("clicked on the expand link")
                personDetails = self.driver.find_element(By.XPATH,
                                                         "//*[@id='item--details']/div[1]/div[5]/div")
                details = personDetails.text
                print(details)
                self.logger.info(details)
                if details == name:
                    self.logger.info("name matches")
                self.driver.close()
        self.driver.switch_to.window(parent_handle)
        time.sleep(2)
        islgHome = self.driver.find_element(By.XPATH, "//*[@id='dv-single-report']/div[1]/div/nav/a[1]/span")
        islgHome.click()
        self.logger.info("Clicked on ISLG Report Home")

    #@pytest.mark.skip(reason="None")
    def test_ViewAllPeople(self):
        self.logger.info("****TestCase ISLG Reports-006 - Validate View All People***")
        self.logger.info("*****Login Successful****")
        self.logger.info("**** ISLG Reports testing *****")
        self.navigator = Reports(self.driver)
        self.navigator.clickOnISLGReports()
        self.logger.info("ISLG Reports menu was clicked")
        time.sleep(2)
        #self.navigator.clickOnClientListing()
        self.navigator.clickOnViewAllPeople()
        self.logger.info("Clicked on View All People")
        self.navigator.clickOnSearchPeople()
        time.sleep(2)
        search = self.driver.find_elements(By.XPATH, "//*[@id='ui-id-1']/li")
        for results in search:
            print(results.text)
            self.logger.info(results.text)
            if results.text == "A. A. Askarov":
                print("record found")
                results.click()
                time.sleep(4)
                break
            self.logger.info(results.text)

    #@pytest.mark.skip(reason="None")
    def test_ViewIndividualReportsPeople(self):
        self.logger.info("****TestCase ISLG Reports-007 - Validate View Individual FReports- People***")
        self.logger.info("*****Login Successful****")
        self.logger.info("**** ISLG Reports testing *****")
        self.navigator = Reports(self.driver)
        self.navigator.clickOnISLGReports()
        self.logger.info("ISLG Reports menu was clicked")
        time.sleep(2)
        #self.navigator.clickOnClientListing()
        self.navigator.clickOnViewIndividualPeople()
        searchPeople = self.driver.find_elements(By.XPATH, "//*[@id='ui-id-2']//li")
        print(len(searchPeople))
        for results in searchPeople:
            print(results.text)
            self.logger.info(results.text)
            if results.text == "A. Manuel Garcia":
                print("record found")
                results.click()
                time.sleep(4)
                break
            self.logger.info(results.text + "  was selected")
        self.navigator.clickOnViewIndividualReportsPeople()
        peopleBreadCrumbs = self.driver.find_element(By.XPATH, "//*[@id='page-content']/div/div/div[1]/div/nav")
        self.logger.info(peopleBreadCrumbs.text)
        islgReports = self.driver.find_element(By.XPATH, "//*[@id='page-content']/div/div/div[1]/div/nav/a[1]/span")
        islgReports.click()
        self.logger.info("Clicked on to navigate to ISLG Reports home")

    #@pytest.mark.skip(reason="None")
    def test_ViewComparisonReportsOrg(self):
        self.logger.info("****TestCase ISLG Reports-008 - Validate View Comparison Reports- Organization***")
        self.logger.info("*****Login Successful****")
        self.logger.info("**** ISLG Reports testing *****")
        self.navigator = Reports(self.driver)
        self.navigator.clickOnISLGReports()
        self.logger.info("ISLG Reports menu was clicked")
        time.sleep(2)
        #self.navigator.clickOnClientListing()
        self.navigator.clickOnViewComparisonReportsOrg()
        self.logger.info("Clicked on View Comparison Reports for Organization")
        getHeading = self.driver.find_element(By.XPATH, "//*[@id='page-content-1']/div[1]/div/div[1]/div[2]/h2")
        self.logger.info(getHeading.text)
        firstOrgLink = self.driver.find_element(By.XPATH, "//*[@id='page-content-1']/div[2]/div[1]/div/a")
        firstOrgLink.click()
        self.logger.info("Clicked on First Org Link")
        orgBreadCrumbs = self.driver.find_element(By.XPATH, "//*[@id='dv-single-report']/div[1]/div/nav")
        self.logger.info(orgBreadCrumbs.text)
        islgReports = self.driver.find_element(By.XPATH, "//*[@id='dv-single-report']/div[1]/div/nav/a[1]/span")
        islgReports.click()
        self.logger.info("Clicked on to navigate to the Reports home")

    #@pytest.mark.skip(reason="None")
    def test_ViewAllOrganizationReports(self):
        self.logger.info("****TestCase ISLG Reports-009 - Validate View All Organization Reports- Organization***")
        self.logger.info("*****Login Successful****")
        self.logger.info("**** ISLG Reports testing *****")
        self.navigator = Reports(self.driver)
        self.navigator.clickOnISLGReports()
        self.logger.info("ISLG Reports menu was clicked")
        time.sleep(2)
        #self.navigator.clickOnClientListing()
        time.sleep(2)
        self.navigator.clickOnViewAllOrganizationReport()
        self.navigator.searchOrganization()
        search = self.driver.find_elements(By.XPATH, "//*[@id='ui-id-1']//li")
        print(len(search))
        for results in search:
            print(results.text)
            self.logger.info(results.text)
            if results.text == "11 King's Bench Walk (KBW)":
                print("record found")
                self.logger.info(results.text)
                results.click()
                time.sleep(4)
                break
        firstLink = self.driver.find_element(By.XPATH, "(//div[@class='results__search']//div//div[2]//p//a)[1]")
        firstLink.click()
        #getHeading = self.logger.info(By.XPATH, "//*[@id='page-content-1']/div[1]/div[1]/div[1]/div[2]/h2")
        #self.logger.info(getHeading.text)
        navigationBreadCrumbs = self.driver.find_element(By.XPATH, "//*[@id='page-content']/div/div/div[1]/div/nav")
        self.logger.info(navigationBreadCrumbs.text)
        islgReports = self.driver.find_element(By.XPATH, "//*[@id='page-content']/div/div/div[1]/div/nav/a[1]/span")
        islgReports.click()

    #@pytest.mark.skip(reason="None")
    def test_ViewIndividualOrgReports(self):
        self.logger.info("****TestCase ISLG Reports-010 - Validate View Individual Org Reports- Organization***")
        self.logger.info("*****Login Successful****")
        self.logger.info("**** ISLG Reports testing *****")
        self.navigator = Reports(self.driver)
        self.navigator.clickOnISLGReports()
        self.logger.info("ISLG Reports menu was clicked")
        time.sleep(2)
        #self.navigator.clickOnClientListing()
        self.navigator.searchIndividualOrg()
        time.sleep(2)
        search = self.driver.find_elements(By.XPATH, "//*[@id='ui-id-3']//li")
        print(len(search))
        for results in search:
            print(results.text)
            self.logger.info(results.text)
            if results.text == "11 King's Bench Walk (KBW)":
                print("record found")
                self.logger.info(results.text)
                results.click()
                self.logger.info(results.text)
                time.sleep(4)
                break
        self.navigator.clickOnViewIndividualReportsOrg()
        orgBreadCrumbs = self.driver.find_element(By.XPATH, "//*[@id='page-content']/div/div/div[1]")
        self.logger.info(orgBreadCrumbs.text)
        islgReports = self.driver.find_element(By.XPATH, "//*[@id='page-content']/div/div/div[1]/div/nav/a[1]/span")
        islgReports.click()
        self.logger.info("Clicked on to navigate to the ISLG Report Home")

    #@pytest.mark.skip(reason="None")
    def test_ViewAllCountriesReports(self):
        self.logger.info("****TestCase ISLG Reports-011 - Validate View All Countries***")
        self.logger.info("*****Login Successful****")
        self.logger.info("**** ISLG Reports testing *****")
        self.navigator = Reports(self.driver)
        self.navigator.clickOnISLGReports()
        self.logger.info("ISLG Reports menu was clicked")
        time.sleep(2)
        #self.navigator.clickOnClientListing()
        time.sleep(2)
        self.navigator.clickOnViewAllCountries()
        self.logger.info("Clicked on View All Countries")
        time.sleep(2)
        self.navigator.searchCountries()
        time.sleep(2)
        search = self.driver.find_elements(By.XPATH, "//*[@id='ui-id-1']//li")
        print(len(search))
        for results in search:
            print(results.text)
            self.logger.info(results.text)
            if results.text == "Albania":
                print("record found")
                self.logger.info(results.text)
                results.click()
                self.logger.info(results.text)
                time.sleep(4)
                break
        countriesBreadcrmbs = self.driver.find_element(By.XPATH, "//*[@id='page-content']/div/div/div/div/nav")
        self.logger.info(countriesBreadcrmbs.text)
        self.driver.find_element(By.XPATH, "(//div[@class='results__search']//div[2]//p//a)[1]").click()
        self.logger.info("Clicked on the First Country link")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//*[@id='item--details-control']/i").click()
        time.sleep(2)
        self.logger.info("Clicked on Expand Countries link")
        time.sleep(2)
        getCountry = self.driver.find_element(By.XPATH, "//*[@id='item--details']/div[1]/div/div")
        self.logger.info(getCountry.text)
        islgReports = self.driver.find_element(By.XPATH, "//*[@id='page-content']/div/div/div/div/nav/a[1]/span")
        islgReports.click()
        self.logger.info("Clicked on to navigate to the ISLG Reports home")

    #@pytest.mark.skip(reason="None")
    def test_ViewIndividualCountryReports(self):
        self.logger.info("****TestCase ISLG Reports-012 - Validate Individual Countries***")
        self.logger.info("*****Login Successful****")
        self.logger.info("**** ISLG Reports testing *****")
        self.navigator = Reports(self.driver)
        self.navigator.clickOnISLGReports()
        self.logger.info("ISLG Reports menu was clicked")
        time.sleep(2)
        #self.navigator.clickOnClientListing()
        time.sleep(2)
        self.navigator.searchIndividualCountries()
        time.sleep(2)
        search = self.driver.find_elements(By.XPATH, "//*[@id='ui-id-4']//li")
        print(len(search))
        for results in search:
            print(results.text)
            self.logger.info(results.text)
            if results.text == "Australia":
                print("record found")
                self.logger.info(results.text)
                results.click()
                self.logger.info(results.text)
                time.sleep(4)
                break
        self.navigator.clickOnIndivisualReportsCountrues()
        self.logger.info("Clicked on View Individual Reports")
        self.driver.find_element(By.XPATH, "(//div[@class='card__lists']//div//a)[1]").click()
        time.sleep(2)
        navigationBreadCrumbs = self.driver.find_element(By.XPATH, "//*[@id='dv-single-report']/div[1]/div/nav")
        self.logger.info(navigationBreadCrumbs.text)
        islgReports = self.driver.find_element(By.XPATH, "//*[@id='dv-single-report']/div[1]/div/nav/a[1]/span")
        islgReports.click()
        self.logger.info("Clicked on to navigate to ISLG Reports home")

    #@pytest.mark.skip(reason="None")
    def test_ViewComparativeCountryReports(self):
        self.logger.info("****TestCase ISLG Reports-013 - Validate Comparative Countries***")
        self.logger.info("*****Login Successful****")
        self.logger.info("**** ISLG Reports testing *****")
        self.navigator = Reports(self.driver)
        self.navigator.clickOnISLGReports()
        self.logger.info("ISLG Reports menu was clicked")
        time.sleep(2)
        #self.navigator.clickOnClientListing()
        time.sleep(2)
        self.navigator.clickOnViewComparativeReports()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//div[@class='card__lists']//div//a[1]").click()
        time.sleep(2)
        countriesBreadCrumbs = self.driver.find_element(By.XPATH, "//*[@id='dv-single-report']/div[1]/div/nav")
        self.logger.info(countriesBreadCrumbs.text)
        islgReports = self.driver.find_element(By.XPATH, "//*[@id='dv-single-report']/div[1]/div/nav/a[1]/span")
        islgReports.click()
        self.logger.info("Clicked on to navigate to the ISLG Reports home")


    #@pytest.mark.skip(reason="None")
    def test_SavedReports(self):
        self.logger.info("****TestCase ISLG Reports-014 - Validate Saved Reports***")
        self.logger.info("*****Login Successful****")
        self.logger.info("**** ISLG Reports testing *****")
        self.navigator = Reports(self.driver)
        self.navigator.clickOnISLGReports()
        self.logger.info("ISLG Reports menu was clicked")
        time.sleep(2)
        #self.navigator.clickOnClientListing()
        time.sleep(2)
        self.navigator.clickOnViewYourSavedReports()
        time.sleep(3)
        self.logger.info("Clicked on Saved Reports")
        # self.driver.find_element(By.XPATH, "//*[@id='export-details-control']").click()
        # time.sleep(2)
        # self.logger.info("Clicked on Download Saved Reports")
        # excelFile = self.driver.find_element(By.XPATH,
        #                              "//*[@id='export-details']/p[1]/a")
        # excelFile.click()
        # time.sleep(2)
        # self.logger.info("Downloaded Excel File")
        # time.sleep(3)
        #self.driver.find_element(By.XPATH, "//*[@id='export-details-control']").click()
        #time.sleep(2)
        #self.logger.info("Clicked on Download Saved Reports")
        #pdfFile = self.driver.find_element(By.XPATH, "//*[@id='export-details']/p[2]/a")
        #pdfFile.click()
        #time.sleep(2)
        #self.logger.info("Downloaded File PDF")

    @pytest.mark.skip(reason="None")
    def test_DisputeAddToNotepad(self):
        self.logger.info("****TestCase ISLG Reports-015 - Comparative Reports - Add to Notepad ***")
        self.logger.info("*****Login Successful****")
        self.logger.info("**** ISLG Reports testing *****")
        self.navigator = Reports(self.driver)
        self.navigator.clickOnISLGReports()
        self.logger.info("ISLG Reports menu was clicked")
        time.sleep(2)
        #self.navigator.clickOnClientListing()
        time.sleep(2)
        self.navigator.clickOnViewComparisonReport()
        element = self.driver.find_element(By.XPATH, "(//div[@class='card__lists']//div//a)[1]").click()
        self.driver.execute_script("arguments[0].click();", element)
        time.sleep(2)
        self.navigator.clickOnAddToNotepad()
        time.sleep(2)
        self.navigator.selectResearchTopicOption()
        time.sleep(2)
        self.navigator.clickOnAddTopic()
        time.sleep(2)
        researchToastMessage = self.driver.find_element(By.XPATH, "/html/body/div[7]/span[3]").text
        #result = self.driver.execute_script("return arguments[0]", researchToastMessage)
        self.logger.info(researchToastMessage)

    #@pytest.mark.skip(reason="None")
    def test_PeopleAddToNotepad(self):
        self.logger.info("****TestCase ISLG Reports-016 - Comparative People Reports - Add to Notepad ***")
        self.logger.info("*****Login Successful****")
        self.logger.info("**** ISLG Reports testing *****")
        self.navigator = Reports(self.driver)
        self.navigator.clickOnISLGReports()
        self.logger.info("ISLG Reports menu was clicked")
        time.sleep(2)
        #self.navigator.clickOnClientListing()
        time.sleep(2)
        self.navigator.clickOnPeopleComparisonReports()
        element = self.driver.find_element(By.XPATH, "//div[@class='card__lists']//div//a[1]")
        self.driver.execute_script("arguments[0].click();", element)

        time.sleep(2)
        self.navigator.clickOnAddToNotepad()
        time.sleep(2)
        self.navigator.selectResearchTopicOption()
        time.sleep(2)
        self.navigator.clickOnAddTopic()
        time.sleep(2)
        researchToastMessage = self.driver.find_element(By.XPATH, "/html/body/div[7]/span[3]").text
        #result = self.driver.execute_script("return arguments[0]", researchToastMessage)
        self.logger.info(researchToastMessage)

    #@pytest.mark.skip(reason="None")
    def test_OrgAddToNotepad(self):
        self.logger.info("****TestCase ISLG Reports-017 - Organization Reports - Add to Notepad ***")
        self.logger.info("*****Login Successful****")
        self.logger.info("**** ISLG Reports testing *****")
        self.navigator = Reports(self.driver)
        self.navigator.clickOnISLGReports()
        self.logger.info("ISLG Reports menu was clicked")
        time.sleep(2)
        #self.navigator.clickOnClientListing()
        time.sleep(2)
        self.navigator.clickOnViewComparisonReportsOrg()
        element = self.driver.find_element(By.XPATH, "//div[@class='card__lists']//div//a[1]")
        self.driver.execute_script("arguments[0].click();", element)
        time.sleep(2)
        self.navigator.clickOnAddToNotepad()
        time.sleep(2)
        self.navigator.selectResearchTopicOption()
        time.sleep(2)
        self.navigator.clickOnAddTopic()
        time.sleep(2)
        researchToastMessage = self.driver.find_element(By.XPATH, "/html/body/div[7]/span[3]").text
        #result = self.driver.execute_script("return arguments[0]", researchToastMessage)
        self.logger.info(researchToastMessage)

    #@pytest.mark.skip(reason="None")
    def test_CountryAddToNotepad(self):
        self.logger.info("****TestCase ISLG Reports-018 - Country Reports - Add to Notepad ***")
        self.logger.info("*****Login Successful****")
        self.logger.info("**** ISLG Reports testing *****")
        self.navigator = Reports(self.driver)
        self.navigator.clickOnISLGReports()
        self.logger.info("ISLG Reports menu was clicked")
        time.sleep(2)
        #self.navigator.clickOnClientListing()
        time.sleep(2)
        self.navigator.clickOnViewComparativeReports()
        element = self.driver.find_element(By.XPATH, "//div[@class='card__lists']//div//a[1]")
        self.driver.execute_script("arguments[0].click();", element)
        time.sleep(2)
        self.navigator.clickOnAddToNotepad()
        time.sleep(2)
        self.navigator.selectResearchTopicOption()
        time.sleep(2)
        self.navigator.clickOnAddTopic()
        time.sleep(2)
        researchToastMessage = self.driver.find_element(By.XPATH, "/html/body/div[7]/span[3]").text
        #result = self.driver.execute_script("return arguments[0]", researchToastMessage)
        self.logger.info(researchToastMessage)




















