import time
from selenium.webdriver.support.ui import Select


class SubjectNavigator:
    subjectNavigatormenu_cssselector = "#Rslink > li:nth-child(1) > a"
    clientListing_cssseelector = "#dvClientListing > div > button"
    subjectNavigatorHeading_xpath = "//*[@id='page-content']/div/div[3]/div/div[1]/h1"
    subjectTextsearch_textbox_cssselector = "#txtSubjectNavigatorSearch"
    textFind_button_id = "btnSearchSnTreeData"
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
        self.driver.find_element_by_id(self.textFind_button_id).click()

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
        time.sleep(10)
        print("Before")
        #self.driver.find_element_by_xpath(self. branchA_xpath).click()
        #a = self.driver.find_element_by_xpath(self. branchA_xpath)
        #self.driver.execute_script("arguments[0].click();", a)
        #self.driver.find_element_by_xpath("//div[contains(@id,'item-list-2ba0e-1')]/..//a")
        e = self.driver.find_element_by_xpath("//a[contains(@title,'A')]")
        self.driver.execute_script("arguments[0].click();", e)
        print("A")

    def collapseBranchA(self):
        collapseA = self.driver.find_element_by_link_text("A")
        self.driver.execute_script("arguments[0].click();", collapseA)

    def clickOnBranchB(self):
        self.driver.find_element_by_link_text(self.branchB_link).click()

    def collapseBranchB(self):
        collapseB = self.driver.find_element_by_link_text("B")
        self.driver.execute_script("arguments[1].click();", collapseB)

    def clickOnBranchC(self):
        self.driver.find_element_by_link_text(self.branchC_xpath).click()

    def collapseBranchC(self):
        collapseC = self.driver.find_element_by_link_text("C")
        self.driver.execute_script("arguments[2].click();", collapseC)

    def clickOnBranchD(self):
        self.driver.find_element_by_link_text(self.branchD_xpath).click()

    def collapseBranchD(self):
        collapseD = self.driver.find_element_by_link_text("D")
        self.driver.execute_script("arguments[3].click();", collapseD)

    def clickOnBranchE(self):
        self.driver.find_element_by_link_text(self.branchE_xpath).click()

    def collapseBranchE(self):
        collapseE = self.driver.find_element_by_link_text("E")
        self.driver.execute_script("arguments[0].click();", collapseE)

    def clickOnBranchF(self):
        self.driver.find_element_by_link_text(self.branchF_xpath).click()

    def collapseBranchF(self):
        collapseF = self.driver.find_element_by_link_text("F")
        self.driver.execute_script("arguments[0].click();", collapseF)

    def clickOnBranchG(self):
        self.driver.find_element_by_link_text(self.branchG_xpath).click()

    def collapseBranchG(self):
        collapseG = self.driver.find_element_by_link_text("G")
        self.driver.execute_script("arguments[0].click();", collapseG)

    def clickOnBranchH(self):
        self.driver.find_element_by_link_text(self.branchH_xpath).click()

    def collapseBranchH(self):
        collapseH = self.driver.find_element_by_link_text("H")
        self.driver.execute_script("arguments[0].click();", collapseH)

    def clickOnBranchI(self):
        self.driver.find_element_by_link_text(self.branchI_xpath).click()

    def collapseBranchI(self):
        collapseI = self.driver.find_element_by_link_text("I")
        self.driver.execute_script("arguments[0].click();", collapseI)

    def clickOnBranchJ(self):
        self.driver.find_element_by_link_text(self.branchJ_xpath).click()

    def collapseBranchJ(self):
        collapseH = self.driver.find_element_by_link_text("H")
        self.driver.execute_script("arguments[0].click();", collapseH)

    def clickOnBranchK(self):
        self.driver.find_element_by_link_text(self.branchK_xpath).click()

    def collapseBranchK(self):
        collapseK = self.driver.find_element_by_link_text("K")
        self.driver.execute_script("arguments[0].click();", collapseK)

    def clickOnBranchL(self):
        self.driver.find_element_by_link_text(self.branchL_xpath).click()

    def collapseBranchL(self):
        collapseL = self.driver.find_element_by_link_text("L")
        self.driver.execute_script("arguments[0].click();", collapseL)

    def clickOnBranchM(self):
        self.driver.find_element_by_link_text(self.branchM_xpath).click()

    def collapseBranchM(self):
        collapseM = self.driver.find_element_by_link_text("M")
        self.driver.execute_script("arguments[0].click();", collapseM)

    def clickOnBranchN(self):
        self.driver.find_element_by_link_text(self.branchN_xpath).click()

    def collapseBranchN(self):
        collapseN = self.driver.find_element_by_link_text("N")
        self.driver.execute_script("arguments[0].click();", collapseN)

    def clickOnBranchO(self):
        self.driver.find_element_by_link_text(self.branchO_xpath).click()

    def collapseBranchO(self):
        collapseO = self.driver.find_element_by_link_text("O")
        self.driver.execute_script("arguments[0].click();", collapseO)

    def clickOnBranchP(self):
        self.driver.find_element_by_link_text(self.branchP_xpath).click()

    def collapseBranchQ(self):
        collapseQ = self.driver.find_element_by_link_text("Q")
        self.driver.execute_script("arguments[0].click();", collapseQ)

    def clickOnBranchQ(self):
        self.driver.find_element_by_link_text(self.branchQ_xpath).click()

    def collapseBranchQ(self):
        collapseQ = self.driver.find_element_by_link_text("Q")
        self.driver.execute_script("arguments[0].click();", collapseQ)

    def clickOnBranchR(self):
        self.driver.find_element_by_link_text(self.branchR_xpath).click()

    def collapseBranchR(self):
        collapseR = self.driver.find_element_by_link_text("R")
        self.driver.execute_script("arguments[0].click();", collapseR)

    def clickOnBranchS(self):
        self.driver.find_element_by_link_text(self.branchS_xpath).click()

    def collapseBranchS(self):
        collapseS = self.driver.find_element_by_link_text("S")
        self.driver.execute_script("arguments[0].click();", collapseS)

    def clickOnBranchT(self):
        self.driver.find_element_by_link_text(self.branchT_xpath).click()

    def collapseBranchT(self):
        collapseT = self.driver.find_element_by_link_text("T")
        self.driver.execute_script("arguments[0].click();", collapseT)

    def clickOnBranchU(self):
        self.driver.find_element_by_link_text(self.branchU_xpath).click()

    def collapseBranchU(self):
        collapseU = self.driver.find_element_by_link_text("U")
        self.driver.execute_script("arguments[0].click();", collapseU)

    def clickOnBranchV(self):
        self.driver.find_element_by_link_text(self.branchV_xpath).click()

    def collapseBranchV(self):
        collapseV = self.driver.find_element_by_link_text("V")
        self.driver.execute_script("arguments[0].click();", collapseV)

    def clickOnBranchW(self):
        self.driver.find_element_by_link_text(self.branchW_xpath).click()

    def collapseBranchW(self):
        collapseW = self.driver.find_element_by_link_text("W")
        self.driver.execute_script("arguments[0].click();", collapseW)

    def clickOnBranchX(self):
        self.driver.find_element_by_link_text(self.branchX_xpath).click()

    def collapseBranchX(self):
        collapseX = self.driver.find_element_by_link_text("X")
        self.driver.execute_script("arguments[0].click();", collapseX)

    def clickOnBranchY(self):
        self.driver.find_element_by_link_text(self.branchY_xpath).click()

    def collapseBranchY(self):
        collapseY = self.driver.find_element_by_link_text("E")
        self.driver.execute_script("arguments[0].click();", collapseY)

    def clickOnBranchZ(self):
        self.driver.find_element_by_link_text(self.branchZ_xpath).click()

    def collapseBranchZ(self):
        collapseZ = self.driver.find_element_by_link_text("Z")
        self.driver.execute_script("arguments[0].click();", collapseZ)

    def clcikOnFullTextSearch(self):
        self.driver.find_element_by_xpath(self.fulltextsearch_xpath).click()

    def clickOnExpandSearch(self):
        self.driver.find_element_by_xpath(self.expandSearch_xpath).click()
