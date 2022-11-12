from telnetlib import EC

import clipboard
import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from ddt import ddt, data, unpack

from pageObjects.LoginPage import LoginPage
from pageObjects.SubjectNavigator import SubjectNavigator
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import string
import pyperclip
import pyautogui

import random


@pytest.mark.usefixtures("setup")

class Test_testCasesSN:
    logger = LogGen.loggen()

    #@pytest.mark.skip(reason="None")
    def test_addtoResearch(self):
        self.logger.info("****TestCase 001 - Verify Add to Research***")
        self.navigator = SubjectNavigator(self.driver)
        self.navigator.clickOnSubjectNavigatormenu()
        self.logger.info("Clicked on Subject Navigator from the navigation menu")
        #self.navigator.clickOnClientListing()
        self.navigator.clickOnBranchA()
        time.sleep(2)
        self.logger.info("Clicked on Branch A")
        time.sleep(1)
        # Clicks on Expand All of the first row
        #self.driver.find_element_by_xpath("(//div[contains(@class,'card__actions')]/a[1])[1]").click()
        # time.sleep(2)
        # # #actionsclick = self.driver.find_element_by_xpath(
        # #     "//body/main[contains(@class,'main')]/section/div[contains(@class,"
        # #     "'container')]/div[contains(@class,'subject-navigator')]/div[contains("
        # #     "@class,'item-list compact__container')]/div[contains(@class,"
        # #     "'dropdown item-list__item')]/div[contains(@class,'dropdown__content "
        # #     "item-list__content card-list branch__content')]/div[1]/div[1]/div["
        # #     "1]/button[1][1]/i[1]"
        actionsclick = self.driver.find_element(By.XPATH, "(//div[@class='card__actions dropdown']//button)[1]")
        self.driver.execute_script("arguments[0].click();", actionsclick)
        researchNotepad = self.driver.find_element(By.XPATH, "(//div[@class='card__actions dropdown']//div//p//a)[1]")
        self.driver.execute_script("arguments[0].click();", researchNotepad)
        time.sleep(2)
        firstOption = self.driver.find_element(By.XPATH,
                                                           "//*[@id='popup-add-to-rn']/div[1]/div[2]/div/ul/li[1]/label/span")
        self.driver.execute_script("arguments[0].click();", firstOption)
        add = self.driver.find_element_by_xpath("//*[@ id = 'btn-popup-add']")
        self.driver.execute_script("arguments[0].click();", add)
        self.logger.info("Added to Research Notepad")
        time.sleep(2)
        # self.driver.find_element(By.XPATH, "(//div[@class='card card--basic  dropdown']//div//p//a)[1]")
        # self.driver.execute_script("arguments[0].click();", actionsclick)
        #
        # comments = self.driver.find_element_by_xpath("//*[@id='bookmark-comments']")
        # comments.send_keys("Adding to Research Notepad")
        # time.sleep(2)
        #
        # time.sleep(2)
        # validationMsg = self.driver.find_element(By.XPATH, "//div[@class='topics-details bookmark-error']//span")
        # time.sleep(2)
        # res = validationMsg.text
        # self.logger.info(validationMsg.text)
        # if len(res) != 0:
        #     self.logger.info("Document is already added to the research notepad")
        #     clickNew = self.driver.find_element(By.XPATH, "//a[@title='Create new research topic']")
        #     self.driver.execute_script("arguments[0].click();", clickNew)
        #     self.driver.find_element(By.XPATH, "//input[@id='topic-name']").send_keys("TestTopic2")
        #     clickSave = self.driver.find_element(By.XPATH, "//button[@id='btn-create-new-research-topic']")
        #     self.driver.execute_script("arguments[0].click();", clickSave)
        # firstOption = self.driver.find_element(By.XPATH,
        #                                            "//*[@id='popup-add-to-rn']/div[1]/div[2]/div/ul/li[1]/label/span")
        # self.driver.execute_script("arguments[0].click();", firstOption)
        # time.sleep(2)
        # clickAdd = self.driver.find_element(By.XPATH, "//button[@id='btn-popup-add']")
        # self.driver.execute_script("arguments[0].click();", clickAdd)
        #
        # self.logger.info("done")
        # time.sleep(2)
        time.sleep(2)

    #@pytest.mark.skip(reason="None")
    def test_copyLocation(self):
        self.logger.info("****TestCase 002 - Copy Location***")
        self.logger.info("*****Login Successful****")
        self.navigator = SubjectNavigator(self.driver)
        self.navigator.clickOnSubjectNavigatormenu()
        time.sleep(2)
        #self.navigator.clickOnClientListing()
        self.navigator.clickOnBranchA()
        time.sleep(2)
        actionsclick = self.driver.find_element(By.XPATH, "(//div[@class='card__actions dropdown']//button)[1]")
        self.driver.execute_script("arguments[0].click();", actionsclick)
        time.sleep(2)
        copyLocation = self.driver.find_element(By.XPATH, "(//div[@class='card__actions dropdown']//div//p//a)[3]")
        self.driver.execute_script("arguments[0].click();", copyLocation)
        self.logger.info("Clicked on Copy Location")
        #self.driver.find_element_by_xpath("//*[contains(@title, 'Copy Location')]").click()
        # time.sleep(2)
        # parent_handle = self.driver.current_window_handle
        # print(parent_handle)
        # test = self.driver.find_element_by_xpath("//input[@title='Search']")
        # time.sleep(2)
        # # all_handles = self.driver.window_handles
        # # print(test.send_keys(Keys.CONTROL + "v"))
        # myurlstring = ""
        # myurlstring = clipboard.paste()
        # time.sleep(2)
        # self.logger.info(myurlstring + "  URL copied")
        # self.driver.execute_script("window.open('" + myurlstring + "');")
        # time.sleep(2)
        # all_handles = self.driver.window_handles
        # print(all_handles)
        # for handle in all_handles:
        #     if handle != parent_handle:
        #         self.driver.switch_to.window(handle)
        #         time.sleep(2)
        #         self.driver.close()
        # self.driver.switch_to.window(parent_handle)
        # time.sleep(1)

    #@pytest.mark.skip(reason="None")
    def test_find(self):
        self.logger.info("****TestCase 003 - Verify Find and Reset***")
        self.navigator = SubjectNavigator(self.driver)
        self.navigator.clickOnSubjectNavigatormenu()
        # self.navigator.clickOnClientListing()
        self.logger.info("Subject Navigator menu is available")
        self.driver.find_element_by_xpath("//*[@id='search-subject']").click()
        text = self.driver.find_element_by_xpath("//*[@id='search-subject']")
        # entering Abuse of Right as search value
        text.send_keys("abuse of rights")
        self.navigator.findText()
        time.sleep(3)
        textval = self.driver.find_element_by_css_selector("#search-popover > div > p > strong > span").get_attribute(
            'textContent')
        print(textval)  # This will print the no of matches found
        self.logger.info(textval + " Matches Found")
        time.sleep(2)
        text.clear()
        text.send_keys("ahj")
        self.navigator.findText()
        time.sleep(2)
        matchesnotfound = self.driver.find_element_by_css_selector(
            "div[class='grid search-subject-no-results'] strong").get_attribute(
            'textContent')
        print(matchesnotfound)  # This will print matches not found
        self.logger.info(textval + "  Matches Found")
        time.sleep(2)
        closepop = self.driver.find_element_by_xpath("//*[@id='search-popover']/a")
        self.driver.execute_script("arguments[0].click();", closepop)
        self.logger.info("****Search Completed***")
        # Validate reset button
        self.driver.find_element_by_xpath("//*[@id='search-reset']").click()

    #@pytest.mark.skip(reason="None")
    def test_searchOptions(self):
        self.logger.info("****TestCase 005 - Verify Search By All Words***")
        self.navigator = SubjectNavigator(self.driver)
        self.navigator.clickOnSubjectNavigatormenu()
        # self.navigator.clickOnClientListing()
        # this expands the advanced find
        self.driver.implicitly_wait(2)
        self.driver.find_element_by_xpath("//*[@id='btn-search-options-control']/i").click()
        self.logger.info("Clicked on the expand search")
        allwords = self.driver.find_element_by_id("rb-all-words")
        self.driver.execute_script("arguments[0].click();", allwords)
        self.driver.implicitly_wait(2)
        self.driver.find_element_by_xpath("//*[@id='btn-search-options-control']/i").click()
        text = self.driver.find_element_by_xpath("//*[@id='search-subject']")
        # entering Abuse of right'  award as search value
        text.send_keys(" 'Abuse of right'  award")
        self.navigator.findText()
        time.sleep(2)
        textval = self.driver.find_element_by_xpath("//span[@class='no-of-search-subject']").get_attribute(
            'textContent')
        print(textval)  # This will print the no of matches found
        self.logger.info("Search Entry - 'Abuse of Right' ")
        self.logger.info(textval + " No of Matches found")
        self.driver.implicitly_wait(2)
        text.clear()
        text.send_keys(" 'Clean hands' doctrine")
        self.navigator.findText()
        self.driver.implicitly_wait(2)
        textval1 = self.driver.find_element_by_xpath("//span[@class='no-of-search-subject']").get_attribute(
            'textContent')
        print(textval1)  # This will print the no of matches found
        self.logger.info("Search Entry - 'Clean hands' doctrine ")
        self.logger.info(textval1 + " Matches Found")
        text.clear()
        text.send_keys(" '+'Clean hands' + doctrine - claimant")
        self.navigator.findText()
        time.sleep(2)
        textval2 = self.driver.find_element_by_xpath("//span[@class='no-of-search-subject']").get_attribute(
            'textContent')
        print(textval2)  # This will print the no of matches found
        self.logger.info("Search Entry - '+'Clean hands' + doctrine - claimant ")
        self.logger.info(textval2 + " Matches Found")

    #@pytest.mark.skip(reason="Takes longer to retrieve records")
    def test_searchByAnyWords(self):
        self.logger.info("****TestCase 006 - Verify Search By Any Words***")
        self.navigator = SubjectNavigator(self.driver)
        self.navigator.clickOnSubjectNavigatormenu()
        # self.navigator.clickOnClientListing()
        # this expands the advanced find
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@id='btn-search-options-control']/i").click()
        self.logger.info("Clicked on the expand search")
        anywords = self.driver.find_element_by_xpath("//input[@id='rb-any-words']")
        self.driver.execute_script("arguments[0].click();", anywords)
        time.sleep(6)
        self.driver.find_element_by_xpath("//*[@id='btn-search-options-control']/i").click()
        text = self.driver.find_element_by_xpath("//*[@id='search-subject']")
        # entering 'Abuse of right'  award  search value
        text.send_keys("test")
        # text.send_keys(" 'Abuse of right'  award")
        self.navigator.findText()
        time.sleep(2)
        textval = self.driver.find_element_by_xpath("//span[@class='no-of-search-subject']").get_attribute(
            'textContent')
        print(textval)  # This will print the no of matches found
        self.logger.info("Search Entry - 'Canada' ")
        self.logger.info(textval + " No of Matches found")
        # time.sleep(2)
        # text.clear()
        # text.send_keys("Clean hands")
        # # text.send_keys(" 'Clean hands' doctrine")
        # self.navigator.findText()
        # time.sleep(2)
        # textval1 = self.driver.find_element_by_xpath("//span[@class='no-of-search-subject']").get_attribute(
        #     'textContent')
        # print(textval1)  # This will print the no of matches found
        # self.logger.info("Search Entry - 'Clean hands' doctrine ")
        # self.logger.info(textval1 + " Matches Found")
        # text.clear()
        # text.send_keys(" '+'Clean hands' + doctrine - claimant")
        # self.navigator.findText()
        # time.sleep(3)
        # textval2 = self.driver.find_element_by_xpath("//span[@class='no-of-search-subject']").get_attribute(
        #     'textContent')
        # print(textval2)  # This will print the no of matches found
        # self.logger.info("Search Entry - '+'Clean hands' + doctrine - claimant ")
        # self.logger.info(textval2 + " Matches Found")

    #@pytest.mark.skip(reason="None")
    def test_searchByBoolean(self):
        self.logger.info("****TestCase 007 - Verify Search By Boolean***")
        self.navigator = SubjectNavigator(self.driver)
        self.navigator.clickOnSubjectNavigatormenu()
        # self.navigator.clickOnClientListing()
        self.logger.info("Subject Navigator menu is available")
        self.driver.find_element_by_xpath("//*[@id='search-subject']").click()
        text = self.driver.find_element_by_xpath("//*[@id='search-subject']")
        # entering Canada And Country as search value
        text.send_keys("Canada And Country")
        self.navigator.findText()
        time.sleep(2)
        textval = self.driver.find_element_by_xpath(
            "//div[@class='form__set form__set--inline']//strong[1]").get_attribute(
            'textContent')
        print(textval)  # This will print the no of matches found
        self.logger.info(textval)
        time.sleep(2)
        text.clear()
        text.send_keys("(Abuse or Rights) AND (abuse w/5 rights)")
        self.navigator.findText()
        time.sleep(2)
        textval2 = self.driver.find_element_by_xpath(
            "//div[@class='form__set form__set--inline']//strong[1]").get_attribute(
            'textContent')
        print(textval2)  # This will print the no of matches found
        self.logger.info(textval2)
        text.clear()
        # fuzzysearch
        text.send_keys("countr%ies")
        self.navigator.findText()
        time.sleep(2)
        textval4 = self.driver.find_element_by_xpath(
            "//div[@class='form__set form__set--inline']//strong[1]").get_attribute(
            'textContent')
        print(textval4)  # This will print the no of matches found
        self.logger.info(textval4)
        closepop = self.driver.find_element_by_xpath("//*[@id='search-popover']/a")
        self.driver.execute_script("arguments[0].click();", closepop)
        self.logger.info("****Search Completed***")
        # Validate reset button
        self.driver.find_element_by_xpath("//*[@id='search-reset']").click()

    #@pytest.mark.skip(reason="None")
    def test_searchByAllWords(self):
        self.logger.info("****TestCase 008 - Search By All Words***")
        self.navigator = SubjectNavigator(self.driver)
        self.navigator.clickOnSubjectNavigatormenu()
        # self.navigator.clickOnClientListing()
        # this expands the advanced find
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@id='btn-search-options-control']/i").click()
        self.logger.info("Clicked on the expand search")
        allwords = self.driver.find_element_by_id("rb-all-words")
        self.driver.execute_script("arguments[0].click();", allwords)
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@id='btn-search-options-control']/i").click()
        text = self.driver.find_element_by_xpath("//*[@id='search-subject']")
        # entering Abuse of right'  award as search value
        text.send_keys(" 'Abuse of right'  award")
        self.navigator.findText()
        time.sleep(2)
        textval = self.driver.find_element_by_xpath("//span[@class='no-of-search-subject']").get_attribute(
            'textContent')
        print(textval)  # This will print the no of matches found
        self.logger.info("Search Entry - 'Abuse of Right' ")
        self.logger.info(textval + " No of Matches found")
        self.driver.implicitly_wait(2)
        text.clear()
        text.send_keys(" 'Clean hands' doctrine")
        self.navigator.findText()
        self.driver.implicitly_wait(2)
        textval1 = self.driver.find_element_by_xpath("//span[@class='no-of-search-subject']").get_attribute(
            'textContent')
        print(textval1)  # This will print the no of matches found
        self.logger.info("Search Entry - 'Clean hands' doctrine ")
        self.logger.info(textval1 + " Matches Found")
        text.clear()
        text.send_keys(" '+'Clean hands' + doctrine - claimant")
        self.navigator.findText()
        time.sleep(2)
        textval2 = self.driver.find_element_by_xpath("//span[@class='no-of-search-subject']").get_attribute(
            'textContent')
        print(textval2)  # This will print the no of matches found
        self.logger.info("Search Entry - '+'Clean hands' + doctrine - claimant ")
        self.logger.info(textval2 + " Matches Found")

    #@pytest.mark.skip(reason="None")
    def test_switchlayout(self, setup):
        self.logger.info("****TestCase 009 - Verify Card/Compact View***")
        self.navigator = SubjectNavigator(self.driver)
        self.navigator.clickOnSubjectNavigatormenu()
        #self.navigator.clickOnClientListing()
        self.navigator.clickOnBranchA()  # Clicks on Branch A
        # a = self.driver.find_element_by_xpath("//span[(text()= 'AA')]")
        # self.driver.execute_script("arguments[0].click();", a)
        # cardHeader = self.driver.find_element(By.XPATH, "//a[@data-branchid='27633']//i[@class='far fa-angle-right dropdown__icon--rotate']")
        # self.driver.execute_script("arguments[0].click();", cardHeader)
        # card = self.driver.find_element_by_link_text("Dispute Document").text
        # if card == "Dispute Document":
        #     assert True == True
        #     self.logger.info("***Dispute Document is displayed for card***")
        # cardview = self.driver.find_element_by_link_text("Dispute Details").text
        # if cardview == "Dispute Details":
        #     assert True == True
        #     self.logger.info("***Dispute Details is displayed for card***")
        # compact view is clicked
        #self.driver.find_element_by_xpath("//*[@id='page-content']/div/div/div[4]/div[2]/div/button[2]").click()
        self.logger.info("****Compact View is clicked****")
        time.sleep(2)

    #@pytest.mark.skip(reason="None")
    def test_followTopic(self):
        self.logger.info("****TestCase 004 - Verify Follow Topic***")
        self.navigator = SubjectNavigator(self.driver)
        self.navigator.clickOnSubjectNavigatormenu()
        # self.navigator.clickOnClientListing()
        self.navigator.clickOnBranchA()
        time.sleep(2)
        actions = self.driver.find_element(By.XPATH, "(//div[@class='card__actions dropdown']//button)[1]")
        self.driver.execute_script("arguments[0].click();", actions)
        time.sleep(2)
        followtopic = self.driver.find_element_by_xpath("//*[contains(@title, 'Follow Topic')]")
        self.driver.execute_script("arguments[0].click();", followtopic)
        time.sleep(2)
        message = self.driver.find_element(By.XPATH,
                                           "//*[contains(text(), 'You have followed this topic.')]").get_attribute(
            'textContent')
        print(message)
        self.logger.info(message + " is displayed when Followed Topic option is clicked")
        self.driver.find_element(By.XPATH, "//*[contains(@title,'Actions')]").click()
        time.sleep(2)
        self.logger.info("Clicked on Follow Topic")
        # self.driver.find_element(By.XPATH, "//*[contains(@title,'Actions')]").click()
        # time.sleep(2)
        # followtopicstate = self.driver.find_element_by_xpath("//*[contains(@title, 'Follow Topic')]")
        # elementdisabled = followtopicstate.get_property('disabled')
        # print(elementdisabled)
        # self.logger.info(elementdisabled)
        # self.logger.info("follow topic is disabled")
        # time.sleep(2)

    #@pytest.mark.skip(reason="None")
    def test_useAsFullTextSearch(self, setup):
        self.logger.info("****TestCase 010 - Verify Use As Full Text Search***")
        self.navigator = SubjectNavigator(self.driver)
        self.navigator.clickOnSubjectNavigatormenu()
        #self.navigator.clickOnClientListing()
        self.navigator.clickOnBranchA()
        time.sleep(2)
        parent_handle = self.driver.current_window_handle
        print(parent_handle)
        actincClick = self.driver.find_element(By.XPATH, "//*[contains(@title,'Actions')]")
        self.driver.execute_script("arguments[0].click();", actincClick)
        time.sleep(2)

        fullText = self.driver.find_element(By.XPATH, "(//div[@class='card__actions dropdown']//div//p//a)[2]")
        self.driver.execute_script("arguments[0].click();", fullText)
        all_handles = self.driver.window_handles
        print(all_handles)
        for handle in all_handles:
            if handle != parent_handle:
                self.driver.switch_to.window(handle)
                time.sleep(2)
                element = self.driver.find_element(By.XPATH, "//span[@title='Search Subject']")
                self.driver.execute_script("arguments[0].scrollIntoView();", element)
                self.driver.implicitly_wait(2)
                getelementtext = self.driver.find_element(By.XPATH, "//span[@title='Search Subject']//ul").text
                print(getelementtext)
                self.logger.info(getelementtext + "  Full Text is present ")
                time.sleep(2)
                self.driver.close()
        self.driver.switch_to.window(parent_handle)
        time.sleep(2)

    #@pytest.mark.skip(reason="None")
    def test_documentComparison(self):
        self.logger.info("****TestCase 011 - Verify Document Comparison***")
        self.navigator = SubjectNavigator(self.driver)
        self.navigator.clickOnSubjectNavigatormenu()
        #self.navigator.clickOnClientListing()
        self.navigator.clickOnBranchA()
        time.sleep(2)
        # parent_handle = self.driver.current_window_handle
        # print(parent_handle)
        # branch1 = self.driver.find_element(By.XPATH, "(//div[@class='card__header']//a)[1]")
        # self.driver.execute_script("arguments[0].click();", branch1)
        # crossRef = self.driver.find_element(By.XPATH, "(//div[@class='card__content dropdown__content branch__content']//div//ul//li)[1]//a")
        # self.driver.execute_script("arguments[0].click();", crossRef)
        self.logger.info("Clicked on Cross Reference")
        # linkRef = self.driver.find_element(By.XPATH, "(//div[@class='tabs__content-container']//div//div//span//a)[1])")
        # self.driver.execute_script("arguments[0].click();", linkRef)
        # linkReference = self.driver.find_element(By.XPATH, "(//span[@class='document__citation tooltip-elem']//a)[1]")
        # self.driver.execute_script("arguments[0].click();", linkReference)
        # # cc = self.driver.find_element(By.XPATH, "(//div[contains(@class,'card__header')]/a[1])")
        # self.driver.execute_script("arguments[0].click();", cc)
        # time.sleep(2)
        # dd = self.driver.find_element(By.XPATH, "//div[@class='card-list']//div//div//a[@data-branchid='27633']")
        # self.driver.execute_script("arguments[0].click();", dd)
        # ee = self.driver.find_element(By.XPATH, "//div[@class='document']//div[@style='z-index: 46;']//button")
        # self.driver.execute_script("arguments[0].click();", ee)
        # # Click on Document Comparison
        # time.sleep(2)
        # ff = self.driver.find_element(By.XPATH, "//div[@style='z-index: 45;']//div//p//a[2]")
        # self.driver.execute_script("arguments[0].click();", ff)
        # time.sleep(2)
        # self.driver.find_element(By.XPATH, "//*[@id='popup-add-to-dc']/div[1]/div[2]/ul/li[1]/label/span").click()
        # self.driver.find_element(By.XPATH, "//*[@id='btn-comparison-add']").click()
        # comparisonmessage = self.driver.find_element(By.XPATH,
        #                                              "//*[contains(text(), 'Added to your document comparison group.')]").get_attribute(
        #     'textContent')
        # print(comparisonmessage)
        # self.logger.info(comparisonmessage + " is displayed")
        # time.sleep(2)

    #@pytest.mark.skip(reason="None")
    def test_fullCaseAnalaysis(self):
        self.logger.info("****TestCase 012 - Verify Full Case Analysis***")
        self.navigator = SubjectNavigator(self.driver)
        self.navigator.clickOnSubjectNavigatormenu()
        # self.navigator.clickOnClientListing()
        self.navigator.clickOnBranchB()
        time.sleep(2)
        # parent_handle = self.driver.current_window_handle
        # print(parent_handle)
        self.logger.info("Full Case Analaysis not displayed")


    #@pytest.mark.skip(reason="None")
    def test_copyCitation(self):
        self.logger.info("****TestCase 013 - Verify Copy Citation***")
        self.navigator = SubjectNavigator(self.driver)
        self.navigator.clickOnSubjectNavigatormenu()
        #self.navigator.clickOnClientListing()
        self.navigator.clickOnBranchB()
        # parent_handle = self.driver.current_window_handle
        # print(parent_handle)
        time.sleep(2)
        self.logger.info("Copy Citation")

    #pytest.mark.skip(reason="None")
    def test_disputeDetails(self):
        self.logger.info("****TestCase 014 - Verify Dispute Details***")
        self.navigator = SubjectNavigator(self.driver)
        self.navigator.clickOnSubjectNavigatormenu()
        #self.navigator.clickOnClientListing()
        self.navigator.clickOnBranchB()
        time.sleep(2)
        parent_handle = self.driver.current_window_handle
        print(parent_handle)
        gg = self.driver.find_element(By.XPATH, "(//div[@class='item-list compact__container']//div[@class='dropdown item-list__item'][2]//div//div//div//a//i)[2]")
        self.driver.execute_script("arguments[0].click();", gg)
        time.sleep(2)
        expandLink1 = self.driver.find_element(By.XPATH, "(//div[@class='dropdown item-list__item'][2]//div[2]//div[2]//div//div//a)[1]")
        self.driver.execute_script("arguments[0].click();", expandLink1)
        time.sleep(2)
        self.logger.info("Clicked on Disputes")
        # time.sleep(2)
        # toggle = self.driver.find_element(By.XPATH, "//div[@class='card-list']//div//div//a[@data-branchid='27633']")
        # self.driver.execute_script("arguments[0].click();", toggle)
        # time.sleep(2)
        # dispute = self.driver.find_element_by_css_selector(".tabs__list-item.tabs__tab-control.dispute-details-content.active")
        # self.driver.execute_script("arguments[0].click();", dispute)
        # actions = ActionChains(self.driver)
        # # # cheated here
        # pyautogui.press("tab", 4)
        # pyautogui.press('enter')
        # element = self.driver.find_element(By.XPATH, "//a[@class='tabs__list-item tabs__tab-control dispute-details-content active']")
        # element.send_keys(Keys.ENTER)
        # disputeDetails = self.driver.find_element(By.XPATH, "//a[normalize-space()='All Dispute Details']")
        # self.driver.execute_script("arguments[0].click();", disputeDetails)
        # parent_handle = self.driver.current_window_handle
        # print(parent_handle)
        # all_handles = self.driver.window_handles
        # print(all_handles)
        # for handle in all_handles:
        #       if handle != parent_handle:
        #          self.driver.switch_to.window(handle)
        #          time.sleep(2)
        #          self.driver.close()
        # self.driver.switch_to.window(parent_handle)
        # self.driver.quit()
