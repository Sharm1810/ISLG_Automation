import time

import self
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from utilities.customLogger import LogGen

logger = LogGen.loggen()


class JurisprudenceCitator:
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
    reset_xpath = "//*[@id='page-content']/div/div[1]/div[2]/div[1]/a"
    clearFilters_xpath = "//*[@id='filter-dropdown']/p[2]/a"
    toggleFilterByType_xpath = "//*[@id='filter-dropdown-control']"
    citationCopiedToastMessage_xpath = "/html/body/div[7]/span[3]"
    researchOptions_xpath = "(//label[@class='form__radio']//input)[1]"
    researchComments_xpath = "//*[@id='Comments']"
    researchAddButton_xpath = "//*[@id='btnAddRNFirst']"
    researchEntireDocument_xpath = "//*[@id='EntireDocument']"
    researchButtonAddSecond_xpath = "//*[@id='btnAddRNSecond']"
    researchToastMessage_xpath = "/html/body/div[7]/span[3]"
    comparisonGroupOption_xpath = "//*[@id='popup-add-to-dc']/div[1]/div[2]/ul/li[1]/label/span"
    addComparison_xpath = "//*[@id='btnGroupAdd']"
    comparisonGroupToastMessage = "/html/body/div[7]/span[3]"
    allDisputeDetailsText = "//*[@id='page-content']/div/div[1]/p/span[2]/strong/text()"
    proceedingDetails_xpath = "//div[@class='table__wrapper']//strong//a[1]"



    def __init__(self, driver):
        self.driver = driver

    # clicks on Jurisprudence Navigation menu
    def clickOnJurisprudenceMenu(self):
        self.driver.find_element(By.XPATH, self.jurisprudenceMenu_xpath).click()

    # Clicks on skip Client Listing
    def clickOnClientListing(self):
        self.driver.implicitly_wait(1000)
        self.driver.find_element(By.CSS_SELECTOR, self.clientListing_css_selector).click()
        self.driver.implicitly_wait(1000)

    def getHeading(self):
        subjectHeading = self.driver.find_element(By.XPATH, self.jurisprudenceHeading_xpath).get_attribute(
            "textContent")

    def clickOnFirstJurisprudence(self):
        jurisprudenceBranch = self.driver.find_element(By.XPATH, self.expandJurisprudence_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", jurisprudenceBranch)
        self.driver.execute_script("arguments[0].click();", jurisprudenceBranch)

    def clickOnCollapse(self):
        collapseBranch = self.driver.find_element(By.XPATH, self.expandJurisprudence_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", collapseBranch)
        self.driver.execute_script("arguments[0].click();", collapseBranch)

    def clickOnInnerDropdown(self):
        innerDropdown = self.driver.find_element(By.XPATH, self.expandInnerDropdown_xpath)
        self.driver.execute_script("arguments[0].click();", innerDropdown)

    def clickOnCopyCitation(self):
        copyCitation = self.driver.find_element(By.XPATH, self.copyCitation_xpath)
        self.driver.execute_script("arguments[0].click();", copyCitation)

    def getCopyCitationMessage(self):
        copyCitationToastMessage = self.driver.find_element(By.XPATH, self.citationCopiedToastMessage_xpath).text
        result = self.driver.execute_script("return arguments[0]", copyCitationToastMessage)

    def clickOnActions(self):
        actionsDropdown = self.driver.find_element(By.XPATH, self.actionsDropdown_xpath)
        self.driver.execute_script("arguments[0].click();", actionsDropdown)

    def clickOnAddToResearch(self):
        addToResearch = self.driver.find_element(By.XPATH, self.addToResearchNotepad_xpath)
        self.driver.execute_script("arguments[0].click();", addToResearch)

    def clickOnResearchOption(self):
        researchOption = self.driver.find_element(By.XPATH, self.researchOptions_xpath)
        self.driver.execute_script("arguments[0].click();", researchOption)

    def clickOnAddResearch(self):
        addResearch = self.driver.find_element(By.XPATH, self. researchAddButton_xpath)
        self.driver.execute_script("arguments[0].click();", addResearch)

    def enterResearchComments(self):
        commentsResearch = self.driver.find_element(By.XPATH, self.researchComments_xpath)
        commentsResearch.send_keys("Add to Research Notepad")

    def clickOnResearchEntireDocument(self):
        entireDocument = self.driver.find_element(By.XPATH, self.researchEntireDocument_xpath)
        self.driver.execute_script("arguments[0].click();", entireDocument)

    def clickOnResearchAddSecond(self):
        addResearchSecond = self.driver.find_element(By.XPATH, self.researchButtonAddSecond_xpath)
        self.driver.execute_script("arguments[0].click();", addResearchSecond)

    def getResearchNotepadToastMessage(self):
        researchToastMessage = self.driver.find_element(By.XPATH, self.researchToastMessage_xpath).text
        result = self.driver.execute_script("return arguments[0]", researchToastMessage)

    def clickOnDocumentComparison(self):
        documentComparison = self.driver.find_element(By.XPATH, self.addToDocumentComparison_xpath)
        self.driver.execute_script("arguments[0].click();", documentComparison)

    def clickOnDocumentComparisonGroup(self):
        documentComparisonGroup = self.driver.find_element(By.XPATH, self.comparisonGroupOption_xpath)
        self.driver.execute_script("arguments[0].click();", documentComparisonGroup)

    def clickOnAddDocumentComparisonGroup(self):
        documentComparisonAddGroup = self.driver.find_element(By.XPATH, self.addComparison_xpath)
        self.driver.execute_script("arguments[0].click();", documentComparisonAddGroup)


    def clickOnFollowTopic(self):
        followTopic = self.driver.find_element(By.XPATH, self.followTopic_xpath)
        self.driver.execute_script("arguments[0].click();", followTopic)

    def clickOnCopyLocation(self):
        copyLocation = self.driver.find_element(By.XPATH, self.copyLocation_xpath)
        self.driver.execute_script("arguments[0].click();", copyLocation)

    def clickOnDisputeDetailsTab(self):
        disputeDetailsTab = self.driver.find_element(By.XPATH, self.disputeDetailsTab_xpath)
        self.driver.execute_script("arguments[0].click();", disputeDetailsTab)

    def clickOnAllDisputeDetails(self):
        allDisputeDetails = self.driver.find_element(By.XPATH, self.allDisputeDetailsButton_xpath)
        self.driver.execute_script("arguments[0].click();", allDisputeDetails)

    def clickOnAllDocumentsFromDispute(self):
        allDocuments = self.driver.find_element(By.XPATH, self. allDocumentsFromDispute_xpath)
        self.driver.execute_script("arguments[0].click();", allDocuments)

    def clickOnExpandProceedingDetails(self):
        expandProceedingDetails = self.driver.find_element(By.XPATH, self.expandProceedingDetailsDropdown_xpath)
        self.driver.execute_script("arguments[0].click();", expandProceedingDetails)

    def clickOnExpandProceedingDetailsTribunal(self):
        expandProceedingDetailsTribunal = self.driver.find_element(By.XPATH, self.proceedingDetails_xpath)
        self.driver.execute_script("arguments[0].click();", expandProceedingDetailsTribunal)

    def clickOnFind(self):
        find = self.driver.find_element(By.XPATH, self.find_xpath)
        self.driver.execute_script("arguments[0].click();", find)

    def clickOnReset(self):
        reset = self.driver.find_element(By.XPATH, self.reset_xpath)
        self.driver.execute_script("arguments[0].click();", reset)
