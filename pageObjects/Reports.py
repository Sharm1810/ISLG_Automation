import time

import self
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from utilities.customLogger import LogGen

logger = LogGen.loggen()


class Reports:
    reports_xpath = "//*[@id='Rslink']/li[6]/a/span"
    selectReport_xpath = "//*[@id='txtAllReportSearch']"
    viewAllReports_xpath = "//*[@id='btnAllReportSearch']"
    viewAllDispute_xpath = "//*[@id='frmIndividual-14']/div/a[1]"
    comparisonReports_xpath = "//*[@id='page-content']/div/div/div[3]/div[2]/div[2]/a"
    disputeSelection_xpath = "//*[@id='search-14']"
    individualReports_xpath = "//*[@id='frmIndividual-14']/div/a[2]"
    peopleReports_xpath = "//*[@id='page-content']/div/div/div[4]/div[2]/div[2]/a"
    vieAllPeople_xpath = "//*[@id='frmIndividual-15']/div/a[1]"
    peopleSearch_xpath = "//*[@id='search-keyword']"
    searchIndividualPeople_xpath = "//*[@id='search-15']"
    viewIndividualReportsPeople_xpath = "//*[@id='frmIndividual-15']/div/a[2]"
    comparisonReportsOrg_xpath = "//*[@id='page-content']/div/div/div[5]/div[2]/div[2]/a"
    viewAllOrganizations_xpath = "//*[@id='frmIndividual-16']/div/a[1]"
    organizationSearch_xpath = "//*[@id='search-keyword']"
    searchIndividualOrg_xpath = "//*[@id='search-16']"
    viewIndividualReportsOrg_xpath = "//*[@id='frmIndividual-16']/div/a[2]"
    viewAllCountries_xpath = "//*[@id='frmIndividual-24']/div/a[1]"
    searchCountries_xpath = "//*[@id='search-keyword']"
    individualcountriesSearch_xpath = "//*[@id='search-24']"
    viewIndividualReportsCountries_xpath = "//*[@id='frmIndividual-24']/div/a[2]"
    comparativeCountries_xpath = "//*[@id='page-content']/div/div/div[6]/div[2]/div[2]/a"
    viewSavedReports_xpath = "//*[@id='page-content']/div/div/div[7]/div/div[2]/div/div[2]/a"
    addToNotepad_xpath = "//*[@id='frm-download-report']/a"
    researchTopicOption_xpath = "(//div[@class='card card--compact']//ul//li//label//input)[1]"
    addTopic_xpath = "//*[@id='btn-popup-add']"



    def __init__(self, driver):
        self.driver = driver

    def clickOnISLGReports(self):
        islgmenu = self.driver.find_element(By.XPATH, self.reports_xpath)
        self.driver.execute_script("arguments[0].click();", islgmenu)

    def clickOnselectReport(self):
        reportSelect = self.driver.find_element(By.XPATH, self.selectReport_xpath)
        self.driver.execute_script("arguments[0].click();", reportSelect)
        reportSelect.send_keys("Annul")

    def clickOnViewAllReports(self):
        viewReport = self.driver.find_element(By.XPATH, self.viewAllReports_xpath)
        self.driver.execute_script("arguments[0].click();", viewReport)

    def clickOnClientListing(self):
        self.driver.implicitly_wait(1000)
        self.driver.find_element_by_css_selector("#dvClientListing > div > button").click()
        self.driver.implicitly_wait(1000)

    def clickOnViewAllDispute(self):
        dispute = self.driver.find_element(By.XPATH, self.viewAllDispute_xpath)
        self.driver.execute_script("arguments[0].click();", dispute)

    def clickOnViewComparisonReport(self):
        comparisonReport = self.driver.find_element(By.XPATH, self.comparisonReports_xpath)
        self.driver.execute_script("arguments[0].click();", comparisonReport)

    def clickOnDisputeSelection(self):
        selectDispute = self.driver.find_element(By.XPATH, self.disputeSelection_xpath)
        self.driver.execute_script("arguments[0].click();", selectDispute)
        selectDispute.send_keys("spain")

    def clickOnViewIndividualReports(self):
        individualReports = self.driver.find_element(By.XPATH, self.individualReports_xpath)
        self.driver.execute_script("arguments[0].click();", individualReports)

    def clickOnPeopleComparisonReports(self):
        peopleReport = self.driver.find_element(By.XPATH, self.peopleReports_xpath)
        self.driver.execute_script("arguments[0].click();", peopleReport)

    def clickOnViewAllPeople(self):
        people = self.driver.find_element(By.XPATH, self.vieAllPeople_xpath)
        self.driver.execute_script("arguments[0].click();", people)

    def clickOnSearchPeople(self):
        searchPeople = self.driver.find_element(By.XPATH, "//*[@id='search-keyword']")
        searchPeople.click()
        searchPeople.send_keys("A")

    def clickOnViewIndividualPeople(self):
        search = self.driver.find_element(By.XPATH, self.searchIndividualPeople_xpath)
        search.click()
        search.send_keys("A. Manuel Garcia")

    def clickOnViewIndividualReportsPeople(self):
        reports = self.driver.find_element(By.XPATH, self.viewIndividualReportsPeople_xpath)
        self.driver.execute_script("arguments[0].click();", reports)

    def clickOnViewComparisonReportsOrg(self):
        reports = self.driver.find_element(By.XPATH, self.comparisonReportsOrg_xpath)
        self.driver.execute_script("arguments[0].click();", reports)

    def clickOnViewAllOrganizationReport(self):
        reports = self.driver.find_element(By.XPATH, self.viewAllOrganizations_xpath)
        self.driver.execute_script("arguments[0].click();", reports)

    def searchOrganization(self):
        search = self.driver.find_element(By.XPATH, self.organizationSearch_xpath)
        search.click()
        search.send_keys("11")

    def searchIndividualOrg(self):
        searchIndividual = self.driver.find_element(By.XPATH, "//*[@id='search-16']")
        searchIndividual.click()
        searchIndividual.send_keys("11")

    def clickOnViewIndividualReportsOrg(self):
        individualReportsOrg = self.driver.find_element(By.XPATH, self.viewIndividualReportsOrg_xpath)
        self.driver.execute_script("arguments[0].click();", individualReportsOrg)

    def clickOnViewAllCountries(self):
        countriesAll = self.driver.find_element(By.XPATH, self.viewAllCountries_xpath)
        self.driver.execute_script("arguments[0].click();", countriesAll)

    def searchCountries(self):
        search = self.driver.find_element(By.XPATH, self.searchCountries_xpath)
        search.click()
        search.send_keys("AL")

    def searchIndividualCountries(self):
        searchIndividual = self.driver.find_element(By.XPATH, self.individualcountriesSearch_xpath)
        searchIndividual.click()
        searchIndividual.send_keys("Aus")

    def clickOnIndivisualReportsCountrues(self):
        searchCountry = self.driver.find_element(By.XPATH, self.viewIndividualReportsCountries_xpath)
        self.driver.execute_script("arguments[0].click();", searchCountry)

    def clickOnViewComparativeReports(self):
        comparativeReports = self.driver.find_element(By.XPATH, self.comparativeCountries_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", comparativeReports)
        self.driver.execute_script("arguments[0].click();", comparativeReports)

    def clickOnViewYourSavedReports(self):
        savedReports = self.driver.find_element(By.XPATH, self.viewSavedReports_xpath)
        #self.driver.execute_script("arguments[0].scrollIntoView();", savedReports)
        self.driver.execute_script("arguments[0].click();", savedReports)

    def clickOnAddToNotepad(self):
        notepad = self.driver.find_element(By.XPATH, self.addToNotepad_xpath)
        self.driver.execute_script("arguments[0].click();", notepad)

    def selectResearchTopicOption(self):
        topic = self.driver.find_element(By.XPATH, self.researchTopicOption_xpath)
        self.driver.execute_script("arguments[0].click();", topic)

    def clickOnAddTopic(self):
        add = self.driver.find_element(By.XPATH, self.addTopic_xpath )
        self.driver.execute_script("arguments[0].click();", add)




