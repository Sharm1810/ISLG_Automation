import time

import self
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from utilities.customLogger import LogGen

logger = LogGen.loggen()


class TermsAndPhrases:
    termsAndPhrases_xpath = "//*[@id='Rslink']/li[5]/a/span"
    expandBranch1_xpath = "//*[@id='TermPhraseIndexId-1-control']"
    expandBranch2_xpath = "//*[@id='TermPhraseIndexId-2-control']"
    expandBranch3_xpath = "//*[@id='TermPhraseIndexId-3-control']"
    expandBranch4_xpath = "//*[@id='TermPhraseIndexId-4-control']"
    expandBranch5_xpath = "//*[@id='TermPhraseIndexId-5-control']"
    expandBranch6_xpath = "//*[@id='TermPhraseIndexId-6-control']"
    expandBranch7_xpath = "//*[@id='TermPhraseIndexId-7-control']"
    expandBranch8_xpath = "//*[@id='TermPhraseIndexId-8-control']"
    expandBranch9_xpath = "//*[@id='TermPhraseIndexId-9-control']"
    expandBranch10_xpath = "//*[@id='TermPhraseIndexId-10-control']"
    expandBranch11_xpath = "//*[@id='TermPhraseIndexId-11-control']"
    expandBranch12_xpath = "//*[@id='TermPhraseIndexId-12-control']"
    expandBranch13_xpath = "//*[@id='TermPhraseIndexId-13-control']"
    expandBranch14_xpath = "//*[@id='TermPhraseIndexId-14-control']"
    expandBranch15_xpath = "//*[@id='TermPhraseIndexId-15-control']"
    expandBranch16_xpath = "//*[@id='TermPhraseIndexId-16-control']"
    expandBranch17_xpath = "//*[@id='TermPhraseIndexId-17-control']"
    expandBranch18_xpath = "//*[@id='TermPhraseIndexId-18-control']"
    expandBranch19_xpath = "//*[@id='TermPhraseIndexId-19-control']"
    expandBranch20_xpath = "//*[@id='TermPhraseIndexId-20-control']"
    expandBranch21_xpath = "//*[@id='TermPhraseIndexId-21-control']"
    expandBranch22_xpath = "//*[@id='TermPhraseIndexId-22-control']"
    expandBranch23_xpath = "//*[@id='TermPhraseIndexId-23-control']"
    expandBranch24_xpath = "//*[@id='TermPhraseIndexId-24-control']"
    expandBranch25_xpath = "//*[@id='TermPhraseIndexId-25-control']"
    expandBranch26_xpath = "//*[@id='TermPhraseIndexId-26-control']"
    clientListing_css_selector = "#dvClientListing > div > button"
    heading_xpath = "//*[@id='page-content']/div/div[3]/div/div[1]/h1"
    actions_xpath = "(//div[@class='card__actions dropdown']//button)[1]"
    researchNotepad_xpath = "(//div[@class='card__actions dropdown']//p//a)[1]"
    researchTopicOption1_xpath = "(//label[@class='form__radio']//input)[1]"
    researchAddButton_xpath = "//*[@id='btnAddRNFirst']"
    researchTopicOption2_xpath = "//*[@id='EntireTerm']"
    researchAddButton2_xpath = "//*[@id='btnAddRNTermSecond']"
    toastMessageResearchNotepad_xpath = "/html/body/div[7]/span[3]"
    copyLocation_xpath = "(//div[@class='card__actions dropdown']//p//a)[2]"
    toastMessageCopyLocation_xpath = "/html/body/div[7]/span[3]"
    followTopic_xpath = "(//div[@class='card__actions dropdown']//div//label//input)[1]"
    toastMessageFollowTopic_xpath = "/html/body/div[7]/span[3]"
    find_xpath = "//*[@id='frmTermSearchData']/div/div[2]/button"
    resetLink_xpath = "//*[@id='dvTermPhraseSearches']/a"
    fullCaseAnalysis_xpath = "(//div[@class = 'document__footer-right']//a)[1]"
    firstCardExpand_xpath = "(//p//a[@class='link--has-icon dropdown__toggle searchTermLinksData islg-page-view']//i)[1]"
    copyCitation_xpath = "(//div[@class='citationdiv']//p//a)[1]"
    cataloguedSN_xpath = "(//p[@class='pCatalogued']//a)[1]"
    paragraphExcerpt_xpath = "(//span[@class='tooltip-elem']//a)[1]"
    copyExcerpt_xpath = "(//small//a[@class='link--has-icon copy-excerpt'])[1]"
    textLink_xpath = "(//a[@class='link__text termSourceBookmarkTitle'])[1]"

    def __init__(self, driver):
        self.driver = driver

    # clicks on Terms And Phrases Navigation menu
    def clickOnTermsAndPhrases(self):
        self.driver.find_element(By.XPATH, self.termsAndPhrases_xpath).click()

        # Clicks on skip Client Listing

    def clickOnClientListing(self):
        self.driver.implicitly_wait(1000)
        self.driver.find_element(By.CSS_SELECTOR, self.clientListing_css_selector).click()
        self.driver.implicitly_wait(1000)

    def clickOnFirstBranch(self):
        firstBranch = self.driver.find_element(By.XPATH, self.expandBranch1_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", firstBranch)
        self.driver.execute_script("arguments[0].click();", firstBranch)

    def getHeading(self):
        heading = self.driver.find_element(By.XPATH, self.heading_xpath).text
        return heading

    def clickOnFourthBranch(self):
        fourthBranch = self.driver.find_element(By.XPATH, self.expandBranch4_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", fourthBranch)
        self.driver.execute_script("arguments[0].click();", fourthBranch)

    def clickOnTwentiethBranch(self):
        twentienthBranch = self.driver.find_element(By.XPATH, self.expandBranch20_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", twentienthBranch)
        self.driver.execute_script("arguments[0].click();", twentienthBranch)

    def clickOnTwentySixthBranch(self):
        twentySixthBranch = self.driver.find_element(By.XPATH, self.expandBranch26_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", twentySixthBranch)
        self.driver.execute_script("arguments[0].click();", twentySixthBranch)

    def clickOnActions(self):
        actions = self.driver.find_element(By.XPATH, self.actions_xpath)
        self.driver.execute_script("arguments[0].click();", actions)

    def clickOnAddtoResearchNotepad(self):
        researchNotepad = self.driver.find_element(By.XPATH, self.researchNotepad_xpath)
        self.driver.execute_script("arguments[0].click();", researchNotepad)

    def clickOnResearchTopicOption(self):
        researchTopicOption = self.driver.find_element(By.XPATH, self.researchTopicOption1_xpath)
        self.driver.execute_script("arguments[0].click();", researchTopicOption)

    def clickOnAddResearch(self):
        researchAdd = self.driver.find_element(By.XPATH, self.researchAddButton_xpath)
        self.driver.execute_script("arguments[0].click();", researchAdd)

    def clickOnAddResearchTopicOption2(self):
        researchAddTopicOption2 = self.driver.find_element(By.XPATH, self.researchTopicOption2_xpath)
        self.driver.execute_script("arguments[0].click();", researchAddTopicOption2)

    def clickOnAddResearchButton2(self):
        researchAddButton2 = self.driver.find_element(By.XPATH, self.researchAddButton2_xpath)
        self.driver.execute_script("arguments[0].click();", researchAddButton2)

    def getToastMessageResearch(self):
        toastMessage = self.driver.find_element(By.XPATH, self.toastMessageResearchNotepad_xpath)
        return toastMessage

    def clickOnCopyLocation(self):
        copyLocation = self.driver.find_element(By.XPATH, self.copyLocation_xpath)
        self.driver.execute_script("arguments[0].click();", copyLocation)

    def getToastMessageCopyLocation(self):
        toastMessage = self.driver.find_element(By.XPATH, self.toastMessageCopyLocation_xpath)
        return toastMessage

    def clickOnFollowTopic(self):
        followTopic = self.driver.find_element(By.XPATH, self.followTopic_xpath)
        self.driver.execute_script("arguments[0].click();", followTopic)

    def getToastMessageFollowTopic(self):
        toastMessage = self.driver.find_element(By.XPATH, self.toastMessageFollowTopic_xpath)
        return toastMessage

    def clickOnFind(self):
        find = self.driver.find_element(By.XPATH, self.find_xpath)
        self.driver.execute_script("arguments[0].click();", find)

    def clickOnReset(self):
        reset = self.driver.find_element(By.XPATH, self.resetLink_xpath)
        self.driver.execute_script("arguments[0].click();", reset)

    def clickOnFullCaseAnalysis(self):
        fullCaseAnalysis = self.driver.find_element(By.XPATH, self.fullCaseAnalysis_xpath)
        self.driver.execute_script("arguments[0].click();", fullCaseAnalysis)

    def clickOnExpandCard(self):
        expandCard = self.driver.find_element(By.XPATH, self.firstCardExpand_xpath)
        self.driver.execute_script("arguments[0].click();", expandCard)

    def clickOnCopyCitation(self):
        copyCitation = self.driver.find_element(By.XPATH, self.copyCitation_xpath)
        self.driver.execute_script("arguments[0].click();", copyCitation)

    def clickOnCatalogued(self):
        catalogue = self.driver.find_element(By.XPATH, self.cataloguedSN_xpath)
        self.driver.execute_script("arguments[0].click();", catalogue)

    def clickOnParagraphExcerpt(self):
        excerpt = self.driver.find_element(By.XPATH, self.paragraphExcerpt_xpath)
        self.driver.execute_script("arguments[0].click();", excerpt)

    def clickOnCopyExcerpt(self):
        excerptlink = self.driver.find_element(By.XPATH, self.copyExcerpt_xpath)
        self.driver.execute_script("arguments[0].click();", excerptlink)

    def clickOnTextLink(self):
        textlink = self.driver.find_element(By.XPATH, self.textLink_xpath)
        self.driver.execute_script("arguments[0].click();", textlink)

