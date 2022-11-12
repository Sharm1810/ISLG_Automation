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


