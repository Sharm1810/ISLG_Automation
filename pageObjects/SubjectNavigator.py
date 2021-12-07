import time
from selenium.webdriver.support.ui import Select


class SubjectNavigator:
    subjectNavigatormenu_cssselector = "#Rslink > li:nth-child(1) > a"
    clientListing_cssseelector = "#dvClientListing > div > button"
    subjectNavigatorHeading_xpath = "//*[@id='page-content']/div/div[3]/div/div[1]/h1"
    subjectTextsearch_textbox_cssselector = "#txtSubjectNavigatorSearch"
    textFind_button_id = "btnSearchSnTreeData"
    resetLink_xpath = "//*[@id='dvSubjectNavigatorSearchBranch']/a"
    branchNameA_xpath = "//*[@id='item-list-item-1-control']/i"
    viewContextlink_xpath = "//*[@id='item-list-item-1']/div/div[1]/div[1]/a[2]"
    actionsButton_xpath = "//*[@id='item-list-item-11241-card-11241-actions-control']"
    researchNotepadlink_xpath = "//*[@id='item-list-item-11241-card-11241-actions']/p/a[1]"
    fulltextSearchlink_xpath = "//*[@id='item-list-item-11241-card-11241-actions']/p/a[2]"
    card_button_xpath = "//*[@id='btnCard']"
    compact_button_xpath = "//*[@id='btnCompact']/i"
    branchA_xpath = "//*[@id='spanBranchName-1']"
    branchB_xpath = "//*[@id='spanBranchName-2']"
    branchC_xpath = "//*[@id='spanBranchName-3']"
    branchD_xpath = "//*[@id='spanBranchName-4']"
    branchE_xpath = "//*[@id='spanBranchName-5']"
    branchF_xpath = "//*[@id='spanBranchName-6']"
    branchG_xpath = "//*[@id='spanBranchName-7']"
    branchH_xpath = "//*[@id='spanBranchName-8']"
    branchI_xpath = "//*[@id='spanBranchName-9']"
    branchJ_xpath = "//*[@id='spanBranchName-10']"
    branchK_xpath = "//*[@id='spanBranchName-11']"
    branchL_xpath = "//*[@id='spanBranchName-12']"
    branchM_xpath = "//*[@id='spanBranchName-13']"
    branchN_xpath = "//*[@id='spanBranchName-14']"
    branchO_xpath = "//*[@id='spanBranchName-15']"
    branchP_xpath = "//*[@id='spanBranchName-16']"
    branchQ_xpath = "//*[@id='spanBranchName-17']"
    branchR_xpath = "//*[@id='spanBranchName-18']"
    branchS_xpath = "//*[@id='spanBranchName-19']"
    branchT_xpath = "//*[@id='spanBranchName-20']"
    branchU_xpath = "//*[@id='spanBranchName-21']"
    branchV_xpath = "//*[@id='spanBranchName-22']"
    branchW_xpath = "//*[@id='spanBranchName-23']"
    branchX_xpath = "//*[@id='spanBranchName-24']"
    branchY_xpath = "//*[@id='spanBranchName-25']"
    branchZ_xpath = "//*[@id='spanBranchName-26']"
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
        self.driver.find_element_by_xpath(self.branchNameA_xpath).click()

    def clickOnViewContext(self):
        self.driver.find_element_by_xpath(self.viewContextlink_xpath).click()

    def clickOnActions(self):
        self.driver.find_element_by_xpath(self.actionsButton_xpath).click()

    def clickOnResearchNotepad(self):
        self.driver.find_element_by_xpath(self.researchNotepadlink_xpath).click()

    def clickOnFulltextsearch(self):
        self.driver.find_element_by_xpath(self.fulltextSearchlink_xpath).click()

    def clickOnCard(self):
        self.driver.find_element_by_xpath(self.card_button_xpath).click()

    def clickOnCompactView(self):
        self.driver.find_element_by_xpath(self.compact_button_xpath).click()

    def clickOnBranchA(self):
        self.driver.find_element_by_xpath(self.branchNameA_xpath).click()

    def clickOnBranchB(self):
        self.driver.find_element_by_xpath(self.branchB_xpath).click()

    def clickOnBranchC(self):
        self.driver.find_element_by_xpath(self.branchC_xpath).click()

    def clickOnBranchD(self):
        self.driver.find_element_by_xpath(self.branchD_xpath).click()

    def clickOnBranchE(self):
        self.driver.find_element_by_xpath(self.branchE_xpath).click()

    def clickOnBranchF(self):
        self.driver.find_element_by_xpath(self.branchF_xpath).click()

    def clickOnBranchG(self):
        self.driver.find_element_by_xpath(self.branchG_xpath).click()

    def clickOnBranchH(self):
        self.driver.find_element_by_xpath(self.branchH_xpath).click()

    def clickOnBranchI(self):
        self.driver.find_element_by_xpath(self.branchI_xpath).click()

    def clickOnBranchJ(self):
        self.driver.find_element_by_xpath(self.branchJ_xpath).click()

    def clickOnBranchK(self):
        self.driver.find_element_by_xpath(self.branchK_xpath).click()

    def clickOnBranchL(self):
        self.driver.find_element_by_xpath(self.branchL_xpath).click()

    def clickOnBranchM(self):
        self.driver.find_element_by_xpath(self.branchM_xpath).click()

    def clickOnBranchN(self):
        self.driver.find_element_by_xpath(self.branchN_xpath).click()

    def clickOnBranchO(self):
        self.driver.find_element_by_xpath(self.branchO_xpath).click()

    def clickOnBranchP(self):
        self.driver.find_element_by_xpath(self.branchP_xpath).click()

    def clickOnBranchQ(self):
        self.driver.find_element_by_xpath(self.branchQ_xpath).click()

    def clickOnBranchR(self):
        self.driver.find_element_by_xpath(self.branchR_xpath).click()

    def clickOnBranchS(self):
        self.driver.find_element_by_xpath(self.branchS_xpath).click()

    def clickOnBranchT(self):
        self.driver.find_element_by_xpath(self.branchT_xpath).click()

    def clickOnBranchU(self):
        self.driver.find_element_by_xpath(self.branchU_xpath).click()

    def clickOnBranchV(self):
        self.driver.find_element_by_xpath(self.branchV_xpath).click()

    def clickOnBranchW(self):
        self.driver.find_element_by_xpath(self.branchW_xpath).click()

    def clickOnBranchX(self):
        self.driver.find_element_by_xpath(self.branchX_xpath).click()

    def clickOnBranchY(self):
        self.driver.find_element_by_xpath(self.branchY_xpath).click()

    def clickOnBranchZ(self):
        self.driver.find_element_by_xpath(self.branchZ_xpath).click()

    def clcikOnFullTextSearch(self):
        self.driver.find_element_by_xpath(self.fulltextsearch_xpath).click()

    def clickOnExpandSearch(self):
        self.driver.find_element_by_xpath(self.expandSearch_xpath).click()
