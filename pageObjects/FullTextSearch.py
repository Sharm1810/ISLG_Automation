import time

import self
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from utilities.customLogger import LogGen

logger = LogGen.loggen()


class FullTextSearch:
    fullTextSearch_xpath = "//*[@id='Rslink']/li[7]/a/span"
    search_xpath = "//*[@id='btnSearch']"
    resetLink_css_selector = "   self.driver.find_element(By.CSS_SELECTOR, "  # page-content > div > div > div.form__set.form__set--inline > div.form__group.form__group--wide > a")
    searchTextBox_xpath = "//*[@id='btnSearch']"
    allWordsOption_xpath = "//*[@id='StaticFilters']/div[1]/div[1]/fieldset/label[1]/span"
    anyWordsOption_xpath = "//*[@id='StaticFilters']/div[1]/div[1]/fieldset/label[2]/span"
    boolean_xpath = "//*[@id='StaticFilters']/div[1]/div[1]/fieldset/label[3]/span/i"
    expandSearchType_xpath = "//*[@id='search-type-dropdown-control']/i"
    stemming_xpath = "// *[ @ id = 'StaticFilters'] / div[2] / div[1] / fieldset / label[1] / span / span"
    synonyms_xpath = "//*[@id='StaticFilters']/div[2]/div[1]/fieldset/label[2]/span"
    fuzzyTypo_xpath = "//*[@id='StaticFilters']/div[2]/div[1]/fieldset/label[3]/span"
    fuzyyTypoNumbers_xpath = "//*[@id='fuzzy-typo']"
    disputeDocumentCheckBox_xpath = "//*[@id='StaticFilters']/div[3]/div[2]/div/fieldset/div[1]/div/div[1]/label/span/text()"
    arbitrationRulesCheckBox_xpath = "//*[@id='StaticFilters']/div[3]/div[2]/div/fieldset/div[1]/div/div[2]/label/span"
    treatiesAndRulesCheckBox_xpath = "//*[@id='StaticFilters']/div[3]/div[2]/div/fieldset/div[1]/div/div[3]/label/span/text()"
    documentTypeDropdown_xpath = "//*[@id='StaticFilters']/div[3]/div[2]/div/fieldset/div[2]/div/div[1]/div/div/span/span[1]/span/ul/li/input"
    arbitrationRulesDropdown_xpath = "//*[@id='StaticFilters']/div[3]/div[2]/div/fieldset/div[2]/div/div[2]/div/div/span/span[1]/span/ul/li/input"
    treatiesAndRulesDropdown_xpath = "//*[@id='StaticFilters']/div[3]/div[2]/div/fieldset/div[2]/div/div[3]/div/div/span/span[1]/span/ul/li/input"
    respondentSateDropdown_xpath = "//*[@id='StaticFilters']/div[4]/div[1]/div/span/span[1]/span/ul/li/input"
    applicableInstrumentsDropdown_xpath = "//*[@id='StaticFilters']/div[4]/div[2]/div/span/span[1]/span/ul/li/input"
    applicableArbitrationRulesDropdown_xpath = "//*[@id='StaticFilters']/div[4]/div[3]/div/span/span[1]/span/ul/li/input"
    clientListing_css_selector = "#dvClientListing > div > button"
    fulltextHeading_xpath = "//*[@id='page-content']/div/div/div[1]/div/div[1]/h1"
    copyCitation_xpath = "//div[@class = 'citationdiv']//p//small//a[1]"
    researchNotepad_xpath = "//div[@id='fts-actions']//p//a[1]"
    actions_xpath = "//*[@id='fts-actions-control']"
    researchTopicOption_xpath = "//div[@class='card card--compact']//ul//li[1]//label"
    researchAdd_xpath = "//*[@id='btn-popup-add']"
    editBasicFiltersDispute_xpath = "//*[@id='page-content']/div/div[1]/div[5]/div[2]/div/button/i"
    arbitratioCheck_xpath = "//*[@id='search__filters']/div[1]/div[2]/div[2]/div/fieldset/div[1]/div/div[2]/label/span/span/i"
    treatiesCheck_xpath = "//*[@id='search__filters']/div[1]/div[2]/div[2]/div/fieldset/div[1]/div/div[3]/label/span/span/i"
    submitSearch_xpath = "//*[@id='btnBasicFilter']"
    disputeCheck_xpath = "//*[@id='search__filters']/div[1]/div[2]/div[2]/div/fieldset/div[1]/div/div[1]/label/span"
    allWords_xpath = "//*[@id='page-content']/div/div[1]/div[4]/div[1]/fieldset/label[1]/span/i"
    anyWords_xpath = "//*[@id='page-content']/div/div[1]/div[4]/div[1]/fieldset/label[2]/span"
    language_xpath = "//*[@id='StaticFilters']/div[3]/div[1]/div[1]/div/div/span/span[1]/span/ul/li/input"
    languageValues_xpath = "///*[@id='select2-select-language-results']//li"
    subject_xpath = "//*[@id='StaticFilters']/div[4]/div[4]/div[1]/div/div/span/span[1]/span/ul/li/input"
    treatyInstrument_xpath = "//*[@id='StaticFilters']/div[4]/div[4]/div[2]/div/div/span/span[1]/span/ul/li/input"
    provision_xpath = "//*[@id='StaticFilters']/div[4]/div[4]/div[3]/div/div/span/span[1]/span/ul/li/input"
    searchFT_xpath = "//*[@id='txtFTSSearch']"
    firstLink_xpath = "(//span[@class='document__citation copy-element tooltip-elem']//a)[1]"
    fullCase_xpath = "(//div[@class='document__footer-right']//a)[1]"
    downloadDocument_xpath = "(//p[@class='text--right']//a)[1]"
    researchOption_xpath = "(//label[@class='form__radio']//input)[1]"
    addNotepad_xpath = "//*[@id='btn-popup-add']"
    expandDocumentDetails_xpath = "(//div[@class='dropdown']//button//span)[1]"
    disputeDetailsCopyCitation_xpath = "//div[@class='dispute-details']//div[@class='citationdiv']//p//small//a"


    def __init__(self, driver):
        self.driver = driver

    # clicks on Jurisprudence Navigation menu
    def clickOnFullTextSearchMenu(self):
        self.driver.find_element(By.XPATH, self.fullTextSearch_xpath).click()

        # Clicks on skip Client Listing

    def clickOnClientListing(self):
        self.driver.implicitly_wait(1000)
        self.driver.find_element(By.CSS_SELECTOR, self.clientListing_css_selector).click()
        self.driver.implicitly_wait(1000)

    def getHeading(self):
        fullTextHeading = self.driver.find_element(By.XPATH, self.fulltextHeading_xpath).get_attribute(
            "textContent")
        return fullTextHeading

    def clickOnSearch(self):
        search = self.driver.find_element(By.XPATH, self.searchTextBox_xpath)
        self.driver.execute_script("arguments[0].click();", search)

    def clickOnReset(self):
        reset = self.driver.find_element(By.CSS_SELECTOR, self.resetLink_css_selector)
        self.driver.execute_script("arguments[0].click();", reset)

    def Search(self):
        searchValue = self.driver.find_element(By.XPATH, self.searchTextBox_xpath)
        searchValue.send_keys("Countries")
        # self.driver.execute_script("arguments[0].click();", searchValue)

    def clickOnCopyCitation(self):
        citationlink = self.driver.find_element(By.XPATH, self.copyCitation_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", citationlink)
        self.driver.execute_script("arguments[0].click();", citationlink)

    def clickOnActions(self):
        actions = self.driver.find_element(By.XPATH, self.actions_xpath)
        self.driver.execute_script("arguments[0].click();", actions)

    def clickOnResearchNotepad(self):
        notepad = self.driver.find_element(By.XPATH, self.researchNotepad_xpath)
        self.driver.execute_script("arguments[0].click();", notepad)

    def clickOnResearchTopic(self):
        researchTopic = self.driver.find_element(By.XPATH, self.researchTopicOption_xpath)
        self.driver.execute_script("arguments[0].click();", researchTopic)

    def clickOnResearchAdd(self):
        researchAdd = self.driver.find_element(By.XPATH, self.researchAdd_xpath)
        self.driver.execute_script("arguments[0].click();", researchAdd)

    def clickOnBasicFilters(self):
        filterDispute = self.driver.find_element(By.XPATH, self.editBasicFiltersDispute_xpath)
        self.driver.execute_script("arguments[0].click();", filterDispute)

    def deselectArbitration(self):
        arbitrationCheck = self.driver.find_element(By.XPATH, self.arbitratioCheck_xpath)
        self.driver.execute_script("arguments[0].click();", arbitrationCheck)

    def deselectTreaties(self):
        treatiesCheck = self.driver.find_element(By.XPATH, self.treatiesCheck_xpath)
        self.driver.execute_script("arguments[0].click();", treatiesCheck)

    def submitSearch(self):
        submitSearch = self.driver.find_element(By.XPATH, self.submitSearch_xpath)
        self.driver.execute_script("arguments[0].click();", submitSearch)

    def deselectDispute(self):
        dispute = self.driver.find_element(By.XPATH, self.disputeCheck_xpath)
        self.driver.execute_script("arguments[0].click();", dispute)

    def clickAllWordsOption(self):
        allwords = self.driver.find_element(By.XPATH, self.allWordsOption_xpath)
        self.driver.execute_script("arguments[0].click();", allwords)

    def clickAnyWordsOption(self):
        anywords = self.driver.find_element(By.XPATH, self.anyWordsOption_xpath)
        self.driver.execute_script("arguments[0].click();", anywords)

    def clickOnLanguage(self):
        languageClick = self.driver.find_element(By.XPATH, self.language_xpath)
        languageClick.click()
        languageClick.send_keys("Eng")

    def clickOnRespondentState(self):
        respondent = self.driver.find_element(By.XPATH, self.respondentSateDropdown_xpath)
        self.driver.execute_script("arguments[0].click();", respondent)
        respondent.send_keys("united")

    def clickOnApplicableInstruments(self):
        applicable = self.driver.find_element(By.XPATH, self.applicableInstrumentsDropdown_xpath)
        self.driver.execute_script("arguments[0].click();", applicable)
        applicable.send_keys("agreement")

    def clickOnArbitrationRules(self):
        arbitration = self.driver.find_element(By.XPATH, self.applicableArbitrationRulesDropdown_xpath)
        self.driver.execute_script("arguments[0].click();", arbitration)
        arbitration.send_keys("ICC")

    def clickOnSubject(self):
        subject = self.driver.find_element(By.XPATH, self.subject_xpath)
        self.driver.execute_script("arguments[0].click();", subject)
        subject.send_keys("Clean")

    def clickOnTreatyInstrument(self):
        treatyInstrument = self.driver.find_element(By.XPATH, self.treatyInstrument_xpath)
        self.driver.execute_script("arguments[0].click();", treatyInstrument)
        treatyInstrument.send_keys("United")


    def clickOnProvision(self):
        provision = self.driver.find_element(By.XPATH, self.provision_xpath)
        self.driver.execute_script("arguments[0].click();", provision)
        provision.send_keys("Art")

    def clickOnSearchFT(self):
        fullTextSearch = self.driver.find_element(By.XPATH, self.searchFT_xpath)
        self.driver.execute_script("arguments[0].click();", fullTextSearch)
        fullTextSearch.send_keys("Countries")
        btnSearch = self.driver.find_element(By.XPATH, self. searchTextBox_xpath)
        self.driver.execute_script("arguments[0].click();", btnSearch)

    def clickOnFirstLink(self):
        firstLink = self.driver.find_element(By.XPATH, self.firstLink_xpath)
        self.driver.execute_script("arguments[0].click();", firstLink)

    def clickOnFullCaseAnalysis(self):
        fullCaseAnalysis = self.driver.find_element(By.XPATH, self.fullCase_xpath)
        self.driver.execute_script("arguments[0].click();", fullCaseAnalysis)

    def clickOnDownloadDocument(self):
        downloadDoc = self.driver.find_element(By.XPATH, self.downloadDocument_xpath)
        self.driver.execute_script("arguments[0].click();", downloadDoc)

    def clickOnResearch(self):
        researchNotepad = self.driver.find_element(By.XPATH, self.researchNotepad_xpath)
        self.driver.execute_script("arguments[0].click();", researchNotepad)

    def selectResearchOption(self):
        researchOption = self.driver.find_element(By.XPATH, self.researchOption_xpath)
        self.driver.execute_script("arguments[0].click();", researchOption)

    def clickOnAddNotepad(self):
        addNote = self.driver.find_element(By.XPATH, self.addNotepad_xpath)
        self.driver.execute_script("arguments[0].click();", addNote)

    def clickOnExpandDocumentDetails(self):
        expandDocument = self.driver.find_element(By.XPATH, self.expandDocumentDetails_xpath)
        self.driver.execute_script("arguments[0].click();", expandDocument)

    def clickOnDisputeDetailsCopyCitaion(self):
        copyCitation = self.driver.find_element(By.XPATH, self.disputeDetailsCopyCitation_xpath)
        self.driver.execute_script("arguments[0].click();", copyCitation)




