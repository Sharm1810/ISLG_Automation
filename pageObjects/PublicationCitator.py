import time

import self
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from utilities.customLogger import LogGen

logger = LogGen.loggen()


class PublicationCitator:
    publicationCitator_xpath = "//*[@id='Rslink']/li[4]/a"
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
    seeAllLink_xpath = "(//ul[@class='list--bordered list--bordered-no-padding']//li[2]//a)[1]"
    fullCaseAnalysis_xpath = "(//div[@class='document__footer-right']//a)[1]"
    addToDocumentComparison_xpath = "(//p[@class='text--right']//button)[1]"
    documentComparisonOption_xpath = "//*[@id='popup-add-to-dc']/div[1]/div[2]/ul/li[1]/label/span"
    documentComparisonAdd_xpath = "//*[@id='btn-comparison-add']"
    documentCompareCancel_xpath = "//*[@id='btn-comparison-Cancel']"
    seeAllGroups_xpath = "//*[@id='popup-add-to-dc']/div[1]/div[1]/div[2]/a"
    researchNotepad_xpath = "//button[@title='Add to Notepad']"
    researchOption_xpath = "(//label[@class='form__radio']//input)[1]"
    addNotepad_xpath = "//*[@id='btn-popup-add']"
    closeResearchNotepad_xpath = "//*[@id='popup-add-to-rn']/div[1]/p[1]/a"
    seeAllTopics_xpath = "//*[@id='popup-add-to-rn']/div[1]/div[1]/div[2]/a"
    createResearchTopic_xpath = "//*[@id='popup-add-to-rn']/div[1]/div[2]/div/p/a"
    enterTopic_xpath = "//*[@id='topic-name']"
    saveTopic_xpath = "//*[@id='btn-create-new-research-topic']"
    copyCitationlink_xpath = "//div[@class='citationdiv']//p//a"
    downloadDocumentLink_xpath = "//*[@id='frm-download-document-view']/p/a"
    viewPDF_xpath = "//div[@class='grid__col grid__col--md-4']//a"
    subjectNavigatorMenu_xpath = "(//nav[@class='document__nav primarylang']//ul//li//a[1]//img)[1]"
    subjectNavigatorExpandLink_xpath = "//div[@class='dropdown default-sidebar']//button"
    jurisprudenceCitatorMenu_xpath = "//nav[@class='document__nav primarylang']//li[3]//a//img"
    jurisprudenceCitatorExpandLink_xpath = "//div[@class='dropdown default-sidebar']//button"
    articleCitatorMenu_xpath = "//*[@id='document-view']/nav/ul/li[2]/a"
    articleCitatorLink_xpath = "//div[@class='dropdown default-sidebar']//button"
    termsAndPhrasesMenu_xpath = "//nav[@class='document__nav primarylang']//ul//li[5]//a//img"
    termsAndPhrasesExpandLink_xpath = "//div[@class='dropdown default-sidebar']//button"
    keywordSearch_xpath = "//nav[@class='document__nav primarylang']//ul//li[6]//a"
    keywordSearchEntry_xpath = "//*[@id='txtkeyword']"
    searchButton_xpath = "//*[@id='btnKeywordSearch']"
    goToFullTextSearch_xpath = "//*[@id='GotoFulltextSearch']"
    booksFirstLink_xpath = "(//div[@class='item-list compact__container']//div[2]//div//a)[1]"
    booksAction_xpath = "//div[@class='dropdown card__actions']//button"
    booksAddToNotepad_xpath = "//div[@class='card__actions dropdown']//div//p//a[1]"
    booksResearchOption_xpath = "(//div[@class='topics-details']//div//ul//li//label//input)[1]"
    booksResearchAdd_xpath = "//p[@class='text--right']//button[2]"
    booksResearchEntirePublication_xpath = "//div[@class='specific-reference-bookmark']//div//ul//li//label//input"
    entirePublicationAdd_xpath = "//p[@class='text--right']//button[3]"



    def __init__(self, driver):
        self.driver = driver

    # clicks on Publication Citator Navigation menu
    def clickOnPublicationCitator(self):
        publicationCitatormenu = self.driver.find_element(By.XPATH, self.publicationCitator_xpath)
        self.driver.execute_script("arguments[0].click();", publicationCitatormenu)



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

    def clickOnSeeAll(self):
        seeAllLink = self.driver.find_element(By.XPATH, self.seeAllLink_xpath)
        self.driver.execute_script("arguments[0].click();", seeAllLink)

    def clickOnFullCaseAnalysis(self):
        fullCaseAnalysis = self.driver.find_element(By.XPATH, self.fullCaseAnalysis_xpath)
        self.driver.execute_script("arguments[0].click();", fullCaseAnalysis)

    def addToDocumentComparison(self):
        documentComparison = self.driver.find_element(By.XPATH, self.addToDocumentComparison_xpath)
        self.driver.execute_script("arguments[0].click();", documentComparison)

    def selectDocumentComparisonOption(self):
        selectOptionComparison = self.driver.find_element(By.XPATH, self.documentComparisonOption_xpath)
        self.driver.execute_script("arguments[0].click();", selectOptionComparison)


    def clickOnAddDocumentCompare(self):
        addCompare = self.driver.find_element(By.XPATH, self.documentComparisonAdd_xpath)
        self.driver.execute_script("arguments[0].click();", addCompare)

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

    def clickOnCloseResearchNotepad(self):
        closeResearch = self.driver.find_element(By.XPATH, self.closeResearchNotepad_xpath)
        self.driver.execute_script("arguments[0].click();", closeResearch)


    def clickOnSeeAllTopics(self):
        seeAllTopics = self.driver.find_element(By.XPATH, self.seeAllTopics_xpath)
        self.driver.execute_script("arguments[0].click();", seeAllTopics)

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

    def clickOnJurisprudenceNavigatorMenu(self):
        jurisprudenceCitator = self.driver.find_element(By.XPATH, self.jurisprudenceCitatorMenu_xpath)
        self.driver.execute_script("arguments[0].click();", jurisprudenceCitator)

    def clickOnJurisprudenceLink(self):
        jurisprudenceLink = self.driver.find_element(By.XPATH, self.jurisprudenceCitatorExpandLink_xpath)
        self.driver.execute_script("arguments[0].click();", jurisprudenceLink)

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
        keyword = keywordSearchEntry.send_keys("case")
        return keyword

    def clickOnSearchButton(self):
        buttonSearch = self.driver.find_element(By.XPATH, self.searchButton_xpath)
        self.driver.execute_script("arguments[0].click();", buttonSearch)

    def clickOnGoToFullTextSearch(self):
        fulltextSearch = self.driver.find_element(By.XPATH, self.goToFullTextSearch_xpath)
        self.driver.execute_script("arguments[0].click();", fulltextSearch)

    def clickOnBooksSubMenu(self):
        booksMenu = self.driver.find_element(By.XPATH, self.booksSubMenu_xpath)
        self.driver.execute_script("arguments[0].click();", booksMenu)

    def clickOnBooksFirstLink(self):
        firstLink = self.driver.find_element(By.XPATH, self.booksFirstLink_xpath)
        self.driver.execute_script("arguments[0].click();", firstLink)

    def clickOnBooksActions(self):
        actionsBooks = self.driver.find_element(By.XPATH, self.booksAction_xpath)
        self.driver.execute_script("arguments[0].click();", actionsBooks)

    def clickOnBooksAddToNotepad(self):
        booksAddToNotepad = self.driver.find_element(By.XPATH, self.booksAddToNotepad_xpath)
        self.driver.execute_script("arguments[0].click();", booksAddToNotepad)

    def selectBooksResearchOption(self):
        booksResearchOption = self.driver.find_element(By.XPATH, self.booksResearchOption_xpath)
        self.driver.execute_script("arguments[0].click();", booksResearchOption)

    def clickOnBooksResearchAdd(self):
        booksResearchAdd = self.driver.find_element(By.XPATH, self.booksResearchAdd_xpath)
        self.driver.execute_script("arguments[0].click();", booksResearchAdd)

    def selectBooksEntirePublictaion(self):
        entirePub = self.driver.find_element(By.XPATH, self.booksResearchEntirePublication_xpath)
        self.driver.execute_script("arguments[0].click();", entirePub)

    def clickOnAddEntirePublication(self):
        booksAddPublication = self.driver.find_element(By.XPATH, self.entirePublicationAdd_xpath)
        self.driver.execute_script("arguments[0].click();", booksAddPublication)
















