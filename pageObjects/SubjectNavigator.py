import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class SubjectNavigator:
    subjectNavigatormenu_cssselector = "#Rslink > li:nth-child(1) > a"
    clientListing_cssseelector = "#dvClientListing > div > button"
    subjectNavigatorHeading_xpath = "//*[@id='page-content']/div/div[3]/div/div[1]/h1"
    subjectTextsearch_textbox_cssselector = "#txtSubjectNavigatorSearch"
    textFind_button_id = "//*[@id='btn-search-subject-citator']"
    resetLink_xpath = "//*[@id='dvSubjectNavigatorSearchBranch']/a"
    branchNameA_link = "A"
    viewContextlink_xpath = "//*[@id='item-list-item-1']/div/div[1]/div[1]/a[2]"
    actionsButton_xpath = "//*[@id='item-list-item-11241-card-11241-actions-control']"
    researchNotepadlink_xpath = "//*[@id='item-list-item-11241-card-11241-actions']/p/a[1]"
    fulltextSearchlink_xpath = "//*[@id='item-list-item-11241-card-11241-actions']/p/a[2]"
    card_button_xpath = "//*[@id='btnCard']"
    compact_button_xpath = "//*[@id='btnCompact']/i"
    branchA_xpath = "//a[contains(@title='A')]"
    branchB_link = "B"
    branchC_xpath = "C"
    branchD_xpath = "D"
    branchE_xpath = "E"
    branchF_xpath = "F"
    branchG_xpath = "G"
    branchH_xpath = "H"
    branchI_xpath = "I"
    branchJ_xpath = "J"
    branchK_xpath = "K"
    branchL_xpath = "L"
    branchM_xpath = "M"
    branchN_xpath = "N"
    branchO_xpath = "O"
    branchP_xpath = "P"
    branchQ_xpath = "Q"
    branchR_xpath = "R"
    branchS_xpath = "S"
    branchT_xpath = "T"
    branchU_xpath = "U"
    branchV_xpath = "V"
    branchW_xpath = "W"
    branchX_xpath = "X"
    branchY_xpath = "Y"
    branchZ_xpath = "Z"
    fulltextsearch_xpath = "//*[@id='item-list-item-11241-card-11241-actions']/p/a[2]"
    expandSearch_xpath = "//*[@id='btnfilter-dropdown-control']"
    searchStemmingChecked_xpath = "//*[@id='filter-dropdown']/fieldset[2]/label[1]/span/span/i"
    searchFuzzyTypoChecked_xpath = "//*[@id='chkSnFuzzyTypo']"
    actionsclick_xpath = "(//div[@class='card__actions dropdown']//a)[1]"
    researchNotepadActions_xpath = "(//div[@class='card__actions dropdown']//div//p//a)[1]"
    mainBranchFirstLink_xpath = "(//div[@class='card card--basic  dropdown']//div//a)[1]//span"
    crossRef_xpath = "(//div[@class='dropdown item-list__item']//div//div[2]//div)[1]//span[1]"
    innerCardHeader_xpath = "(//div[@class='card-list'][2]//div//div)[1]"
    firstLink_xpath = "(//div[@class='card-list']//div//div[2]//div[2]//div//a)[1]"
    fullCaseAnalysis_xpath = "(//div[@class='document__footer-right']//a)[1]"
    subjectNavigatorMenu_xpath = "(//nav[@class='document__nav primarylang']//ul//li//a[1]//img)[1]"
    subjectNavigatorExpandLink_xpath = "//div[@class='dropdown default-sidebar']//button"
    viewSubjectNavigator_xpath = "(//div[@class='dropdown default-sidebar']//div//div//p[2]//small//a)[1]"
    copyCitation_xpath = "//div[@class='document-details-view']//div//p//small//a"
    viewPDF_xpath = "//div[@class='grid__col grid__col--md-4']//a"
    downloadDocument_xpath = "(//p[@class='text--right']//a)[1]"
    documentComparison_xpath = "(//p[@class='text--right']//button)[1]"
    addToDocumentComparison_xpath = "(//p[@class='text--right']//button)[1]"
    documentComparisonOption_xpath = "//*[@id='popup-add-to-dc']/div[1]/div[2]/ul/li[1]/label/span"
    documentComparisonAdd_xpath = "//*[@id='btn-comparison-add']"
    documentCompareCancel_xpath = "//*[@id='btn-comparison-Cancel']"
    researchNotepad_xpath = "//button[@title='Add to Notepad']"
    researchOption_xpath = "(//label[@class='form__radio']//input)[1]"
    addNotepad_xpath = "//*[@id='btn-popup-add']"
    actions_xpath = "(//div[@class='card__actions dropdown']//button)[1]"
    researchNotepadDropdown_xpath = "(//div[@class='card__actions dropdown']//p//a)[1]"
    researchOptionFirst_xpath = "(//div[@class='card card--compact']//ul//li)[1]"
    bookmarkError_xpath = "//div[@class='topics-details bookmark-error']//span"
    copyLocationDropdown_xpath = "(//div[@class='card__actions dropdown']//p//a)[3]"
    researchNotepadCancel_xpath = "(//p[@class='text--right']//a)[1]"
    copyLocationToastMessage_xpath = "//div[@data-notify= 'container']//span[3]"

    def __init__(self, driver):
        self.driver = driver

    def clickOnSubjectNavigatormenu(self):
        self.driver.find_element_by_css_selector(self.subjectNavigatormenu_cssselector).click()

    def clickOnClientListing(self):
        self.driver.implicitly_wait(1000)
        self.driver.find_element_by_css_selector("#dvClientListing > div > button").click()
        self.driver.implicitly_wait(1000)

    def getHeading(self):
        subjectHeading = self.driver.find_element_by_xpath(self.subjectNavigatorHeading_xpath).text

    def resetLink(self):
        self.driver.find_element_by_xpath(self.resetLink_xpath).click()

    def findText(self):
        self.driver.find_element_by_xpath(self.textFind_button_id).click()

    def textInput(self, searchtext):
        self.driver.find_element_by_id("txtSubjectNavigatorSearch").click()
        text = self.driver.find_element_by_css_selector("#txtSubjectNavigatorSearch")
        # entering Abuse of Right as search value
        text.send_keys("Abuse of Right")

    def expandBranch(self):
        self.driver.find_element_by_link_text(self.branchNameA_link).click()

    def clickOnViewContext(self):
        self.driver.find_element_by_link_text(self.viewContextlink_xpath).click()

    def clickOnActions(self):
        self.driver.find_element_by_link_text(self.actionsButton_xpath).click()

    def clickOnResearchNotepad(self):
        self.driver.find_element_by_link_text(self.researchNotepadlink_xpath).click()

    def clickOnFulltextsearch(self):
        self.driver.find_element_by_link_text(self.fulltextSearchlink_xpath).click()

    def clickOnCard(self):
        self.driver.find_element_by_link_text(self.card_button_xpath).click()

    def clickOnCompactView(self):
        self.driver.find_element_by_link_text(self.compact_button_xpath).click()

    def clickOnBranchA(self):
        a = self.driver.find_element_by_xpath("//span[(text()= 'A')]")
        self.driver.execute_script("arguments[0].click();", a)

    def collapseBranchA(self):
        collapseA = self.driver.find_element_by_xpath("//span[(text()= 'A')]")
        self.driver.execute_script("arguments[0].click();", collapseA)

    def clickOnBranchB(self):
        b = self.driver.find_element_by_xpath("//span[(text()= 'B')]")
        self.driver.execute_script("arguments[0].click();", b)

    def collapseBranchB(self):
        collapseB = self.driver.find_element_by_xpath("//span[(text()= 'B')]")
        self.driver.execute_script("arguments[0].click();", collapseB)

    def clickOnBranchC(self):
        c = self.driver.find_element_by_xpath("//span[text()='C']")
        self.driver.execute_script("arguments[0].click();", c)

    def collapseBranchC(self):
        collapseC = self.driver.find_element_by_xpath("//span[text()='C']")
        self.driver.execute_script("arguments[0].click();", collapseC)

    def clickOnBranchD(self):
        d = self.driver.find_element_by_xpath("//span[text()='D']")
        self.driver.execute_script("arguments[0].click();", d)

    def collapseBranchD(self):
        collapseD = self.driver.find_element_by_xpath("//span[text()='D']")
        self.driver.execute_script("arguments[0].click();", collapseD)

    def clickOnBranchE(self):
        e = self.driver.find_element_by_xpath("//span[text()='E']")
        self.driver.execute_script("arguments[0].click();", e)

    def collapseBranchE(self):
        collapseE = self.driver.find_element_by_xpath("//span[text()='E']")
        self.driver.execute_script("arguments[0].click();", collapseE)

    def clickOnBranchF(self):
        f = self.driver.find_element_by_xpath("//span[text()='F']")
        self.driver.execute_script("arguments[0].click();", f)

    def collapseBranchF(self):
        collapseF = self.driver.find_element_by_xpath("//span[text()='F']")
        self.driver.execute_script("arguments[0].click();", collapseF)

    def clickOnBranchG(self):
        g = self.driver.find_element_by_xpath("//span[text()='G']")
        self.driver.execute_script("arguments[0].click();", g)

    def collapseBranchG(self):
        collapseG = self.driver.find_element_by_xpath("//span[text()='G']")
        self.driver.execute_script("arguments[0].click();", collapseG)

    def clickOnBranchH(self):
        h = self.driver.find_element_by_xpath("//span[text()='H']")
        self.driver.execute_script("arguments[0].click();", h)

    def collapseBranchH(self):
        collapseH = self.driver.find_element_by_xpath("//span[text()='H']")
        self.driver.execute_script("arguments[0].click();", collapseH)

    def clickOnBranchI(self):
        i = self.driver.find_element_by_xpath("//span[text()='I']")
        self.driver.execute_script("arguments[0].click();", i)

    def collapseBranchI(self):
        collapseI = self.driver.find_element_by_xpath("//span[text()='I']")
        self.driver.execute_script("arguments[0].click();", collapseI)

    def clickOnBranchJ(self):
        j = self.driver.find_element_by_xpath("//span[text()='J']")
        self.driver.execute_script("arguments[0].click();", j)

    def collapseBranchJ(self):
        collapseJ = self.driver.find_element_by_xpath("//span[text()='J']")
        self.driver.execute_script("arguments[0].click();", collapseJ)

    def clickOnBranchK(self):
        k = self.driver.find_element_by_xpath("//span[text()='K']")
        self.driver.execute_script("arguments[0].click();", k)

    def collapseBranchK(self):
        collapseK = self.driver.find_element_by_xpath("//span[text()='K']")
        self.driver.execute_script("arguments[0].click();", collapseK)

    def clickOnBranchL(self):
        l = self.driver.find_element_by_xpath("//span[text()='L']")
        self.driver.execute_script("arguments[0].click();", l)

    def collapseBranchL(self):
        collapseL = self.driver.find_element_by_xpath("//span[text()='L']")
        self.driver.execute_script("arguments[0].click();", collapseL)

    def clickOnBranchM(self):
        m = self.driver.find_element_by_xpath("//span[text()='M']")
        self.driver.execute_script("arguments[0].click();", m)

    def collapseBranchM(self):
        collapseM = self.driver.find_element_by_xpath("//span[text()='M']")
        self.driver.execute_script("arguments[0].click();", collapseM)

    def clickOnBranchN(self):
        n = self.driver.find_element_by_xpath("//span[text()='M']")
        self.driver.execute_script("arguments[0].click();", n)

    def collapseBranchN(self):
        collapseN = self.driver.find_element_by_xpath("//span[text()='N']")
        self.driver.execute_script("arguments[0].click();", collapseN)

    def clickOnBranchO(self):
        o = self.driver.find_element_by_xpath("//span[text()='O']")
        self.driver.execute_script("arguments[0].click();", o)

    def collapseBranchO(self):
        collapseO = self.driver.find_element_by_xpath("//span[text()='O']")
        self.driver.execute_script("arguments[0].click();", collapseO)

    def clickOnBranchP(self):
        p = self.driver.find_element_by_xpath("//span[text()='P']")
        self.driver.execute_script("arguments[0].click();", p)

    def collapseBranchP(self):
        collapseP = self.driver.find_element_by_xpath("//span[text()='P']")
        self.driver.execute_script("arguments[0].click();", collapseP)

    def clickOnBranchQ(self):
        q = self.driver.find_element_by_xpath("//span[text()='Q']")
        self.driver.execute_script("arguments[0].click();", q)

    def collapseBranchQ(self):
        collapseQ = self.driver.find_element_by_xpath("//span[text()='Q']")
        self.driver.execute_script("arguments[0].click();", collapseQ)

    def clickOnBranchR(self):
        r = self.driver.find_element_by_xpath("//span[text()='R']")
        self.driver.execute_script("arguments[0].click();", r)

    def collapseBranchR(self):
        collapseR = self.driver.find_element_by_xpath("//span[text()='R']")
        self.driver.execute_script("arguments[0].click();", collapseR)

    def clickOnBranchS(self):
        s = self.driver.find_element_by_xpath("//span[text()='S']")
        self.driver.execute_script("arguments[0].click();", s)

    def collapseBranchS(self):
        collapseS = self.driver.find_element_by_xpath("//span[text()='S']")
        self.driver.execute_script("arguments[0].click();", collapseS)

    def clickOnBranchT(self):
        t = self.driver.find_element_by_xpath("//span[text()='T']")
        self.driver.execute_script("arguments[0].click();", t)

    def collapseBranchT(self):
        collapseT = self.driver.find_element_by_xpath("//span[text()='T']")
        self.driver.execute_script("arguments[0].click();", collapseT)

    def clickOnBranchU(self):
        u = self.driver.find_element_by_xpath("//span[text()='U']")
        self.driver.execute_script("arguments[0].click();", u)

    def collapseBranchU(self):
        collapseU = self.driver.find_element_by_xpath("//span[text()='U']")
        self.driver.execute_script("arguments[0].click();", collapseU)

    def clickOnBranchV(self):
        v = self.driver.find_element_by_xpath("//span[text()='V']")
        self.driver.execute_script("arguments[0].click();", v)

    def collapseBranchV(self):
        collapseV = self.driver.find_element_by_xpath("//span[text()='V']")
        self.driver.execute_script("arguments[0].click();", collapseV)

    def clickOnBranchW(self):
        w = self.driver.find_element_by_xpath("//span[text()='W']")
        self.driver.execute_script("arguments[0].click();", w)

    def collapseBranchW(self):
        collapseW = self.driver.find_element_by_xpath("//span[text()='W']")
        self.driver.execute_script("arguments[0].click();", collapseW)

    def clickOnBranchX(self):
        x = self.driver.find_element_by_xpath("//span[text()='X']")
        self.driver.execute_script("arguments[0].click();", x)

    def collapseBranchX(self):
        collapseX = self.driver.find_element_by_xpath("//span[text()='X']")
        self.driver.execute_script("arguments[0].click();", collapseX)

    def clickOnBranchY(self):
        y = self.driver.find_element_by_xpath("//span[text()='Y']")
        self.driver.execute_script("arguments[0].click();", y)

    def collapseBranchY(self):
        collapseY = self.driver.find_element_by_xpath("//span[text()='Y']")
        self.driver.execute_script("arguments[0].click();", collapseY)

    def clickOnBranchZ(self):
        z = self.driver.find_element_by_xpath("//span[text()='Z']")
        self.driver.execute_script("arguments[0].click();", z)

    def collapseBranchZ(self):
        collapseZ = self.driver.find_element_by_link_text("Z")
        self.driver.execute_script("arguments[0].click();", collapseZ)

    def clickOnFullTextSearch(self):
        self.driver.find_element_by_xpath(self.fulltextsearch_xpath).click()

    def clickOnExpandSearch(self):
        self.driver.find_element_by_xpath(self.expandSearch_xpath).click()

    def clickActions(self):
        actions = self.driver.find_element(By.XPATH, self.actionsclick_xpath)
        self.driver.execute_script("arguments[0].click();", actions)

    def clickResearchNotepad(self):
        notepad = self.driver.find_element(By.XPATH, self.researchNotepadActions_xpath)
        self.driver.execute_script("arguments[0].click();", notepad)

    def clickOnFirstLinkMainBranch(self):
        firstLink = self.driver.find_element(By.XPATH, self.mainBranchFirstLink_xpath)
        self.driver.execute_script("arguments[0].click();", firstLink)

    def crossReferences(self):
        textTitle = self.driver.find_element(By.XPATH, self.crossRef_xpath)
        cross = textTitle.text
        return cross

    def clickOnInnerCardHeader(self):
        crossRefink = self.driver.find_element(By.XPATH, self.innerCardHeader_xpath)
        self.driver.execute_script("arguments[0].click();", crossRefink)

    def clickOnInnerFirstLink(self):
        firstLink = self.driver.find_element(By.XPATH, self.firstLink_xpath)
        self.driver.execute_script("arguments[0].click();", firstLink)

    def clickOnFullCaseAnalysis(self):
        fullCaseAnalysis = self.driver.find_element(By.XPATH, self.fullCaseAnalysis_xpath)
        self.driver.execute_script("arguments[0].click();", fullCaseAnalysis)

    def clickOnSubjectNavigatorMenu(self):
        subjectNavigator = self.driver.find_element(By.XPATH, self.subjectNavigatorMenu_xpath)
        self.driver.execute_script("arguments[0].click();", subjectNavigator)

    def clickOnSubjectNavigatorLink(self):
        subjectNavigatorLink = self.driver.find_element(By.XPATH, self.subjectNavigatorExpandLink_xpath)
        self.driver.execute_script("arguments[0].click();", subjectNavigatorLink)

    def clickOnViewSubjectNavigator(self):
        subjectNavigatorView = self.driver.find_element(By.XPATH, self.viewSubjectNavigator_xpath)
        self.driver.execute_script("arguments[0].click();", subjectNavigatorView)

    def clickOnCopyCitation(self):
        copyCitation = self.driver.find_element(By.XPATH, self.copyCitation_xpath)
        self.driver.execute_script("arguments[0].click();", copyCitation)

    def clickOnViewPDF(self):
        viewPDF = self.driver.find_element(By.XPATH, self.viewPDF_xpath)
        self.driver.execute_script("arguments[0].click();", viewPDF)

    def clickOnDownloadDocument(self):
        downloadDoc = self.driver.find_element(By.XPATH, self.downloadDocument_xpath)
        self.driver.execute_script("arguments[0].click();", downloadDoc)

    def clickOnDocumentComparison(self):
        documentComparison = self.driver.find_element(By.XPATH, self.documentComparison_xpath)
        self.driver.execute_script("arguments[0].click();", documentComparison)

    def selectDocumentComparisonOption(self):
        selectOptionComparison = self.driver.find_element(By.XPATH, self.documentComparisonOption_xpath)
        self.driver.execute_script("arguments[0].click();", selectOptionComparison)

    def clickOnAddDocumentCompare(self):
        addCompare = self.driver.find_element(By.XPATH, self.documentComparisonAdd_xpath)
        self.driver.execute_script("arguments[0].click();", addCompare)

    def clickOnResearch(self):
        researchNotepad = self.driver.find_element(By.XPATH, self.researchNotepad_xpath)
        self.driver.execute_script("arguments[0].click();", researchNotepad)

    def selectResearchOption(self):
        researchOption = self.driver.find_element(By.XPATH, self.researchOption_xpath)
        self.driver.execute_script("arguments[0].click();", researchOption)

    def clickOnAddNotepad(self):
        addNote = self.driver.find_element(By.XPATH, self.addNotepad_xpath)
        self.driver.execute_script("arguments[0].click();", addNote)

    def clickOnActionsDropdown(self):
        actionsDropdown = self.driver.find_element(By.XPATH, self.actions_xpath)
        self.driver.execute_script("arguments[0].click();", actionsDropdown)

    def clickOnResearchNotepadDropdown(self):
        researchNotepad = self.driver.find_element(By.XPATH, self.researchNotepadDropdown_xpath)
        self.driver.execute_script("arguments[0].click();", researchNotepad)

    def checkBookMarkError(self):
        bookmarkError = self.driver.find_element(By.XPATH, self.bookmarkError_xpath)
        error = bookmarkError.text
        return error

    def clickOnCopyLocationDropdown(self):
        copyLocation = self.driver.find_element(By.XPATH, self.copyLocationDropdown_xpath)
        self.driver.execute_script("arguments[0].click();", copyLocation)

    def clickOnCancelResearch(self):
        cancelResearch = self.driver.find_element(By.XPATH, self.researchNotepadCancel_xpath)
        self.driver.execute_script("arguments[0].click();", cancelResearch)

    def checkToastMessage(self):
        toastMessage = self.driver.find_element(By.XPATH, self.copyLocationToastMessage_xpath)
        message = toastMessage.text
        time.sleep(10)
        return message




