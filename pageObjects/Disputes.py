import time

import self
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from utilities.customLogger import LogGen

logger = LogGen.loggen()


class Disputes:
    search_xpath = "//*[@id='txtDDSearch']"
    reset_xpath = "//*[@id='dvDDSearchBranch']/a"
    disputesMenu_xpath = "//*[@id='ResearchToolMenu']/ul[2]/li[2]/a/span"
    firstLink_xpath = "(//div[@class='card card--basic dropdown']//div//a)[1]"
    copyCitation_xpath = "//span[@class='citationdiv']//p//small//a[1]"
    actions_xpath= "(//div[@class='card__actions dropdown']//button)[1]"
    research_xpath = "(//div[@class='card__actions dropdown']//p//a)[1]"
    researchTopicOption_xpath = "//div[@class='card card--compact']//ul//li[1]//label"
    researchAdd_xpath = "//*[@id='btn-popup-add']"
    copyLocation_xpath = "(//div[@class='card__actions dropdown']//p//a)[2]"
    followTopic_xpath = "(//label[@class='form__radio ResearchNotepadEnabled auto-login ']//span)[1]"
    allDisputeDetails_xpath = "(//p[@class='text--right']//a)[1]"

    def __init__(self, driver):
        self.driver = driver

    def clickOnDisputeDocuments(self):
        self.driver.find_element(By.XPATH, self.disputesMenu_xpath).click()

    # Clicks on skip Client Listing

    def clickOnClientListing(self):
        self.driver.implicitly_wait(1000)
        self.driver.find_element_by_css_selector("#dvClientListing > div > button").click()
        self.driver.implicitly_wait(1000)

    def clickOnSearch(self):
        filter = self.driver.find_element(By.XPATH, self.search_xpath)
        self.driver.execute_script("arguments[0].click();", filter)

    def clickOnReset(self):
        reset = self.driver.find_element(By.XPATH, self.reset_xpath)
        self.driver.execute_script("arguments[0].click();", reset)

    def clickOnFirstLink(self):
        firstLink = self.driver.find_element(By.XPATH, self.firstLink_xpath)
        self.driver.execute_script("arguments[0].click();", firstLink)

    def clickOnCopyCitation(self):
        citation = self.driver.find_element(By.XPATH, self.copyCitation_xpath)
        self.driver.execute_script("arguments[0].click();", citation)

    def clickOnActions(self):
        actions = self.driver.find_element(By.XPATH, self.actions_xpath)
        self.driver.execute_script("arguments[0].click();", actions)

    def clickOnResearchNotepad(self):
        research = self.driver.find_element(By.XPATH, self.research_xpath)
        self.driver.execute_script("arguments[0].click();", research)

    def clickOnAddResearchNotepad(self):
        researchTopic = self.driver.find_element(By.XPATH, self.researchTopicOption_xpath)
        self.driver.execute_script("arguments[0].click();", researchTopic)
        addButton = self.driver.find_element(By.XPATH, self.researchAdd_xpath)
        self.driver.execute_script("arguments[0].click();", addButton)

    def clickOnCopyLocation(self):
        location = self.driver.find_element(By.XPATH, self.copyLocation_xpath)
        self.driver.execute_script("arguments[0].click();", location)

    def clickOnFollowTopic(self):
        follow = self.driver.find_element(By.XPATH, self.followTopic_xpath)
        self.driver.execute_script("arguments[0].click();", follow)

    def clickOnAllDisputeDetails(self):
        disputeDetails = self.driver.find_element(By.XPATH, self.allDisputeDetails_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", disputeDetails)
        self.driver.execute_script("arguments[0].click();", disputeDetails)






