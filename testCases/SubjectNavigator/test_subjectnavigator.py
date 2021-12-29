import pytest
import time
from pageObjects.LoginPage import LoginPage
from pageObjects.SubjectNavigator import SubjectNavigator
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import string
import pyperclip

import random


class Test_002_SubjectNavigator:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_subjectNaviagtor(self, setup):
        self.logger.info("****TestCase 001 - Verify Subject Navigator menu***")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("*****Login Successful****")
        self.logger.info("**** Subject Navigator testing *****")

        self.navigator = SubjectNavigator(self.driver)
        self.navigator.clickOnSubjectNavigatormenu()
        self.navigator.clickOnClientListing()
        self.logger.info("Subject Navigator menu is available")
        self.driver.quit()

    @pytest.mark.regression
    def test_parentBranchcheck(self, setup):
        self.logger.info("***Test Case 002 - Verify Parent Branches***")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("*****Login Successful****")
        self.navigator = SubjectNavigator(self.driver)
        self.navigator.clickOnSubjectNavigatormenu()
        self.navigator.clickOnClientListing()
        self.navigator.clickOnBranchA()
        print("BranchA")
        parentBranchA = self.driver.find_element_by_link_text("A").text
        if parentBranchA == "A":
            assert True == True
            self.logger.info("***ParentBranch A was clicked***")
            self.driver.save_screenshot(".\\Screenshots\\" + "parentBranchA.png")
        else:
                assert True == False
                self.logger.info("***Missing Parent Branch A***")
                self.driver.save_screenshot(".\\Screenshots\\" + "missingParentBranchA.png")
        time.sleep(3)
        self.navigator.collapseBranchA()

        self.navigator.clickOnBranchB()
        parentBranchB = self.driver.find_element_by_link_text("B").text
        if parentBranchB == "B":
            assert True == True
            self.logger.info("***ParentBranch B was clicked***")
            self.driver.save_screenshot(".\\Screenshots\\" + "parentBranchB.png")
        else:
            assert True == False
            self.logger.info("***Missing Parent Branch B***")
            self.driver.save_screenshot(".\\Screenshots\\" + "missingParentBranchB.png")
        collapseB = self.driver.find_element_by_link_text("B")
        self.driver.execute_script("arguments[0].click();", collapseB)

        self.navigator.collapseBranchC()
        parentBranchC = self.driver.find_element_by_xpath("C").text
        if parentBranchC == "C":
            assert True == True
            self.logger.info("***ParentBranch C was clicked***")
            self.driver.save_screenshot(".\\Screenshots\\" + "parentBranchC.png")
        else:
            assert True == False
            self.logger.info("***Missing Parent Branch C***")
            self.driver.save_screenshot(".\\Screenshots\\" + "missingParentBranchC.png")
        time.sleep(3)
        collapseC = self.driver.find_element_by_link_text("C")
        self.driver.execute_script("arguments[2].click();", collapseC)

        parentBranchD = self.driver.find_element_by_xpath("//*[@id='spanBranchName-4']").text
        if parentBranchD == "D":
            assert True == True
            self.logger.info("***ParentBranch D was clicked***")
            self.driver.save_screenshot(".\\Screenshots\\" + "parentBranchD.png")
        else:
            assert True == False
            self.logger.info("***Missing Parent Branch D***")
            self.driver.save_screenshot(".\\Screenshots\\" + "missingParentBranchD.png")
        time.sleep(2)
        collapseD = self.driver.find_element_by_link_text("D")
        self.driver.execute_script("arguments[0].click();", collapseD)

        self.navigator.clickOnBranchE()
        parentBranchE = self.driver.find_element_by_xpath("//*[@id='spanBranchName-5']").text
        if parentBranchE == "E":
            assert True == True
            self.logger.info("***ParentBranch E was clicked***")
            self.driver.save_screenshot(".\\Screenshots\\" + "parentBranchE.png")
        else:
            assert True == False
            self.logger.info("***Missing Parent Branch E***")
            self.driver.save_screenshot(".\\Screenshots\\" + "missingParentBranchE.png")
        time.sleep(2)
        self.navigator.collapseBranchE()

        self.navigator.clickOnBranchF()
        parentBranchF = self.driver.find_element_by_xpath("//*[@id='spanBranchName-6']").text
        if parentBranchF == "F":
            assert True == True
            self.logger.info("***ParentBranch F was clicked***")
            self.driver.save_screenshot(".\\Screenshots\\" + "parentBranchF.png")
        else:
            assert True == False
            self.logger.info("***Missing Parent Branch F***")
            self.driver.save_screenshot(".\\Screenshots\\" + "missingParentBranchF.png")
        # self.navigator.clickOnBranchF()
        self.driver.find_element_by_link_text("F").click()
        time.sleep(2)
        self.navigator.collapseBranchF()

        parentBranchG = self.driver.find_element_by_xpath("//*[@id='spanBranchName-7']").text
        if parentBranchG == "G":
            assert True == True
            self.logger.info("***ParentBranch G was clicked***")
            self.driver.save_screenshot(".\\Screenshots\\" + "parentBranchG.png")
        else:
            assert True == False
            self.logger.info("***Missing Parent Branch G***")
            self.driver.save_screenshot(".\\Screenshots\\" + "missingParentBranchG.png")
        # self.navigator.clickOnBranchG()
        self.driver.find_element_by_link_text("G").click()
        time.sleep(3)

        parentBranchH = self.driver.find_element_by_xpath("//*[@id='spanBranchName-8']").text
        if parentBranchH == "H":
            assert True == True
            self.logger.info("***ParentBranch H was clicked***")
            self.driver.save_screenshot(".\\Screenshots\\" + "parentBranchH.png")
        else:
            assert True == False
            self.logger.info("***Missing Parent Branch H***")
            self.driver.save_screenshot(".\\Screenshots\\" + "missingParentBranchH.png")
        self.navigator.clickOnBranchH()

        parentBranchI = self.driver.find_element_by_xpath("//*[@id='spanBranchName-9']").text
        if parentBranchI == "I":
            assert True == True
            self.logger.info("***ParentBranch I was clicked***")
            self.driver.save_screenshot(".\\Screenshots\\" + "parentBranchI.png")
        else:
            assert True == False
            self.logger.info("***Missing Parent Branch I***")
            self.driver.save_screenshot(".\\Screenshots\\" + "missingParentBranchI.png")
        self.navigator.clickOnBranchI()
        time.sleep(1)

        parentBranchJ = self.driver.find_element_by_xpath("//*[@id='spanBranchName-10']").text
        if parentBranchJ == "J":
            assert True == True
            self.logger.info("***ParentBranch J was clicked***")
            self.driver.save_screenshot(".\\Screenshots\\" + "parentBranchJ.png")
        else:
            assert True == False
            self.logger.info("***Missing Parent Branch J***")
            self.driver.save_screenshot(".\\Screenshots\\" + "missingParentBranchJ.png")
        self.navigator.clickOnBranchJ()

        parentBranchK = self.driver.find_element_by_xpath("//*[@id='spanBranchName-11']").text
        if parentBranchK == "K":
            assert True == True
            self.logger.info("***ParentBranch K was clicked***")
            self.driver.save_screenshot(".\\Screenshots\\" + "parentBranchK.png")
        else:
            assert True == False
            self.logger.info("***Missing Parent Branch K***")
            self.driver.save_screenshot(".\\Screenshots\\" + "missingParentBranchK.png")
        self.navigator.clickOnBranchK()

        parentBranchL = self.driver.find_element_by_xpath("//*[@id='spanBranchName-12']").text
        if parentBranchL == "L":
            assert True == True
            self.logger.info("***ParentBranch L was clicked***")
            self.driver.save_screenshot(".\\Screenshots\\" + "parentBranchL.png")
        else:
            assert True == False
            self.logger.info("***Missing Parent Branch L***")
            self.driver.save_screenshot(".\\Screenshots\\" + "missingParentBranchL.png")
        self.navigator.clickOnBranchL()
        time.sleep(2)

        parentBranchM = self.driver.find_element_by_xpath("//*[@id='spanBranchName-13']").text
        if parentBranchM == "M":
            assert True == True
            self.logger.info("***ParentBranch M was clicked***")
            self.driver.save_screenshot(".\\Screenshots\\" + "parentBranchM.png")
        else:
            assert True == False
            self.logger.info("***Missing Parent Branch M***")
            self.driver.save_screenshot(".\\Screenshots\\" + "missingParentBranchM.png")
        self.navigator.clickOnBranchM()
        time.sleep(2)

        parentBranchN = self.driver.find_element_by_xpath("//*[@id='spanBranchName-14']").text
        if parentBranchN == "N":
            assert True == True
            self.logger.info("***ParentBranch N was clicked***")
            self.driver.save_screenshot(".\\Screenshots\\" + "parentBranchN.png")
        else:
            assert True == False
            self.logger.info("***Missing Parent Branch N***")
            self.driver.save_screenshot(".\\Screenshots\\" + "missingParentBranchN.png")
        self.navigator.clickOnBranchN()
        time.sleep(2)

        parentBranchO = self.driver.find_element_by_xpath("//*[@id='spanBranchName-15']").text
        if parentBranchO == "O":
            assert True == True
            self.logger.info("***ParentBranch O was clicked***")
            self.driver.save_screenshot(".\\Screenshots\\" + "parentBranchO.png")
        else:
            assert True == False
            self.logger.info("***Missing Parent Branch O***")
            self.driver.save_screenshot(".\\Screenshots\\" + "missingParentBranchO.png")
        self.navigator.clickOnBranchO()
        time.sleep(2)

        parentBranchP = self.driver.find_element_by_xpath("//*[@id='spanBranchName-16']").text
        if parentBranchP == "P":
            assert True == True
            self.logger.info("***ParentBranch P was clicked***")
            self.driver.save_screenshot(".\\Screenshots\\" + "parentBranchP.png")
        else:
            assert True == False
            self.logger.info("***Missing Parent Branch P***")
            self.driver.save_screenshot(".\\Screenshots\\" + "missingParentBranchP.png")
        self.navigator.clickOnBranchP()

        parentBranchQ = self.driver.find_element_by_xpath("//*[@id='spanBranchName-17']").text
        if parentBranchQ == "Q":
            assert True == True
            self.logger.info("***ParentBranch Q was clicked***")
            self.driver.save_screenshot(".\\Screenshots\\" + "parentBranchQ.png")
        else:
            assert True == False
            self.logger.info("***Missing Parent Branch Q***")
            self.driver.save_screenshot(".\\Screenshots\\" + "missingParentBranchQ.png")
        self.navigator.clickOnBranchQ()
        time.sleep(2)

        parentBranchR = self.driver.find_element_by_xpath("//*[@id='spanBranchName-18']").text
        if parentBranchR == "R":
            assert True == True
            self.logger.info("***ParentBranch R was clicked***")
            self.driver.save_screenshot(".\\Screenshots\\" + "parentBranchR.png")
        else:
            assert True == False
            self.logger.info("***Missing Parent Branch R***")
            self.driver.save_screenshot(".\\Screenshots\\" + "missingParentBranchR.png")
        self.navigator.clickOnBranchR()
        time.sleep(2)

        parentBranchS = self.driver.find_element_by_xpath("//*[@id='spanBranchName-19']").text
        if parentBranchS == "S":
            assert True == True
            self.logger.info("***ParentBranch S was clicked***")
            self.driver.save_screenshot(".\\Screenshots\\" + "parentBranchS.png")
        else:
            assert True == False
            self.logger.info("***Missing Parent Branch C***")
            self.driver.save_screenshot(".\\Screenshots\\" + "missingParentBranchS.png")
        self.navigator.clickOnBranchS()
        time.sleep(2)

        parentBranchT = self.driver.find_element_by_xpath("//*[@id='spanBranchName-20']").text
        if parentBranchT == "T":
            assert True == True
            self.logger.info("***ParentBranch T was clicked***")
            self.driver.save_screenshot(".\\Screenshots\\" + "parentBranchT.png")
        else:
            assert True == False
            self.logger.info("***Missing Parent Branch T***")
            self.driver.save_screenshot(".\\Screenshots\\" + "missingParentBranchT.png")
        self.navigator.clickOnBranchT()
        time.sleep(2)

        parentBranchU = self.driver.find_element_by_xpath("//*[@id='spanBranchName-21']").text
        if parentBranchU == "U":
            assert True == True
            self.logger.info("***ParentBranch U was clicked***")
            self.driver.save_screenshot(".\\Screenshots\\" + "parentBranchU.png")
        else:
            assert True == False
            self.logger.info("***Missing Parent Branch U***")
            self.driver.save_screenshot(".\\Screenshots\\" + "missingParentBranchU.png")
        self.navigator.clickOnBranchU()
        time.sleep(2)

        parentBranchV = self.driver.find_element_by_xpath("//*[@id='spanBranchName-22']").text
        if parentBranchV == "V":
            assert True == True
            self.logger.info("***ParentBranch V was clicked***")
            self.driver.save_screenshot(".\\Screenshots\\" + "parentBranchV.png")
        else:
            assert True == False
            self.logger.info("***Missing Parent Branch V***")
            self.driver.save_screenshot(".\\Screenshots\\" + "missingParentBranchV.png")
        self.navigator.clickOnBranchV()
        time.sleep(2)

        parentBranchW = self.driver.find_element_by_xpath("//*[@id='spanBranchName-23']").text
        if parentBranchW == "W":
            assert True == True
            self.logger.info("***ParentBranch W was clicked***")
            self.driver.save_screenshot(".\\Screenshots\\" + "parentBranchW.png")
        else:
            assert True == False
            self.logger.info("***Missing Parent Branch W***")
            self.driver.save_screenshot(".\\Screenshots\\" + "missingParentBranchW.png")
        self.navigator.clickOnBranchW()
        time.sleep(2)

        parentBranchX = self.driver.find_element_by_xpath("//*[@id='spanBranchName-24']").text
        if parentBranchX == "X":
            assert True == True
            self.logger.info("***ParentBranch X was clicked***")
            self.driver.save_screenshot(".\\Screenshots\\" + "parentBranchX.png")
        else:
            assert True == False
            self.logger.info("***Missing Parent Branch X***")
            self.driver.save_screenshot(".\\Screenshots\\" + "missingParentBranchX.png")
        self.navigator.clickOnBranchX()

        parentBranchY = self.driver.find_element_by_xpath("//*[@id='spanBranchName-25']").text
        if parentBranchY == "Y":
            assert True == True
            self.logger.info("***ParentBranch Y was clicked***")
            self.driver.save_screenshot(".\\Screenshots\\" + "parentBranchY.png")
        else:
            assert True == False
            self.logger.info("***Missing Parent Branch Y***")
            self.driver.save_screenshot(".\\Screenshots\\" + "missingParentBranchY.png")
        self.navigator.clickOnBranchY()

        parentBranchZ = self.driver.find_element_by_xpath("//*[@id='spanBranchName-26']").text
        if parentBranchZ == "Z":
            assert True == True
            self.logger.info("***ParentBranch Z was clicked***")
            self.driver.save_screenshot(".\\Screenshots\\" + "parentBranchZ.png")
        else:
            assert True == False
            self.logger.info("***Missing Parent Branch C***")
            self.driver.save_screenshot(".\\Screenshots\\" + "missingParentBranchZ.png")
        self.navigator.clickOnBranchZ()
        self.logger.info("**** Expanded all parent branches *****")
        self.driver.quit()

    def test_Search(self, setup):
        self.logger.info("***Test Case 003 - Verify Search***")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("*****Login Successful****")
        self.navigator = SubjectNavigator(self.driver)
        self.navigator.clickOnSubjectNavigatormenu()
        self.navigator.clickOnClientListing()
        self.driver.find_element_by_id("txtSubjectNavigatorSearch").click()
        text = self.driver.find_element_by_css_selector("#txtSubjectNavigatorSearch")
        # entering Abuse of Right as search value
        text.send_keys("Abuse of Right")
        self.navigator.findText()

        self.msg = self.driver.find_element_by_xpath("//*[@id='page-content']/div/div[6]/div[1]").text
        print(self.msg)

        if "53 matches found" in self.msg:
            assert True == True
            self.logger.info("Results Found")
            self.driver.save_screenshot(".\\Screenshots\\" + "matchesfound.png")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "No matchesfound.png")
            self.logger.info("No Matches found")
            assert True == False
        self.logger.info("Validated Search")
        self.driver.quit()

    def test_ViewContext(self, setup):
        self.logger.info("***Test Case 004 - Verify View in Context***")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("*****Login Successful****")
        self.navigator = SubjectNavigator(self.driver)
        self.navigator.clickOnSubjectNavigatormenu()
        self.navigator.clickOnClientListing()
        self.driver.find_element_by_id("txtSubjectNavigatorSearch").click()
        text = self.driver.find_element_by_css_selector("#txtSubjectNavigatorSearch")
        # entering Abuse of Right as search value
        text.send_keys("Abuse of Right")
        self.navigator.findText()
        fhandle = self.driver.current_window_handle
        print(fhandle)
        self.driver.find_element_by_xpath("//*[@id='item-list-item-1']/div/div[1]/div[1]/a[2]").click()
        handles = []
        handles = self.driver.window_handles
        newhandle = handles[1]
        self.driver.switch_to.window(newhandle)
        self.driver.switch_to.default_content()
        self.driver.switch_to.window(handles[0])
        self.driver.quit()

    # @pytest.mark.regression
    def test_AddToResearchNotepad(self, setup):
        self.logger.info("***Test Case 005 - Verify Add To Research Notepad***")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("*****Login Successful****")
        self.navigator = SubjectNavigator(self.driver)
        self.navigator.clickOnSubjectNavigatormenu()
        self.navigator.clickOnClientListing()
        self.driver.find_element_by_id("txtSubjectNavigatorSearch").click()
        text = self.driver.find_element_by_css_selector("#txtSubjectNavigatorSearch")
        # entering Abuse of Right as search value
        text.send_keys("Abuse of Right")
        self.navigator.findText()
        self.navigator.clickOnActions()
        self.navigator.clickOnResearchNotepad()
        self.driver.find_element_by_xpath("//*[@id='TopicSelection']/ul/li[1]/label/span").click()
        self.driver.find_element_by_xpath("//*[@id='btnAddRNFirst']").click()
        time.sleep(1)
        message = self.driver.find_element_by_xpath("//*[@id='errorBMexist']").text
        if message == "Entry already exists in this topic.":
            self.logger.info("topic already exists")
            self.driver.find_element_by_xpath("//*[@id='popup-add-to-rn']/div[1]/p[2]/button[2]").click()

        self.driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
        time.sleep(1)
        self.logger.info("***Verify if the Topic is added to the motepad***")
        self.driver.find_element_by_xpath("//*[@id='aResearchNotePad']/a").click()
        select = self.driver.find_element_by_partial_link_text('t441981')
        self.driver.execute_script("arguments[0].click();", select)
        self.msg = self.driver.find_element_by_xpath("//*[@id='divBookmarksResult']/div[2]/div/div[1]/span").text
        print(self.msg)

        if "Subject Navigator" in self.msg:
            assert True == True
            self.logger.info("Results Found")
            self.driver.save_screenshot(".\\Screenshots\\" + "ResearchNotepadSubject Navigator.png")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "Subject Navigtaor not found.png")
            self.logger.info("Subject Navigator not found")
            assert True == False
        self.logger.info("Validated if Topic was added to Research Notepad")
        self.driver.quit()

    # @pytest.mark.regression
    def test_ResetLink(self, setup):
        self.logger.info("***Test Case 006 - Verify Reset Link***")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("*****Login Successful****")
        self.navigator = SubjectNavigator(self.driver)
        self.navigator.clickOnSubjectNavigatormenu()
        self.navigator.clickOnClientListing()
        self.driver.find_element_by_id("txtSubjectNavigatorSearch").click()
        text = self.driver.find_element_by_css_selector("#txtSubjectNavigatorSearch")
        # entering Abuse of Right as search value
        text.send_keys("Abuse of Right")
        self.navigator.findText()
        # self.driver.find_element_by_xpath("//*[@id='spanBranchName-1']").click()
        self.navigator.resetLink()
        if text == "":
            assert True == True
            self.logger.info("Reset link passed")
        else:
            self.logger.error("***Reset Link failed***")
        self.driver.quit()

    # @pytest.mark.regression
    def test_fullTextSearch(self, setup):
        self.logger.info("***Test Case 007 - Verify Full Text Search***")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("*****Login Successful****")
        self.navigator = SubjectNavigator(self.driver)
        self.navigator.clickOnSubjectNavigatormenu()
        self.navigator.clickOnClientListing()
        self.navigator.clickOnBranchA()
        self.navigator.clickOnActions()
        self.navigator.clickOnFulltextsearch()
        time.sleep(2)
        handles = self.driver.window_handles
        newhandle = handles[1]
        self.driver.switch_to.window(newhandle)
        self.msg = self.driver.find_element_by_xpath(
            "//*[@id='page-content']/div/div/div[1]").text

        if "Full Text Search" in self.msg:
            self.logger.info("Fulltext Search page is opened")
            print(self.msg)
            self.driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.END)
            filterlist = self.driver.find_element_by_xpath(
                "//*[@id='StaticFilters']/div[4]/div[4]/div[1]/div/div/span/span[1]/span/ul/li[1]").text
            print(filterlist)
        self.logger.info("****Full Text Search completed***")
        self.driver.switch_to.default_content()
        self.driver.switch_to.window(handles[0])
        self.driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't')
        self.driver.quit()

    # @pytest.mark.regression
    def test_copyLocation(self, setup):
        self.logger.info("***Test Case 008 - Verify Copy Location***")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("*****Login Successful****")
        self.navigator = SubjectNavigator(self.driver)
        self.navigator.clickOnSubjectNavigatormenu()
        self.navigator.clickOnClientListing()
        self.navigator.clickOnBranchA()
        self.navigator.clickOnActions()
        self.driver.find_element_by_xpath("//*[@id='item-list-item-11241-card-11241-actions']/p/a[3]").click()
        self.driver.execute_script("window.open('');")
        profile_window = self.driver.window_handles[1]
        self.driver.switch_to.window(profile_window)
        action = ActionChains(self.driver)
        action.send_keys(Keys.TAB)
        action.send_keys(Keys.TAB)
        ActionChains(self.driver).key_down(Keys.ADD).send_keys('p').key_up(Keys.CONTROL).perform()
        ActionChains(self.driver).send_keys(Keys.ENTER)
        action.key_down(Keys.Control).send_keys("v").key_up(Keys.CONTROL).perform()
        # ctrl + L
        action.send_keys(Keys.Enter).perform()
        # testgit

    # @pytest.mark.regression
    def test_expandSearch(self, setup):
        self.logger.info("***Test Case 009 - Verify Expand Search and check for Linguistic Aids***")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("*****Login Successful****")
        self.navigator = SubjectNavigator(self.driver)
        self.navigator.clickOnSubjectNavigatormenu()
        self.navigator.clickOnClientListing()
        self.navigator.clickOnExpandSearch()
        self.logger.info("****Search was expanded***")
        checkboxStemming = self.driver.find_element_by_xpath("//*[@id='chkSNStemming']")
        if checkboxStemming.is_selected():
            assert True == True
            self.logger.info("Stemming checkbox is selected by default")
        else:
            self.logger.info("Stemming checkbox is not selected")
            self.logger.info("Test case failed")
        checkboxFuzzyTypo = self.driver.find_element_by_xpath("//*[@id='chkSnFuzzyTypo']")
        if checkboxFuzzyTypo.is_selected():
            assert True == True
            self.logger.info("Fuzzy Typo is selected by default")
        else:
            self.logger.info("Fuzzy Typo checkbox is not selected")
            self.logger.info("Test Case Failed")
        self.driver.quit()

    def test_searchAllWords(self, setup):
        self.logger.info("***Test Case 010 - Verify Expand Search and select option All Words***")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("*****Login Successful****")
        self.navigator = SubjectNavigator(self.driver)
        self.navigator.clickOnSubjectNavigatormenu()
        self.navigator.clickOnClientListing()
        self.navigator.clickOnExpandSearch()
        self.logger.info("****Search was expanded***")
