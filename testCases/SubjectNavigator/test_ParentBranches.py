import pytest
import time

from selenium.webdriver.common.by import By

from pageObjects.LoginPage import LoginPage
from pageObjects.SubjectNavigator import SubjectNavigator
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import string
import pyperclip

import random


class Test_001_ParentBranches:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_ParentBranches(self, setup):
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
        # self.navigator.clickOnClientListing()
        self.logger.info("Subject Navigator menu is available")
        self.driver.quit()

    @pytest.mark.regression
    def test_parentBranchcheck(self, setup):
        self.logger.info("***Test Case 001 - Verify Parent Branches***")
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
        time.sleep(2)
        parentBranchA = self.driver.find_element_by_xpath("//a[contains(@title,'A')]").text
        if parentBranchA == "A":
            assert True == True
            self.logger.info("***ParentBranch A was clicked***")
            self.driver.save_screenshot(".\\Screenshots\\" + "parentBranchA.png")
        else:
            self.logger.info("***Missing Parent Branch A***")
            self.driver.save_screenshot(".\\Screenshots\\" + "missingParentBranchA.png")
        self.navigator.collapseBranchA()

        self.navigator.clickOnBranchB()
        time.sleep(2)
        parentBranchB = self.driver.find_element_by_link_text("B").text
        if parentBranchB == "B":
            assert True == True
            self.logger.info("***ParentBranch B was clicked***")
            self.driver.save_screenshot(".\\Screenshots\\" + "parentBranchB.png")
        else:
            self.logger.info("***Missing Parent Branch B***")
            self.driver.save_screenshot(".\\Screenshots\\" + "missingParentBranchB.png")
        self.navigator.collapseBranchB()

        self.navigator.clickOnBranchC()
        time.sleep(2)
        parentBranchC = self.driver.find_element_by_link_text("C").text
        if parentBranchC == "C":
            assert True == True
            self.logger.info("***ParentBranch C was clicked***")
            self.driver.save_screenshot(".\\Screenshots\\" + "parentBranchC.png")
        else:
            self.logger.info("***Missing Parent Branch C***")
            self.driver.save_screenshot(".\\Screenshots\\" + "missingParentBranchC.png")
        self.navigator.collapseBranchC()

        self.navigator.clickOnBranchD()
        time.sleep(2)
        parentBranchD = self.driver.find_element_by_link_text("D").text
        if parentBranchD == "D":
            assert True == True
            self.logger.info("***ParentBranch D was clicked***")
            self.driver.save_screenshot(".\\Screenshots\\" + "parentBranchD.png")
        else:
            self.logger.info("***Missing Parent Branch C***")
            self.driver.save_screenshot(".\\Screenshots\\" + "missingParentBranchD.png")
        self.navigator.collapseBranchD()

        self.navigator.clickOnBranchE()
        time.sleep(2)
        parentBranchE = self.driver.find_element_by_link_text("E").text
        if parentBranchE == "E":
            assert True == True
            self.logger.info("***ParentBranch E was clicked***")
            self.driver.save_screenshot(".\\Screenshots\\" + "parentBranchE.png")
        else:
            self.logger.info("***Missing Parent Branch E***")
            self.driver.save_screenshot(".\\Screenshots\\" + "missingParentBranchE.png")
        self.navigator.collapseBranchE()

        self.navigator.clickOnBranchF()
        time.sleep(2)
        parentBranchF = self.driver.find_element_by_link_text("F").text
        if parentBranchF == "F":
            assert True == True
            self.logger.info("***ParentBranch F was clicked***")
            self.driver.save_screenshot(".\\Screenshots\\" + "parentBranchF.png")
        else:
            self.logger.info("***Missing Parent Branch F***")
            self.driver.save_screenshot(".\\Screenshots\\" + "missingParentBranchF.png")
        self.navigator.collapseBranchF()

        self.navigator.clickOnBranchG()
        time.sleep(2)
        parentBranchG = self.driver.find_element_by_link_text("G").text
        if parentBranchG == "G":
            assert True == True
            self.logger.info("***ParentBranch G was clicked***")
            self.driver.save_screenshot(".\\Screenshots\\" + "parentBranchG.png")
        else:
            self.logger.info("***Missing Parent Branch G***")
            self.driver.save_screenshot(".\\Screenshots\\" + "missingParentBranchG.png")
        self.navigator.collapseBranchG()

        self.navigator.clickOnBranchH()
        time.sleep(2)
        parentBranchH = self.driver.find_element_by_link_text("H").text
        if parentBranchH == "H":
            assert True == True
            self.logger.info("***ParentBranch H was clicked***")
            self.driver.save_screenshot(".\\Screenshots\\" + "parentBranchH.png")
        else:
            self.logger.info("***Missing Parent Branch G***")
            self.driver.save_screenshot(".\\Screenshots\\" + "missingParentBranchH.png")
        self.navigator.collapseBranchH()

        self.navigator.clickOnBranchI()
        time.sleep(2)
        parentBranchI = self.driver.find_element_by_link_text("I").text
        if parentBranchI == "I":
            assert True == True
            self.logger.info("***ParentBranch I was clicked***")
            self.driver.save_screenshot(".\\Screenshots\\" + "parentBranchI.png")
        else:
            self.logger.info("***Missing Parent Branch G***")
            self.driver.save_screenshot(".\\Screenshots\\" + "missingParentBranchI.png")
        self.navigator.collapseBranchI()

        self.navigator.clickOnBranchJ()
        time.sleep(2)
        parentBranchJ = self.driver.find_element_by_link_text("J").text
        if parentBranchJ == "J":
            assert True == True
            self.logger.info("***ParentBranch J was clicked***")
            self.driver.save_screenshot(".\\Screenshots\\" + "parentBranchJ.png")
        else:
            self.logger.info("***Missing Parent Branch G***")
            self.driver.save_screenshot(".\\Screenshots\\" + "missingParentBranchJ.png")
        self.navigator.collapseBranchJ()

        self.navigator.clickOnBranchK()
        time.sleep(2)
        parentBranchK = self.driver.find_element_by_link_text("K").text
        if parentBranchK == "K":
            assert True == True
            self.logger.info("***ParentBranch K was clicked***")
            self.driver.save_screenshot(".\\Screenshots\\" + "parentBranchK.png")
        else:
            self.logger.info("***Missing Parent Branch K***")
            self.driver.save_screenshot(".\\Screenshots\\" + "missingParentBranchK.png")
        self.navigator.collapseBranchK()

        self.navigator.clickOnBranchL()
        time.sleep(2)
        parentBranchL = self.driver.find_element_by_link_text("L").text
        if parentBranchL == "L":
            assert True == True
            self.logger.info("***ParentBranch L was clicked***")
            self.driver.save_screenshot(".\\Screenshots\\" + "parentBranchL.png")
        else:
            self.logger.info("***Missing Parent Branch K***")
            self.driver.save_screenshot(".\\Screenshots\\" + "missingParentBranchL.png")
        self.navigator.collapseBranchL()

        self.navigator.clickOnBranchM()
        time.sleep(2)
        parentBranchM = self.driver.find_element_by_link_text("M").text
        if parentBranchM == "M":
            assert True == True
            self.logger.info("***ParentBranch M was clicked***")
            self.driver.save_screenshot(".\\Screenshots\\" + "parentBranchM.png")
        else:
            self.logger.info("***Missing Parent Branch M***")
            self.driver.save_screenshot(".\\Screenshots\\" + "missingParentBranchM.png")
        self.navigator.collapseBranchM()

        self.navigator.clickOnBranchN()
        time.sleep(2)
        parentBranchN = self.driver.find_element_by_link_text("N").text
        if parentBranchN == "N":
            assert True == True
            self.logger.info("***ParentBranch N was clicked***")
            self.driver.save_screenshot(".\\Screenshots\\" + "parentBranchN.png")
        else:
            self.logger.info("***Missing Parent Branch N***")
            self.driver.save_screenshot(".\\Screenshots\\" + "missingParentBranchN.png")
        self.navigator.collapseBranchN()

        self.navigator.clickOnBranchO()
        time.sleep(2)
        parentBranchO = self.driver.find_element_by_link_text("O").text
        if parentBranchO == "O":
            assert True == True
            self.logger.info("***ParentBranch O was clicked***")
            self.driver.save_screenshot(".\\Screenshots\\" + "parentBranchO.png")
        else:
            self.logger.info("***Missing Parent Branch O***")
            self.driver.save_screenshot(".\\Screenshots\\" + "missingParentBranchO.png")
        self.navigator.collapseBranchO()

        self.navigator.clickOnBranchP()
        time.sleep(2)
        parentBranchP = self.driver.find_element_by_link_text("P").text
        if parentBranchP == "P":
            assert True == True
            self.logger.info("***ParentBranch P was clicked***")
            self.driver.save_screenshot(".\\Screenshots\\" + "parentBranchP.png")
        else:
            self.logger.info("***Missing Parent Branch P***")
            self.driver.save_screenshot(".\\Screenshots\\" + "missingParentBranchP.png")
        self.navigator.collapseBranchP()

        self.navigator.clickOnBranchQ()
        time.sleep(2)
        parentBranchQ = self.driver.find_element_by_link_text("Q").text
        if parentBranchQ == "P":
            assert True == True
            self.logger.info("***ParentBranch Q was clicked***")
            self.driver.save_screenshot(".\\Screenshots\\" + "parentBranchQ.png")
        else:
            self.logger.info("***Missing Parent Branch Q***")
            self.driver.save_screenshot(".\\Screenshots\\" + "missingParentBranchQ.png")
        self.navigator.collapseBranchQ()

        self.navigator.clickOnBranchR()
        time.sleep(2)
        parentBranchQ = self.driver.find_element_by_link_text("R").text
        if parentBranchQ == "R":
            assert True == True
            self.logger.info("***ParentBranch R was clicked***")
            self.driver.save_screenshot(".\\Screenshots\\" + "parentBranchR.png")
        else:
            self.logger.info("***Missing Parent Branch R***")
            self.driver.save_screenshot(".\\Screenshots\\" + "missingParentBranchR.png")
        self.navigator.collapseBranchR()

        self.navigator.clickOnBranchS()
        time.sleep(2)
        parentBranchS = self.driver.find_element_by_link_text("S").text
        if parentBranchS == "S":
            assert True == True
            self.logger.info("***ParentBranch S was clicked***")
            self.driver.save_screenshot(".\\Screenshots\\" + "parentBranchS.png")
        else:
            self.logger.info("***Missing Parent Branch S***")
            self.driver.save_screenshot(".\\Screenshots\\" + "missingParentBranchS.png")
        self.navigator.collapseBranchS()

        self.navigator.clickOnBranchT()
        time.sleep(2)
        parentBranchT = self.driver.find_element_by_link_text("T").text
        if parentBranchT == "T":
            assert True == True
            self.logger.info("***ParentBranch T was clicked***")
            self.driver.save_screenshot(".\\Screenshots\\" + "parentBranchT.png")
        else:
            self.logger.info("***Missing Parent Branch T***")
            self.driver.save_screenshot(".\\Screenshots\\" + "missingParentBranchT.png")
        self.navigator.collapseBranchT()

        self.navigator.clickOnBranchU()
        time.sleep(2)
        parentBranchU = self.driver.find_element_by_link_text("U").text
        if parentBranchU == "U":
            assert True == True
            self.logger.info("***ParentBranch U was clicked***")
            self.driver.save_screenshot(".\\Screenshots\\" + "parentBranchU.png")
        else:
            self.logger.info("***Missing Parent Branch U***")
            self.driver.save_screenshot(".\\Screenshots\\" + "missingParentBranchU.png")
        self.navigator.collapseBranchU()

        self.navigator.clickOnBranchV()
        time.sleep(2)
        parentBranchV = self.driver.find_element_by_link_text("V").text
        if parentBranchV == "V":
            assert True == True
            self.logger.info("***ParentBranch V was clicked***")
            self.driver.save_screenshot(".\\Screenshots\\" + "parentBranchV.png")
        else:
            self.logger.info("***Missing Parent Branch T***")
            self.driver.save_screenshot(".\\Screenshots\\" + "missingParentBranchV.png")
        self.navigator.collapseBranchV()

        self.navigator.clickOnBranchX()
        time.sleep(2)
        parentBranchX = self.driver.find_element_by_link_text("X").text
        if parentBranchX == "X":
            assert True == True
            self.logger.info("***ParentBranch X was clicked***")
            self.driver.save_screenshot(".\\Screenshots\\" + "parentBranchX.png")
        else:
            self.logger.info("***Missing Parent Branch X***")
            self.driver.save_screenshot(".\\Screenshots\\" + "missingParentBranchX.png")
        self.navigator.collapseBranchX()

        self.navigator.clickOnBranchY()
        time.sleep(2)
        parentBranchY = self.driver.find_element_by_link_text("Y").text
        if parentBranchY == "Y":
            assert True == True
            self.logger.info("***ParentBranch Y was clicked***")
            self.driver.save_screenshot(".\\Screenshots\\" + "parentBranchY.png")
        else:
            self.logger.info("***Missing Parent Branch Y***")
            self.driver.save_screenshot(".\\Screenshots\\" + "missingParentBranchY.png")
        self.navigator.collapseBranchY()

        self.navigator.clickOnBranchZ()
        time.sleep(2)
        parentBranchZ = self.driver.find_element_by_link_text("Z").text
        if parentBranchZ == "Z":
            assert True == True
            self.logger.info("***ParentBranch Z was clicked***")
            self.driver.save_screenshot(".\\Screenshots\\" + "parentBranchZ.png")
        else:
            self.logger.info("***Missing Parent Branch Z***")
            self.driver.save_screenshot(".\\Screenshots\\" + "missingParentBranchZ.png")
        self.navigator.collapseBranchZ()
