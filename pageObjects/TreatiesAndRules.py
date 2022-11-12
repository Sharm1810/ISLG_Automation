import time

import self
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from utilities.customLogger import LogGen

logger = LogGen.loggen()


class TreatiesAndRules:
    saerch_xpath = "//*[@id='txtTreatyRuleSearch']"
    treatiesAndRulesmenu_xpath = "//*[@id='ResearchToolMenu']/ul[2]/li[1]/a"
    clientListing_cssseelector = "#dvClientListing > div > button"
    find_xpath = "//*[@id='frmTreatiesRuleSearch']/div[2]/div[2]/button"
    reset_xpath = "//*[@id='dvTreatySearch']/a"
    filterType_xpath = "//*[@id='btnfilter-dropdown-control']"
    clearFilters_xpath = "//*[@id='filter-dropdown']/p[2]/a"
    researchNotepad_xpath = "(//div[@class='card__actions dropdown']//p//a)[1]"
    expandFirstLink_xpath = "(//div[@class='card__header']//a)[1]//i[1]"
    actions_xpath = "//div[@class='tabs hide-compact']//div//div//button"
    researchTopicOption_xpath = "//div[@class='card card--compact']//ul//li[1]//label"
    researchAdd_xpath = "//*[@id='btnAddRNSecond']"
    copyLocation_xpath = "(//div[@class='card__actions dropdown']//p//a)[2]"
    followTopic_xpath = "//span[@class='form__radio-label']//span"
    copyCitation_xpath = "(//div[@class='citationdiv']//p//small//a)[1]"
    instrumentDetailsTab_xpath = "(//div[@class='tabs__list']//a)[2]"
    expandThirdLink_xpath = "(//div[@class='card__header']//a)[3]"
    documentComparison_xpath = "(//div[@class='card__actions dropdown']//div//p//a)[3]"
    documentComparisonOption_xpath = "//*[@id='GroupSelection']/ul/li[1]/label/span/i"
    documentAdd_xpath = "//*[@id='btnGroupAdd']"



    def __init__(self, driver):
        self.driver = driver

    def clickOnTreatiesAndRules(self):
        self.driver.find_element(By.XPATH, self.treatiesAndRulesmenu_xpath).click()

        # Clicks on skip Client Listing

    def clickOnClientListing(self):
        self.driver.implicitly_wait(1000)
        self.driver.find_element_by_css_selector("#dvClientListing > div > button").click()
        self.driver.implicitly_wait(1000)

    def clickOnFind(self):
        find = self.driver.find_element(By.XPATH, self.find_xpath)
        self.driver.execute_script("arguments[0].click();", find)

    def clickOnReset(self):
        reset = self.driver.find_element(By.XPATH, self.reset_xpath)
        self.driver.execute_script("arguments[0].click();", reset)

    def clickOnFilterType(self):
        filter = self.driver.find_element(By.XPATH, self.filterType_xpath)
        self.driver.execute_script("arguments[0].click();", filter)

    def clickOnClearFilters(self):
        clearFilter = self.driver.find_element(By.XPATH, self.clearFilters_xpath)
        self.driver.execute_script("arguments[0].click();", clearFilter)

    def clickOnResearchNotepad(self):
        researchNotepad = self.driver.find_element(By.XPATH, self.researchNotepad_xpath )
        self.driver.execute_script("arguments[0].click();", researchNotepad)

    def clickOnExpandFirstLink(self):
        firstLink = self.driver.find_element(By.XPATH, self.expandFirstLink_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", firstLink)
        self.driver.execute_script("arguments[0].click();", firstLink)

    def clickOnActions(self):
        actions = self.driver.find_element(By.XPATH, self.actions_xpath)
        self.driver.execute_script("arguments[0].click();", actions)

    def clickOnAddResearchNotepad(self):
        researchTopic = self.driver.find_element(By.XPATH, self.researchTopicOption_xpath)
        self.driver.execute_script("arguments[0].click();", researchTopic)
        addButton = self.driver.find_element(By.XPATH, self.researchAdd_xpath)
        self.driver.execute_script("arguments[0].click();", addButton)

    def clickOnCopyLocation(self):
        location = self.driver.find_element(By.XPATH, self.copyLocation_xpath)
        self.driver.execute_script("arguments[0].click();", location)

    def clickOnFollowTopic(self):
        followTopic = self.driver.find_element(By.XPATH, self.followTopic_xpath)
        self.driver.execute_script("arguments[0].click();", followTopic)

    def clickOnCopyCitation(self):
        copyCitation = self.driver.find_element(By.XPATH, self.copyCitation_xpath)
        self.driver.execute_script("arguments[0].click();", copyCitation)

    def clickOnInstrumentDetails(self):
        instrumentDetails = self.driver.find_element(By.XPATH, self.instrumentDetailsTab_xpath)
        self.driver.execute_script("arguments[0].click();", instrumentDetails)

    def clickOnExpandThirdLink(self):
        expand = self.driver.find_element(By.XPATH, self.expandThirdLink_xpath)
        self.driver.execute_script("arguments[0].click();", expand)

    def clickOnDocumentComparison(self):
        document = self.driver.find_element(By.XPATH, self.documentComparison_xpath)
        self.driver.execute_script("arguments[0].click();", document)
        group = self.driver.find_element(By.XPATH, self.documentComparisonOption_xpath)
        self.driver.execute_script("arguments[0].click();", group)
        add = self.driver.find_element(By.XPATH, self.documentAdd_xpath)
        self.driver.execute_script("arguments[0].click();", add)











