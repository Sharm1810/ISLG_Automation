import time

import self
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from utilities.customLogger import LogGen

logger = LogGen.loggen()


class PublicationCitator:
    publicationCitator_xpath = "//*[@id='Rslink']/li[4]/a/span"
    expandCitator_xpath = "(//div[@class='card__header']//a)[1]"
    copyCitation_xpath = "//div[@class='document']//span//p//small//a"
    actions_xpath = "//div[@class='dropdown card__actions']//button[1]"
    addToResearchNotepad_xpath = "(//div[@class='card__actions dropdown']//p//a)[1]"
    copyLocation_xpath = "(//div[@class='card__actions dropdown']//p//a)[2]"
    followTopic_xpath = "//div[@class='dropdown card__actions']//label"
    researchTopicPopUp_xpath = "//*[@id='popup-add-to-rn']"
    researchTopicOption_xpath = "(//label[@class='form__radio']//input)[1]"
    comments_xpath = "//*[@id='bookmark-comments']"
    researchTopicAddButton_xpath = "//*[@id='btn-popup-add-next']"
    researchTopicScreen2Option_xpath = "//*[@id='popup-add-to-rn']/div[1]/div[3]/div[1]/ul/li/label/span/i"
    researchTopicScreen2AddButton_xpath = "//*[@id='btn-popup-add']"
    find_xpath = "//*[@id='search-publication']"
    resetLink_xpath = "//*[@id='search-reset']"
    clientListing_css_selector = "#dvClientListing > div > button"
    getHeading_xpath = "//*[@id='page-content']/div/div/div[1]/div/div[1]/h1"
    collapseBranch_xpath = "//div[@class='card__header card__header--is-open']//a[1]"
    booksSubMenu_xpath = "//*[@id='PublicationCitatorMenu']/li[1]/a"
    dictionarySubMenu_xpath = "//*[@id='PublicationCitatorMenu']/li[2]/a"
    newsSubMenu_xpath = "//*[@id='PublicationCitatorMenu']/li[3]/a"
    otherSubMenu_xpath = "//*[@id='PublicationCitatorMenu']/li[4]/a"
    periodicalsSubMenu_xpath = "//*[@id='PublicationCitatorMenu']/li[5]/a"
    booksText_xpath = "//*[@id='publication-filter-dropdown-control']/span[1]"
    booksFirstPublication_xpath = "(//div[@class='item-list compact__container']//div)[1]"


    def __init__(self, driver):
        self.driver = driver

    # clicks on Jurisprudence Navigation menu
    def clickOnPublicationCitator(self):
        self.driver.find_element(By.XPATH, self.publicationCitator_xpath).click()

        # Clicks on skip Client Listing

    def clickOnClientListing(self):
        self.driver.implicitly_wait(1000)
        self.driver.find_element(By.CSS_SELECTOR, self.clientListing_css_selector).click()
        self.driver.implicitly_wait(1000)

    def clickOnFirstPublication(self):
        publicationBranch = self.driver.find_element(By.XPATH, self.expandCitator_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", publicationBranch)
        self.driver.execute_script("arguments[0].click();", publicationBranch)

    def clickOnCollapse(self):
        collapseBranch = self.driver.find_element(By.XPATH, self.collapseBranch_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", collapseBranch)
        self.driver.execute_script("arguments[0].click();", collapseBranch)

    def getHeading(self):
        subjectHeading = self.driver.find_element(By.XPATH, self.getHeading_xpath).get_attribute(
            "textContent")

    def clickOnCopyCitation(self):
        copyCitation = self.driver.find_element(By.XPATH, self.copyCitation_xpath)
        self.driver.execute_script("arguments[0].click();", copyCitation)

    def clickOnActions(self):
        actionsClick = self.driver.find_element(By.XPATH, self.actions_xpath)
        self.driver.execute_script("arguments[0].click();", actionsClick)

    def clickOnAddToResearch(self):
        researchClick = self.driver.find_element(By.XPATH, self.addToResearchNotepad_xpath)
        self.driver.execute_script("arguments[0].click();", researchClick)

    def clickOnResearchOption(self):
        researchClickOption = self.driver.find_element(By.XPATH, self.researchTopicOption_xpath)
        self.driver.execute_script("arguments[0].click();", researchClickOption)

    def enterResearchComments(self):
        researchComments = self.driver.find_element(By.XPATH, self.comments_xpath)
        researchComments.send_keys("Add to Research Notepad")

    def clickOnAddResearch(self):
        researchClickOption = self.driver.find_element(By.XPATH, self.researchTopicAddButton_xpath)
        self.driver.execute_script("arguments[0].click();", researchClickOption)

    def clickOnResearchOption2(self):
        researchClickOption2 = self.driver.find_element(By.XPATH, self.researchTopicScreen2Option_xpath)
        self.driver.execute_script("arguments[0].click();", researchClickOption2)

    def clickOnResearchOptionAdd2(self):
        researchClickOptionAdd2 = self.driver.find_element(By.XPATH, self.researchTopicScreen2AddButton_xpath)
        self.driver.execute_script("arguments[0].click();", researchClickOptionAdd2)

    def clickOnCopyLocation(self):
        copyLocation = self.driver.find_element(By.XPATH, self.copyLocation_xpath)
        self.driver.execute_script("arguments[0].click();", copyLocation)

    def clickOnFollowTopic(self):
        followTopic = self.driver.find_element(By.XPATH, self.followTopic_xpath)
        self.driver.execute_script("arguments[0].click();", followTopic)

    def clickOnBooks(self):
        booksSubmenu = self.driver.find_element(By.XPATH, self.booksSubMenu_xpath)
        self.driver.execute_script("arguments[0].click();", booksSubmenu)

    def getBooksFilter(self):
        booksFilterType = self.driver.find_element(By.XPATH, self.booksText_xpath).text
        print(booksFilterType)

    def clickOnBooksFirstPublication(self):
        firstPublication = self.driver.find_element(By.XPATH, self.booksFirstPublication_xpath)
        self.driver.execute_script("arguments[0].click();", firstPublication)

    def clickOnDictionary(self):
        dictionarySubmenu = self.driver.find_element(By.XPATH, self.dictionarySubMenu_xpath)
        self.driver.execute_script("arguments[0].click();", dictionarySubmenu)

    def clickOnDictionaryFirstPublication(self):
        firstPublication = self.driver.find_element(By.XPATH, self.booksFirstPublication_xpath)
        self.driver.execute_script("arguments[0].click();", firstPublication)

    def getDictionaryFilter(self):
        dictionaryFilterType = self.driver.find_element(By.XPATH, self.booksText_xpath).text
        print(dictionaryFilterType)

    def clickOnNewsOnline(self):
        newsOnlineSubmenu = self.driver.find_element(By.XPATH, self.newsSubMenu_xpath)
        self.driver.execute_script("arguments[0].click();", newsOnlineSubmenu)

    def clickOnOther(self):
        otherSubmenu = self.driver.find_element(By.XPATH, self.otherSubMenu_xpath)
        self.driver.execute_script("arguments[0].click();", otherSubmenu)

    def clickOnFind(self):
        find = self.driver.find_element(By.XPATH, self.find_xpath)
        self.driver.execute_script("arguments[0].click();", find)

    def clickOnReset(self):
        reset = self.driver.find_element(By.XPATH, self.resetLink_xpath)
        self.driver.execute_script("arguments[0].click();", reset)

    def clickOnPeriodicals(self):
        periodicalsSubmenu = self.driver.find_element(By.XPATH, self.periodicalsSubMenu_xpath)
        self.driver.execute_script("arguments[0].click();", periodicalsSubmenu)


