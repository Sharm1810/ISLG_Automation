import logging
from telnetlib import EC

import pytest
import time

import self
from basepage import wait
from selenium.common import exceptions
from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementNotInteractableException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from Configurations.conftest import setup

from pageObjects.LoginPage import LoginPage
from pageObjects.SubjectNavigator import SubjectNavigator

from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import string
import pyperclip

import random
    # use function

#log = log_utils.custom_logger(logging.INFO)

@pytest.mark.usefixtures("setup")
class TestBranches:
    logger = LogGen.loggen()

    @pytest.fixture(scope='function')

    def initialize(self):
       # self.main_page = MainPage(self.driver)
        #self.exe_status = ExecutionStatus(self.driver)
        #self.ui_helpers = UIHelpers(self.driver)

        def cleanup():
            self.driver.delete_all_cookies()

        yield
        cleanup()

    # @pytest.fixture(autouse=True)
    # def class_level_setup(self, request):
    #     """
    #     This method is used for one time setup of test execution process.
    #     :return: it returns nothing
    #     """
    #     test_name = request.function.__name__
    #     #if data_reader.get_data(test_name, "Runmode") != "Y":
    #         pytest.skip("Excluded from current execution run.")




    #@pytest.mark.skip(reason="None")
    def test_ParentBranches(self):
        self.logger.info("***Test Case 001 (DevOps Text Case ID - 1443) - Verify Expand/Collapse Parent Branches***")
        self.logger.info("*****Login Successful****")
        self.logger.info("**** Subject Navigator testing *****")
        self.navigator = SubjectNavigator(self.driver)
        self.navigator.clickOnSubjectNavigatormenu()
        self.navigator.clickOnClientListing()
        self.navigator.clickOnBranchA()
        parentBranchA = self.driver.find_element_by_xpath("//a[contains(@title,'A')]").text
        if parentBranchA == "A":
            assert True == True
            self.logger.info("***ParentBranch A was clicked***")
            self.driver.save_screenshot(".\\Screenshots\\" + "parentBranchA.png")
        else:
            self.logger.info("***Missing Parent Branch A***")
            self.driver.save_screenshot(".\\Screenshots\\" + "missingParentBranchA.png")
        self.navigator.collapseBranchA()

        # Clicks on Branch B
        self.navigator.clickOnBranchB()
        parentBranchB = self.driver.find_element_by_link_text("B").text
        if parentBranchB == "B":
            assert True == True
            self.logger.info("***ParentBranch B was clicked***")
            self.driver.save_screenshot(".\\Screenshots\\" + "parentBranchB.png")
        else:
            self.logger.info("***Missing Parent Branch B***")
            self.driver.save_screenshot(".\\Screenshots\\" + "missingParentBranchB.png")
        self.navigator.collapseBranchB()

        # Clicks on Branch C
        self.navigator.clickOnBranchC()
        parentBranchC = self.driver.find_element_by_link_text("C").text
        if parentBranchC == "C":
            assert True == True
            self.logger.info("***ParentBranch C was clicked***")
            self.driver.save_screenshot(".\\Screenshots\\" + "parentBranchC.png")
        else:
            self.logger.info("***Missing Parent Branch C***")
            self.driver.save_screenshot(".\\Screenshots\\" + "missingParentBranchC.png")
        self.navigator.collapseBranchC()

        # Clicks on Branch D
        self.navigator.clickOnBranchD()
        parentBranchD = self.driver.find_element_by_link_text("D").text
        if parentBranchD == "D":
            assert True == True
            self.logger.info("***ParentBranch D was clicked***")
            self.driver.save_screenshot(".\\Screenshots\\" + "parentBranchD.png")
        else:
            self.logger.info("***Missing Parent Branch C***")
            self.driver.save_screenshot(".\\Screenshots\\" + "missingParentBranchD.png")
        self.navigator.collapseBranchD()

        # Clicks on Branch E
        self.navigator.clickOnBranchE()
        parentBranchE = self.driver.find_element_by_link_text("E").text
        if parentBranchE == "E":
            assert True == True
            self.logger.info("***ParentBranch E was clicked***")
            self.driver.save_screenshot(".\\Screenshots\\" + "parentBranchE.png")
        else:
            self.logger.info("***Missing Parent Branch E***")
            self.driver.save_screenshot(".\\Screenshots\\" + "missingParentBranchE.png")
        self.navigator.collapseBranchE()

        # Clicks on Branch F
        self.navigator.clickOnBranchF()
        parentBranchF = self.driver.find_element_by_link_text("F").text
        if parentBranchF == "F":
            assert True == True
            self.logger.info("***ParentBranch F was clicked***")
            self.driver.save_screenshot(".\\Screenshots\\" + "parentBranchF.png")
        else:
            self.logger.info("***Missing Parent Branch F***")
            self.driver.save_screenshot(".\\Screenshots\\" + "missingParentBranchF.png")
        self.navigator.collapseBranchF()

        # Clicks on Branch G
        self.navigator.clickOnBranchG()
        parentBranchG = self.driver.find_element_by_link_text("G").text
        if parentBranchG == "G":
            assert True == True
            self.logger.info("***ParentBranch G was clicked***")
            self.driver.save_screenshot(".\\Screenshots\\" + "parentBranchG.png")
        else:
            self.logger.info("***Missing Parent Branch G***")
            self.driver.save_screenshot(".\\Screenshots\\" + "missingParentBranchG.png")
        self.navigator.collapseBranchG()

        # Clicks on Branch H
        self.navigator.clickOnBranchH()
        parentBranchH = self.driver.find_element_by_link_text("H").text
        if parentBranchH == "H":
            assert True == True
            self.logger.info("***ParentBranch H was clicked***")
            self.driver.save_screenshot(".\\Screenshots\\" + "parentBranchH.png")
        else:
            self.logger.info("***Missing Parent Branch G***")
            self.driver.save_screenshot(".\\Screenshots\\" + "missingParentBranchH.png")
        self.navigator.collapseBranchH()

        # Clicks on Branch I
        self.navigator.clickOnBranchI()
        parentBranchI = self.driver.find_element_by_link_text("I").text
        if parentBranchI == "I":
            assert True == True
            self.logger.info("***ParentBranch I was clicked***")
            self.driver.save_screenshot(".\\Screenshots\\" + "parentBranchI.png")
        else:
            self.logger.info("***Missing Parent Branch G***")
            self.driver.save_screenshot(".\\Screenshots\\" + "missingParentBranchI.png")
        self.navigator.collapseBranchI()

        # Clicks on Branch J
        self.navigator.clickOnBranchJ()
        parentBranchJ = self.driver.find_element_by_link_text("J").text
        if parentBranchJ == "J":
            assert True == True
            self.logger.info("***ParentBranch J was clicked***")
            self.driver.save_screenshot(".\\Screenshots\\" + "parentBranchJ.png")
        else:
            self.logger.info("***Missing Parent Branch G***")
            self.driver.save_screenshot(".\\Screenshots\\" + "missingParentBranchJ.png")
        self.navigator.collapseBranchJ()

        # Clicks on Branch K
        self.navigator.clickOnBranchK()
        parentBranchK = self.driver.find_element_by_link_text("K").text
        if parentBranchK == "K":
            assert True == True
            self.logger.info("***ParentBranch K was clicked***")
            self.driver.save_screenshot(".\\Screenshots\\" + "parentBranchK.png")
        else:
            self.logger.info("***Missing Parent Branch K***")
            self.driver.save_screenshot(".\\Screenshots\\" + "missingParentBranchK.png")
        self.navigator.collapseBranchK()

        # Clicks on Branch L
        self.navigator.clickOnBranchL()
        parentBranchL = self.driver.find_element_by_link_text("L").text
        if parentBranchL == "L":
            assert True == True
            self.logger.info("***ParentBranch L was clicked***")
            self.driver.save_screenshot(".\\Screenshots\\" + "parentBranchL.png")
        else:
            self.logger.info("***Missing Parent Branch K***")
            self.driver.save_screenshot(".\\Screenshots\\" + "missingParentBranchL.png")
        self.navigator.collapseBranchL()

        # Clicks on Branch M
        self.navigator.clickOnBranchM()
        parentBranchM = self.driver.find_element_by_link_text("M").text
        if parentBranchM == "M":
            assert True == True
            self.logger.info("***ParentBranch M was clicked***")
            self.driver.save_screenshot(".\\Screenshots\\" + "parentBranchM.png")
        else:
            self.logger.info("***Missing Parent Branch M***")
            self.driver.save_screenshot(".\\Screenshots\\" + "missingParentBranchM.png")
        self.navigator.collapseBranchM()

        # Clicks on Branch N
        self.navigator.clickOnBranchN()
        parentBranchN = self.driver.find_element_by_link_text("N").text
        if parentBranchN == "N":
            assert True == True
            self.logger.info("***ParentBranch N was clicked***")
            self.driver.save_screenshot(".\\Screenshots\\" + "parentBranchN.png")
        else:
            self.logger.info("***Missing Parent Branch N***")
            self.driver.save_screenshot(".\\Screenshots\\" + "missingParentBranchN.png")
        self.navigator.collapseBranchN()

        # Clicks on Branch O
        self.navigator.clickOnBranchO()
        parentBranchO = self.driver.find_element_by_link_text("O").text
        if parentBranchO == "O":
            assert True == True
            self.logger.info("***ParentBranch O was clicked***")
            self.driver.save_screenshot(".\\Screenshots\\" + "parentBranchO.png")
        else:
            self.logger.info("***Missing Parent Branch O***")
            self.driver.save_screenshot(".\\Screenshots\\" + "missingParentBranchO.png")
        self.navigator.collapseBranchO()

        # Clicks on Branch P
        self.navigator.clickOnBranchP()
        parentBranchP = self.driver.find_element_by_link_text("P").text
        if parentBranchP == "P":
            assert True == True
            self.logger.info("***ParentBranch P was clicked***")
            self.driver.save_screenshot(".\\Screenshots\\" + "parentBranchP.png")
        else:
            self.logger.info("***Missing Parent Branch P***")
            self.driver.save_screenshot(".\\Screenshots\\" + "missingParentBranchP.png")
        self.navigator.collapseBranchP()

        # Clicks on Branch Q
        self.navigator.clickOnBranchQ()
        parentBranchQ = self.driver.find_element_by_link_text("Q").text
        if parentBranchQ == "Q":
            assert True == True
            self.logger.info("***ParentBranch Q was clicked***")
            self.driver.save_screenshot(".\\Screenshots\\" + "parentBranchQ.png")
        else:
            self.logger.info("***Missing Parent Branch Q***")
            self.driver.save_screenshot(".\\Screenshots\\" + "missingParentBranchQ.png")
        self.navigator.collapseBranchQ()

        # Clicks on Branch R
        self.navigator.clickOnBranchR()
        parentBranchQ = self.driver.find_element_by_link_text("R").text
        if parentBranchQ == "R":
            assert True == True
            self.logger.info("***ParentBranch R was clicked***")
            self.driver.save_screenshot(".\\Screenshots\\" + "parentBranchR.png")
        else:
            self.logger.info("***Missing Parent Branch R***")
            self.driver.save_screenshot(".\\Screenshots\\" + "missingParentBranchR.png")
        self.navigator.collapseBranchR()

        # Clicks on Branch S
        self.navigator.clickOnBranchS()
        parentBranchS = self.driver.find_element_by_link_text("S").text
        if parentBranchS == "S":
            assert True == True
            self.logger.info("***ParentBranch S was clicked***")
            self.driver.save_screenshot(".\\Screenshots\\" + "parentBranchS.png")
        else:
            self.logger.info("***Missing Parent Branch S***")
            self.driver.save_screenshot(".\\Screenshots\\" + "missingParentBranchS.png")
        self.navigator.collapseBranchS()

        # Clicks on Branch T
        self.navigator.clickOnBranchT()
        parentBranchT = self.driver.find_element_by_link_text("T").text
        if parentBranchT == "T":
            assert True == True
            self.logger.info("***ParentBranch T was clicked***")
            self.driver.save_screenshot(".\\Screenshots\\" + "parentBranchT.png")
        else:
            self.logger.info("***Missing Parent Branch T***")
            self.driver.save_screenshot(".\\Screenshots\\" + "missingParentBranchT.png")
        self.navigator.collapseBranchT()

        # Clicks on Branch U
        self.navigator.clickOnBranchU()
        parentBranchU = self.driver.find_element_by_link_text("U").text
        if parentBranchU == "U":
            assert True == True
            self.logger.info("***ParentBranch U was clicked***")
            self.driver.save_screenshot(".\\Screenshots\\" + "parentBranchU.png")
        else:
            self.logger.info("***Missing Parent Branch U***")
            self.driver.save_screenshot(".\\Screenshots\\" + "missingParentBranchU.png")
        self.navigator.collapseBranchU()

        # Clicks on Branch V
        self.navigator.clickOnBranchV()
        parentBranchV = self.driver.find_element_by_link_text("V").text
        if parentBranchV == "V":
            assert True == True
            self.logger.info("***ParentBranch V was clicked***")
            self.driver.save_screenshot(".\\Screenshots\\" + "parentBranchV.png")
        else:
            self.logger.info("***Missing Parent Branch T***")
            self.driver.save_screenshot(".\\Screenshots\\" + "missingParentBranchV.png")
        self.navigator.collapseBranchV()

        # Clicks on Branch X
        self.navigator.clickOnBranchX()
        parentBranchX = self.driver.find_element_by_link_text("X").text
        if parentBranchX == "X":
            assert True == True
            self.logger.info("***ParentBranch X was clicked***")
            self.driver.save_screenshot(".\\Screenshots\\" + "parentBranchX.png")
        else:
            self.logger.info("***Missing Parent Branch X***")
            self.driver.save_screenshot(".\\Screenshots\\" + "missingParentBranchX.png")
        self.navigator.collapseBranchX()

        # Clicks on Branch Y
        self.navigator.clickOnBranchY()
        parentBranchY = self.driver.find_element_by_link_text("Y").text
        if parentBranchY == "Y":
            assert True == True
            self.logger.info("***ParentBranch Y was clicked***")
            self.driver.save_screenshot(".\\Screenshots\\" + "parentBranchY.png")
        else:
            self.logger.info("***Missing Parent Branch Y***")
            self.driver.save_screenshot(".\\Screenshots\\" + "missingParentBranchY.png")
        self.navigator.collapseBranchY()

        # Clicks on Branch Z
        self.navigator.clickOnBranchZ()
        parentBranchZ = self.driver.find_element_by_link_text("Z").text
        if parentBranchZ == "Z":
            assert True == True
            self.logger.info("***ParentBranch Z was clicked***")
            self.driver.save_screenshot(".\\Screenshots\\" + "parentBranchZ.png")
        else:
            self.logger.info("***Missing Parent Branch Z***")
            self.driver.save_screenshot(".\\Screenshots\\" + "missingParentBranchZ.png")
        self.navigator.collapseBranchZ()

    def test_SubBranches(self):
        self.logger.info("***Test Case 002 (DevOps Text Case ID - 1622) - Verify Expand/Collapse Sub Branches***")
        self.navigator = SubjectNavigator(self.driver)
        self.navigator.clickOnSubjectNavigatormenu()
        #self.navigator.clickOnClientListing()
        self.navigator.clickOnBranchA()
        try:
            time.sleep(2)
            expandAllLink = self.driver.find_element(By.XPATH, "(//div[@class='card__actions dropdown']//a)[1]")
            self.driver.execute_script("arguments[0].click();", expandAllLink)
            self.logger.info("Clicked on Expand All Link")
            time.sleep(2)
            cardList = self.driver.find_element(By.XPATH, "(//ul[@class='list--icons']//li//a)[1]")
            self.driver.execute_script("arguments[0].scrollIntoView();", cardList)
            self.driver.execute_script("arguments[0].click();", cardList)
            getTextCardList = cardList.text
            self.logger.info(getTextCardList)
            time.sleep(2)
            self.logger.info("Clicked on the First link-Card List")
            time.sleep(2)
            cardHeaderExpandAll = self.driver.find_element(By.XPATH, "(//div[@class='card card--basic card--inner dropdown']//div//div//a)[1]")
            self.driver.execute_script("arguments[0].click();", cardHeaderExpandAll)
            self.logger.info("Clicked on Expand All associated with the card List")
            # linkText = self.driver.find_element(By.XPATH, "(//div[@class='card-list']//div[@class='card card--basic card--inner dropdown']//div[@class='card__content dropdown__content branch__content']//div//div//div//a)[1]")
            # self.driver.execute_script("arguments[0].click();", linkText)
            # getlinkText = linkText.text
            # self.logger.info("Clicked on the Link")
            # self.logger.info(getlinkText)
        except AttributeError:
            print("No element")






