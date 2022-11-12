import time

import self
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from utilities.customLogger import LogGen

logger = LogGen.loggen()

class JursiprudenceCitator:
    jurisprudenceMenu_xpath = "//*[@id='Rslink']/li[3]/a/span"
    jurisprudenceHeading_xpath = "//*[@id='page-content']/div/div[1]/div[1]/div/div[1]/h1"
    clientListing_css_selector = "#dvClientListing > div > button"
    expandJurisprudence_xpath = "(//div[@class='card card--basic dropdown']//div//a)[1]"
    expandedJurisprudenceText_xpath = "(//div[@class='card card--basic dropdown']//div)[2]//p//small//strong"
    expandInnerDropdown_xpath = "(//div[@class='card card--basic card--inner dropdown']//a)[1]"
    copyCitation_xpath = "//div[@class='tabs__content-container']//div//div/div/div//p//small//a"
    disputeDetailsTab_xpath = "(//div[@class='tabs__list hide-compact']//a)[2]"
    allDisputeDetailsButton_xpath = "//div[@class='document__footer-right']//a[1]"
    expandProceedingDetailsDropdown_xpath = "(//div[@class='dropdown']//button//span)[1]"
    collapseProceedingDetailsDropdown_xpath = "(//div[@class='dropdown']//button//span)[2]"
    allDocumentsFromDispute_xpath = "//div[@class='document__footer-left']//p//a"
    actionsDropdown_xpath = "(//div[@class='card__actions dropdown']//button)[1]"
    addToResearchNotepad_xpath = "(//div[@class='card__actions dropdown']//p//a)[1]"
    addToDocumentComparison_xpath = "(//div[@class='card__actions dropdown']//p//a)[2]"
    copyLocation_xpath = "(//div[@class='card__actions dropdown']//p//a)[3]"
    followTopic_xpath = "(//div[@class='card__actions dropdown']//div//label//input)[1]"
    search_xpath = "//*[@id='txtJurisprudenceSearch']"
    find_xpath = "//*[@id='JurisprudenceFind']"
    reset_xpath="//*[@id='page-content']/div/div[1]/div[2]/div[1]/a"
    clearFilters_xpath = "//*[@id='filter-dropdown']/p[2]/a"
    toggleFilterByType_xpath = "//*[@id='filter-dropdown-control']"

    def __init__(self, driver):
        self.driver = driver

    #clicks on Jurisprudence Navigation menu
    def clickOnJurisprudenceMenu(self):
        self.driver.find_element(By.XPATH, self.jurisprudenceMenu_xpath).click()

    #Clicks on skip Client Listing
    def clickOnClientListing(self):
        self.driver.implicitly_wait(1000)
        self.driver.find_element(By.CSS_SELECTOR, self.clientListing_css_selector).click()
        self.driver.implicitly_wait(1000)

    def getHeading(self):
        subjectHeading = self.driver.find_element(By.XPATH, self.jurisprudenceHeading_xpath).click()

    def clickOnFirstJurisprudence(self):
        jurisprudenceBranch = self.driver.find_element(By.XPATH, self.expandJurisprudence_xpath )
        self.driver.execute_script("arguments[0].scrollIntoView();", jurisprudenceBranch)
        self.driver.execute_script("arguments[0].click();", jurisprudenceBranch)


