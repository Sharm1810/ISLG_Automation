import time

import self
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from utilities.customLogger import LogGen

logger = LogGen.loggen()


class ArticleCitator():
    articleCitatormenu_cssselector = "#Rslink > li:nth-child(2) > a"
    clientListing_cssseelector = "#dvClientListing > div > button"
    firstBranchExpand_cssselector = "#page-content > div > div:nth-child(9) > div > div:nth-child(1) > div > div.card__header > a.cursor--pointer.card__title.dropdown__toggle.acTitleClick"
    elementActions_xpath = "//div[@class='tabs']//div//div//button[normalize-space()='Actions']"
    elementResearchNotepad_xpath = "//div[@role='tablist']//a[@title='Add to Research Notepad'][normalize-space("")='Research Notepad']"
    researchTopicOption_xpath = "(//div[@class='card card--compact']//ul//li)[1]//span"
    researchAddbutton_xpath = "//*[@id='btn-popup-add-next']"
    doucmentComparison_xpath = "//div[@role='tablist']//a[@title='Add to Document Comparison'][normalize-space()='Document Comparison']"
    addDocumentoption_xpath = "//div[@class='card card--compact entire-articlecitator']//ul//li//label//span"
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
    researchNotepadSecond_xpath = "//div[@class='card card--compact entire-articlecitator']//ul//li//label//span"
    downloadDocument_xpath = "//*[@id='frm-download-treatiesrules-view']/p/a/span"
    addToDocumentComparison_xpath = "//button[@title='Add to Document Comparison']"
    #addToDocumentComparison_xpath = "//form[@id='frm-download-document-view']//p//a"
    addToNotepad_xpath = "//*[@id='frm-download-treatiesrules-view']/p/button[2]"
    copyCitation_xpath = "//*[@id='treaties-rules']/div[1]/div[2]/p/small/a/span"
    viewOriginalPDF_xpath = "//*[@id='treaties-rules']/div[1]/div[5]/div[2]/a/span[2]/span"
    firstLink_xpath = "(//div[@class='ACCardData']//div//div//a)[1]"
    provisionRuleSeeAll_xpath = "(//div[@class='tabs__content-container']//div//div//ul//li[1]//a)[1]"
    fullCaseAnalysis_xpath = "//div[@class='document__footer-right']//a"
    documentView1_xpath = "//*[@id='document-view']/div[1]/p/i[1]"
    documentComparisonFirstOption_xpath = "//div[@class='card card--compact']//ul//li[1]"
    documentCompareAdd_xpath = "//button[@id='btn-comparison-add']"
    documentCompareCancel_xpath = "//*[@id='btn-comparison-Cancel']"
    seeAllGroups_xpath = "//*[@id='popup-add-to-dc']/div[1]/div[1]/div[2]/a"
    researchNotepad_xpath = "//button[@title='Add to Notepad']"
    researchOption_xpath = "(//label[@class='form__radio']//input)[1]"
    addNotepad_xpath = "//*[@id='btn-popup-add']"
    seeAllTopics_xpath ="//*[@id='popup-add-to-rn']/div[1]/div[1]/div[2]/a"
    researchNotepadHeading_xpath ="//*[@id='ResearchTopicMaster']/div[1]/div/div[1]"
    closeResearchNotepad_xpath = "//*[@id='popup-add-to-rn']/div[1]/p[1]/a"
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
    publicationCitatorMenu_xpath = "//nav[@class='document__nav primarylang']//ul//li[4]//a//img"
    publicationCitatorExpandLink_xpath = "//div[@class='dropdown default-sidebar']//button"
    termsAndPhrasesMenu_xpath = "//nav[@class='document__nav primarylang']//ul//li[5]//a//img"
    termsAndPhrasesExpandLink_xpath = "//div[@class='dropdown default-sidebar']//button"
    keywordSearch_xpath = "//nav[@class='document__nav primarylang']//ul//li[6]//a"
    keywordSearchEntry_xpath = "//*[@id='txtkeyword']"
    searchButton_xpath = "//*[@id='btnKeywordSearch']"
    goToFullTextSearch_xpath = "//*[@id='GotoFulltextSearch']"


    def __init__(self, driver):
        self.driver = driver

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
        elementResearchTopic = self.driver.find_element(By.XPATH, self.researchTopicOption_xpath)
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

    def clickOnSeeAll(self):
        seeAllLink = self.driver.find_element(By.XPATH, self.provisionRuleSeeAll_xpath)
        self.driver.execute_script("arguments[0].click();", seeAllLink)

    def clickOnFullCase(self):
        fullcase = self.driver.find_element(By.XPATH, self.fullCaseAnalysis_xpath)
        self.driver.execute_script("arguments[0].click();", fullcase)

    def getDocumentView(self):
        documentView = self.driver.find_element(By.XPATH, self.documentView1_xpath)
        #self.logger.info(documentView.text)
        print(documentView.text)

    def addToDocumentComparison(self):
        documentComparison = self.driver.find_element(By.XPATH, self.addToDocumentComparison_xpath)
        self.driver.execute_script("arguments[0].click();", documentComparison)

    def selectDocumentCmparisonOption(self):
        options = self.driver.find_element(By.XPATH, self.documentComparisonFirstOption_xpath)
        self.driver.execute_script("arguments[0].click();", options)

    def clickOnAddDocumentCompare(self):
        addCompare = self.driver.find_element(By.XPATH, self.documentComparisonAdd_xpath)
        self.driver.execute_script("arguments[0].click();", addCompare)

    def clickOnCancelCompare(self):
        cancelCompare = self.driver.find_element(By.XPATH, self.documentCompareCancel_xpath)
        self.driver.execute_script("arguments[0].click();",cancelCompare)

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

    def clickOnJurisprudenceNavigatorMenu(self):
        jurisprudenceCitator = self.driver.find_element(By.XPATH, self.jurisprudenceCitatorMenu_xpath)
        self.driver.execute_script("arguments[0].click();", jurisprudenceCitator)

    def clickOnJurisprudenceLink(self):
        jurisprudenceLink = self.driver.find_element(By.XPATH, self.jurisprudenceCitatorExpandLink_xpath)
        self.driver.execute_script("arguments[0].click();", jurisprudenceLink)

    def clickOnPublicationCitatorMenu(self):
        publicationCitator = self.driver.find_element(By.XPATH, self.publicationCitatorMenu_xpath)
        self.driver.execute_script("arguments[0].click();", publicationCitator)

    def clickOnPublicationLink(self):
        publicationLink = self.driver.find_element(By.XPATH, self.publicationCitatorExpandLink_xpath)
        self.driver.execute_script("arguments[0].click();", publicationLink)

    def clickOnTermsAndPhrasesMenu(self):
        termsAndPhrases = self.driver.find_element(By.XPATH, self.termsAndPhrasesMenu_xpath)
        self.driver.execute_script("arguments[0].click();", termsAndPhrases)

    def clickOnTermsAndPhrasesLink(self):
        termsAndPhrasesLink = self.driver.find_element(By.XPATH, self.termsAndPhrasesExpandLink_xpath)
        self.driver.execute_script("arguments[0].click();", termsAndPhrasesLink)

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



















