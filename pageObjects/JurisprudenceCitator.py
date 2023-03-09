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
    addToDocumentComparison_xpath = "(//p[@class='text--right']//button)[1]"
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
    cardexpanded_xpath = "(//div[@class='card-list']//div//div//a)[1]"
    seeAllRef_xpath = "(//div[@class='tabs__content-container']//div//div//ul//li[2]//a)[1]"
    fullCaseAnalysis_xpath = "(//div[@class='document__footer-right']//a)[1]"
    documentComparisonFirstOption_xpath = "//div[@class='card card--compact']//ul//li[1]"
    documentComparison_xpath = "//div[@class='card card--details']//div[@class='tabs']//div//div//p//a[2]"
    documentComparisonOption_xpath = "//*[@id='popup-add-to-dc']/div[1]/div[2]/ul/li[1]/label/span"
    documentComparisonAdd_xpath = "//*[@id='btn-comparison-add']"
    documentCompareCancel_xpath = "//*[@id='btn-comparison-Cancel']"
    seeAllGroups_xpath = "//*[@id='popup-add-to-dc']/div[1]/div[1]/div[2]/a"
    researchNotepad_xpath = "//button[@title='Add to Notepad']"
    researchOption_xpath = "(//label[@class='form__radio']//input)[1]"
    addNotepad_xpath = "//*[@id='btn-popup-add']"
    addToNotepad_xpath = "//*[@id='frm-download-treatiesrules-view']/p/button[2]"
    seeAllTopics_xpath = "//*[@id='popup-add-to-rn']/div[1]/div[1]/div[2]/a"
    closeResearchNotepad_xpath = "//*[@id='popup-add-to-rn']/div[1]/p[1]/a"
    createResearchTopic_xpath = "//*[@id='popup-add-to-rn']/div[1]/div[2]/div/p/a"
    enterTopic_xpath = "//*[@id='topic-name']"
    saveTopic_xpath = "//*[@id='btn-create-new-research-topic']"
    #copyCitation_xpath = "//*[@id='treaties-rules']/div[1]/div[2]/p/small/a/span"
    copyCitationlink_xpath = "//div[@class='citationdiv']//p//a"
    downloadDocumentLink_xpath = "//*[@id='frm-download-document-view']/p/a"
    viewPDF_xpath = "//div[@class='grid__col grid__col--md-4']//a"
    subjectNavigatorMenu_xpath = "(//nav[@class='document__nav primarylang']//ul//li//a[1]//img)[1]"
    subjectNavigatorExpandLink_xpath = "//div[@class='dropdown default-sidebar']//button"
    publicationCitatorMenu_xpath = "//nav[@class='document__nav primarylang']//ul//li[4]//a//img"
    publicationCitatorExpandLink_xpath = "//div[@class='dropdown default-sidebar']//button"
    articleCitatorMenu_xpath = "//*[@id='document-view']/nav/ul/li[2]/a"
    articleCitatorLink_xpath = "//div[@class='dropdown default-sidebar']//button"
    termsAndPhrasesMenu_xpath = "//nav[@class='document__nav primarylang']//ul//li[5]//a//img"
    termsAndPhrasesExpandLink_xpath = "//div[@class='dropdown default-sidebar']//button"
    keywordSearch_xpath = "//nav[@class='document__nav primarylang']//ul//li[6]//a"
    keywordSearchEntry_xpath = "//*[@id='txtkeyword']"
    searchButton_xpath = "//*[@id='btnKeywordSearch']"
    goToFullTextSearch_xpath = "//*[@id='GotoFulltextSearch']"

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

    def clickOnExpandInnerCard(self):
        cardExpand = self.driver.find_element(By.XPATH, self.cardexpanded_xpath)
        self.driver.execute_script("arguments[0].click();", cardExpand)

    def clickOnSeeAllRef(self):
        seeAll = self.driver.find_element(By.XPATH, self.seeAllRef_xpath)
        self.driver.execute_script("arguments[0].click();", seeAll)

    def clickOnFullCaseAnalysis(self):
        fullCase = self.driver.find_element(By.XPATH, self.fullCaseAnalysis_xpath)
        self.driver.execute_script("arguments[0].click();", fullCase)

    def addToDocumentComparison(self):
        documentComparison = self.driver.find_element(By.XPATH, self.addToDocumentComparison_xpath)
        self.driver.execute_script("arguments[0].click();", documentComparison)

    def selectDocumentCmparisonOption(self):
        options = self.driver.find_element(By.XPATH, self.documentComparisonFirstOption_xpath)
        self.driver.execute_script("arguments[0].click();", options)

    def clickOnAddDocumentCompare(self):
        addCompare = self.driver.find_element(By.XPATH, self.documentComparisonAdd_xpath)
        self.driver.execute_script("arguments[0].click();", addCompare)

    def selectDocumentComparisonOption(self):
        selectOptionComparison = self.driver.find_element(By.XPATH, self.documentComparisonOption_xpath)
        self.driver.execute_script("arguments[0].click();", selectOptionComparison)

    def clickOnCancelCompare(self):
        cancelCompare = self.driver.find_element(By.XPATH, self.documentCompareCancel_xpath)
        self.driver.execute_script("arguments[0].click();", cancelCompare)

    def clickOnSeeAllGroups(self):
        seeAll = self.driver.find_element(By.XPATH, self.seeAllGroups_xpath)
        self.driver.execute_script("arguments[0].click();", seeAll)

    def clickOnResearch(self):
        researchNotepad = self.driver.find_element(By.XPATH, self.researchNotepad_xpath)
        self.driver.execute_script("arguments[0].click();", researchNotepad)

    def selectResearchOption(self):
        researchOption = self.driver.find_element(By.XPATH, self.researchOption_xpath)
        self.driver.execute_script("arguments[0].click();", researchOption)

    def clickOnAddNotepad(self):
        addNote = self.driver.find_element(By.XPATH, self.addNotepad_xpath)
        self.driver.execute_script("arguments[0].click();", addNote)

    def clickOnSeeAllTopics(self):
        seeAllTopics = self.driver.find_element(By.XPATH, self.seeAllTopics_xpath)
        self.driver.execute_script("arguments[0].click();", seeAllTopics)

    def clickOnCloseResearchNotepad(self):
        closeResearch = self.driver.find_element(By.XPATH, self.closeResearchNotepad_xpath)
        self.driver.execute_script("arguments[0].click();", closeResearch)

    def clickOnCreateResearchTopic(self):
        createTopic = self.driver.find_element(By.XPATH, self.createResearchTopic_xpath)
        self.driver.execute_script("arguments[0].click();", createTopic)

    def sendTopic(self):
        topic = self.driver.find_element(By.XPATH, self.enterTopic_xpath)
        topic1 = topic.send_keys("TopicTest")
        return topic1

    def clickOnSave(self):
        saveTopic = self.driver.find_element(By.XPATH, self.saveTopic_xpath)
        self.driver.execute_script("arguments[0].click();", saveTopic)

    def clickOnCopyCitationLink(self):
        copyCitationLink = self.driver.find_element(By.XPATH, self.copyCitationlink_xpath)
        self.driver.execute_script("arguments[0].click();", copyCitationLink)

    def clickOnDownloadDocumentLink(self):
        downloadDoc = self.driver.find_element(By.XPATH, self.downloadDocumentLink_xpath)
        self.driver.execute_script("arguments[0].click();", downloadDoc)

    def clickOnViewPDF(self):
        viewpdf = self.driver.find_element(By.XPATH, self.viewPDF_xpath)
        self.driver.execute_script("arguments[0].click();", viewpdf)

    def clickOnSubjectNavigatorMenu(self):
        subjectNavigator = self.driver.find_element(By.XPATH, self.subjectNavigatorMenu_xpath)
        self.driver.execute_script("arguments[0].click();", subjectNavigator)

    def clickOnSubjectNavigatorLink(self):
        subjectNavigatorLink = self.driver.find_element(By.XPATH, self.subjectNavigatorExpandLink_xpath)
        self.driver.execute_script("arguments[0].click();", subjectNavigatorLink)

    def clickOnPublicationCitatorMenu(self):
        publicationCitator = self.driver.find_element(By.XPATH, self.publicationCitatorMenu_xpath)
        self.driver.execute_script("arguments[0].click();", publicationCitator)

    def clickOnPublicationLink(self):
        publicationLink = self.driver.find_element(By.XPATH, self.publicationCitatorExpandLink_xpath)
        self.driver.execute_script("arguments[0].click();", publicationLink)

    def clickOnArticleCitatorMenu(self):
        articleCitator = self.driver.find_element(By.XPATH, self.articleCitatorMenu_xpath)
        self.driver.execute_script("arguments[0].click();", articleCitator)

    def clickOnArticleCitatorLink(self):
        articleCitatorlink = self.driver.find_element(By.XPATH, self.articleCitatorLink_xpath)
        self.driver.execute_script("arguments[0].click();", articleCitatorlink)

    def clickOnTermsAndPhrasesLink(self):
        termsAndPhrasesLink = self.driver.find_element(By.XPATH, self.termsAndPhrasesExpandLink_xpath)
        self.driver.execute_script("arguments[0].click();", termsAndPhrasesLink)

    def clickOnTermsAndPhrasesMenu(self):
        termsAndPhrases = self.driver.find_element(By.XPATH, self.termsAndPhrasesMenu_xpath)
        self.driver.execute_script("arguments[0].click();", termsAndPhrases)

    def clickOnKeywordSearch(self):
        keywordSearch = self.driver.find_element(By.XPATH, self.keywordSearch_xpath)
        self.driver.execute_script("arguments[0].click();", keywordSearch)

    def clickOnKeywordSearchEntry(self):
        keywordSearchEntry = self.driver.find_element(By.XPATH, self.keywordSearchEntry_xpath)
        keyword = keywordSearchEntry.send_keys("Alexandra")
        return keyword

    def clickOnSearchButton(self):
        buttonSearch = self.driver.find_element(By.XPATH, self.searchButton_xpath)
        self.driver.execute_script("arguments[0].click();", buttonSearch)

    def clickOnGoToFullTextSearch(self):
        fulltextSearch = self.driver.find_element(By.XPATH, self.goToFullTextSearch_xpath)
        self.driver.execute_script("arguments[0].click();", fulltextSearch)






