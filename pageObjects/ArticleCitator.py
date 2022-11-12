import time

import self
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from pageObjects.BasePage import BasePage
from utilities.customLogger import LogGen

logger = LogGen.loggen()


class ArticleCitator(BasePage):
    articleCitatormenu_cssselector = "#Rslink > li:nth-child(2) > a"
    clientListing_cssseelector = "#dvClientListing > div > button"
    firstBranchExpand_cssselector = "#page-content > div > div:nth-child(9) > div > div:nth-child(1) > div > div.card__header > a.cursor--pointer.card__title.dropdown__toggle.acTitleClick"
    elementActions_xpath = "//div[@class='tabs']//div//div//button[normalize-space()='Actions']"
    elementResearchNotepad_xpath = "//div[@role='tablist']//a[@title='Add to Research Notepad'][normalize-space("")='Research Notepad']"
    researchTopicOption_cssselector = "#popup-add-to-rn > div.scrolling-content > div:nth-child(3) > div ""> ul > li:nth-child(2) > label"
    researchAddbutton_xpath = "//*[@id='btn-popup-add-next']"
    # doucmentComparison_xpath = "//div[@role='tablist']//a[@title='Add to Document Comparison'][normalize-space()='Document Comparison']"
    addDocumentoption_xpath = "//*[@id='popup-add-to-rn']/div[1]/div[3]/div[1]/ul/li/label"
    addEntireDocumentAdd_xpath = "//*[@id='btn-popup-add']"
    toastMessageResearch_xpath = "/html/body/div[7]/span[3]"
    documentComparison_xpath = "//div[@class='card card--details']//div[@class='tabs']//div//div//p//a[2]"
    documentComparisonOption_xpath = "//*[@id='popup-add-to-dc']/div[1]/div[2]/ul/li[1]/label/span"
    documentComparisonAdd_xpath = "//*[@id='btn-comparison-add']"
    toastMessageDocumentComparison_xpath = "/html/body/div[7]/span[3]"
    copyLocation_xpath = "//div[@class='tabs__list hide-compact']//div//div//p//a[3]"
    followTopicOption_xpath = "//div[@class='tabs__list hide-compact']//div//label//span//span"
    toastMessageFollowTopic_xpath = "/html/body/div[7]/span[3]"
    # thirtyFirstBranchExpand_cssselector= "#page-content > div > div:nth-child(9) > div > div:nth-child(31) > div >
    # div.card__header.card__header--is-open > a.cursor--pointer.card__title.dropdown__toggle.acTitleClick"
    thirtyFirstBranchExpand_xpath = "//*[@id='page-content']/div/div[5]/div/div[26]/div/div[1]/a[2]"
    expand_xpath = "//*[@id='item-list-item-card-7']/div/button"
    provisiontab_xpath = "//body/main[@class='main']/section/div[@class='container']/div[@class='articlecategory']/div[@class='item-list card-list compact__container']/div[20]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/a[1]"
    instrumentDetailstab_xpath = "//*[@id='item-list-item-card-7-tab-2']"
    provisionTabDisplay_xpath = "//body/main[@class='main']/section/div[@class='container']/div[@class='articlecategory']/div[@class='item-list card-list compact__container']/div[20]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/a[1]"
    copyCitation_cssselector = "#item-list-item-card-7-tab-1-content > div > div.hide-compact > div.citationdiv > p > small > a > i"
    toastMessageCopyCitation_xpath = "/html/body/div[7]/span[3]"
    provisionLabelValidFrom_xpath = "//*[@id='item-list-item-card-7-tab-1-content']/div/div[1]/div[2]/div[1]/p/small"
    provisionTabFind_xpath = "//*[@id='provisiondata_10701']/div/div/div[2]/div/input"
    instrumentDetTab_xpath = "//a[normalize-space()='Instrument Details']"
    findButton_xpath = "//button[@id='btn-search-articlecitator-citator']"
    resetLink_xpath = "//*[@id='search-reset']"

    def __init__(self, driver):
        super().__init__(driver)

    def clickOnArticleCitatormenu(self):
        self.driver.find_element_by_css_selector(self.articleCitatormenu_cssselector).click()

    def clickOnClientListing(self):
        self.driver.implicitly_wait(1000)
        self.driver.find_element(By.XPATH, "//*[@id='dvClientListing']/div/button").click()
        self.driver.implicitly_wait(1000)

    def clickOnexpandBranch(self):
        expandbranch = self.driver.find_element(By.CSS_SELECTOR, self.firstBranchExpand_cssselector)
        self.driver.execute_script("arguments[0].click();", expandbranch)

    def clickOnActions(self):
        elementActions = self.driver.find_element(By.XPATH, self.elementActions_xpath)
        self.driver.execute_script("arguments[0].click();", elementActions)

    def clickOnResearchNotepad(self):
        elementResearchNotepad = self.driver.find_element(By.XPATH, self.elementResearchNotepad_xpath)
        self.driver.execute_script("arguments[0].click();", elementResearchNotepad)

    def clickOnResearchTopicOption(self):
        elementResearchTopic = self.driver.find_element(By.CSS_SELECTOR, self.researchTopicOption_cssselector)
        self.driver.execute_script("arguments[0].click();", elementResearchTopic)

    def clickOnAddResearch(self):
        elementAddResearch = self.driver.find_element(By.XPATH, self.researchAddbutton_xpath)
        self.driver.execute_script("arguments[0].click();", elementAddResearch)

    def clickOnDocumentCompariosn(self):
        elementDocumentComparison = self.driver.find_element(By.XPATH, self.doucmentComparison_xpath)
        self.driver.execute_script("arguments[0].click();", elementDocumentComparison)

    def clickOnEntireDocument(self):
        elementEntireDocument = self.driver.find_element(By.XPATH, self.addDocumentoption_xpath)
        self.driver.execute_script("arguments[0].click();", elementEntireDocument)

    def clickOnEntireDocumentAdd(self):
        elementEntireDocAdd = self.driver.find_element(By.XPATH, self.addEntireDocumentAdd_xpath)
        self.driver.execute_script("arguments[0].click();", elementEntireDocAdd)

    def getToastMessageResearch(self):
        elementResearchText = self.driver.find_element(By.XPATH, self.toastMessageResearch_xpath).text
        print(elementResearchText)

    def clickOnDocumentComparison(self):
        elementDocumentComparison = self.driver.find_element(By.XPATH, self.documentComparison_xpath)
        self.driver.execute_script("arguments[0].click();", elementDocumentComparison)

    def selectDocumentComparisonOption(self):
        selectOptionComparison = self.driver.find_element(By.XPATH, self.documentComparisonOption_xpath)
        self.driver.execute_script("arguments[0].click();", selectOptionComparison)

    def clickOnAddDocumentComparison(self):
        addDocumentComparison = self.driver.find_element(By.XPATH, self.documentComparisonAdd_xpath)
        self.driver.execute_script("arguments[0].click();", addDocumentComparison)

    def getToastMessageDocument(self):
        elementDocumentText = self.driver.find_element(By.XPATH, self.toastMessageDocumentComparison_xpath).text
        print(elementDocumentText)

    def clickOnCopyLocation(self):
        copyLocation = self.driver.find_element(By.XPATH, self.copyLocation_xpath)
        self.driver.execute_script("arguments[0].click();", copyLocation)

    def clickOnFollowTopic(self):
        followTopic = self.driver.find_element(By.XPATH, self.followTopicOption_xpath)
        self.driver.execute_script("arguments[0].click();", followTopic)

    def getToastMessageFollowTopic(self):
        elementFollowTopicText = self.driver.find_element(By.XPATH, self.toastMessageFollowTopic_xpath).text
        print(elementFollowTopicText)

    def clickOnexpandThirtyFirstBranch(self):
        expandbranchthirtyone = self.driver.find_element(By.XPATH, self.thirtyFirstBranchExpand_xpath)
        self.driver.execute_script("arguments[0].click();", expandbranchthirtyone)

    def clickOnCollapse(self):
        collapse = self.driver.find_element(By.XPATH, self.expand_xpath)
        self.driver.execute_script("arguments[0].click();", collapse)

    def checkProvisonTab(self):
        provisionTab = self.driver.find_element(By.XPATH, self.provisiontab_xpath).text

    def checkInstrumentDetails(self):
        instrumentTab = self.driver.find_element(By.XPATH, self.instrumentDetailstab_xpath).text

    def clickOnProvisionTab(self):
        provisionTabClick = self.driver.find_element(By.XPATH, self.provisionTabDisplay_xpath)
        self.driver.execute_script("arguments[0].click();", provisionTabClick)

    def clickOnCopyCitation(self):
        copyCitation = self.driver.find_element(By.CSS_SELECTOR, self.copyCitation_cssselector)
        self.driver.execute_script("arguments[0].click();", copyCitation)

    def getToastMessageCopyCitation(self):
        elementCopyCitationText = self.driver.find_element(By.XPATH, self.toastMessageCopyCitation_xpath).text

    def getProvisionTabDetails(self):
        validFrom = self.driver.find_element(By.XPATH, self.provisionLabelValidFrom_xpath).text
        print(validFrom)

    def provisionTabFind(self):
        provisionFind = self.driver.find_element(By.XPATH, self.provisionTabFind_xpath)
        provisionFind.send_keys("Generally")

    def clickOnInstrumentDetailsTab(self):
        detailsTab = self.driver.find_element(By.XPATH, self.instrumentDetTab_xpath)
        self.driver.execute_script("arguments[0].click();", detailsTab)
        try:
            # identify element
            s = detailsTab.text
            print("Element exist -" + s)

        # NoSuchElementException thrown if not present
        except NoSuchElementException:
            print("Element does not exist")

    def clickOnFind(self):
        findBtn = self.driver.find_element(By.XPATH, self.findButton_xpath)
        self.driver.execute_script("arguments[0].click();", findBtn)

    def clickOnReset(self):
        resetLink = self.driver.find_element(By.XPATH, self.resetLink_xpath)
        self.driver.execute_script("arguments[0].click();", resetLink)
