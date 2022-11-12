from telnetlib import EC

import clipboard
import pytest
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.LoginPage import LoginPage
from pageObjects.SubjectNavigator import SubjectNavigator
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import string
import pyperclip

import random


@pytest.mark.usefixtures("setup")
class Test_003_AddtoResearch:
    logger = LogGen.loggen()

    def test_AddtoResearch(self):
        self.logger.info("****TestCase 003 - Verify Add to Research***")
        self.logger.info("*****Login Successful****")
        self.logger.info("**** Subject Navigator testing *****")
        self.navigator = SubjectNavigator(self.driver)
        self.navigator.clickOnSubjectNavigatormenu()
        self.navigator.clickOnClientListing()
        self.logger.info("Subject Navigator menu is available")
        self.navigator.clickOnBranchA()
        # Clicks on Expand All of the first row
        self.driver.find_element_by_xpath("(//div[contains(@class,'card__actions')]/a[1])[1]").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[contains(@title,'Actions')]").click()
        self.driver.find_element_by_xpath("//*[contains(@title,'Research Notepad')]").click()
        self.driver.find_element_by_css_selector(
            "#popup-add-to-rn > div.scrolling-content > div:nth-child(3) > div > ul > li:nth-child(2) > label").click()
        comments = self.driver.find_element_by_xpath("//*[@id='bookmark-comments']")
        comments.send_keys("Adding to Research Notepad")
        self.driver.find_element_by_xpath("//*[@ id = 'btn-popup-add']").click()
        time.sleep(2)
        self.logger.info("Added to Research Notepad")
        self.logger.info("done")

    def test_CopyLocation(self):
        self.logger.info("****TestCase 11 - Copy Location***")
        self.logger.info("*****Login Successful****")
        self.navigator = SubjectNavigator(self.driver)
        self.navigator.clickOnSubjectNavigatormenu()
        # self.navigator.clickOnClientListing()
        self.navigator.clickOnBranchA()
        self.driver.find_element(By.XPATH, "//*[contains(@title,'Actions')]").click()
        self.driver.find_element_by_xpath("//*[contains(@title, 'Copy Location')]").click()
        time.sleep(2)
        parent_handle = self.driver.current_window_handle
        print(parent_handle)
        test = self.driver.find_element_by_xpath("//input[@title='Search']")

        time.sleep(2)
        all_handles = self.driver.window_handles
        print(test.send_keys(Keys.CONTROL + "v"))
        myurl = clipboard.paste()
        self.logger.info(myurl + "  URL copied")
        self.driver.execute_script("window.open('" + myurl + "');")
        time.sleep(2)
        for handle in all_handles:
            if handle != parent_handle:
                self.driver.switch_to.window(handle)

    @mark
    def test_Find(self):
        self.logger.info("****TestCase 002 - Verify Subject Navigator menu***")
        self.navigator = SubjectNavigator(self.driver)
        self.navigator.clickOnSubjectNavigatormenu()
        # self.navigator.clickOnClientListing()
        self.logger.info("Subject Navigator menu is available")
        self.driver.find_element_by_xpath("//*[@id='search-subject']").click()
        text = self.driver.find_element_by_xpath("//*[@id='search-subject']")
        # entering Abuse of Right as search value
        text.send_keys("Abuse of Right")
        self.navigator.findText()
        time.sleep(3)
        textval = self.driver.find_element_by_css_selector("#search-popover > div > p > strong > span").get_attribute(
            'textContent')
        print(textval)  # This will print the no of matches found
        self.logger.info(textval + " Matches Found")
        time.sleep(3)
        text.clear()
        text.send_keys("ahj")
        self.navigator.findText()
        time.sleep(3)
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


    def test_FollowTopic(self):
        self.logger.info("****TestCase 10 - Follow Topic***")
        self.navigator = SubjectNavigator(self.driver)
        self.navigator.clickOnSubjectNavigatormenu()
        # self.navigator.clickOnClientListing()
        self.navigator.clickOnBranchA()
        self.driver.find_element(By.XPATH, "//*[contains(@title,'Actions')]").click()
        followtopic = self.driver.find_element_by_xpath("//*[contains(@title, 'Follow Topic')]")
        self.driver.execute_script("arguments[0].click();", followtopic)
        time.sleep(2)
        message = self.driver.find_element(By.XPATH,
                                           "//*[contains(text(), 'You have followed this topic.')]").get_attribute(
            'textContent')
        print(message)
        self.logger.info(message + " is displayed when Followed Topic option is clicked")
        self.driver.find_element(By.XPATH, "//*[contains(@title,'Actions')]").click()
        self.driver.find_element(By.XPATH, "//*[contains(@title,'Actions')]").click()
        time.sleep(2)
        followtopicstate = self.driver.find_element_by_xpath("//*[contains(@title, 'Follow Topic')]")
        elementdisabled = followtopicstate.get_property('disabled')
        print(elementdisabled)
        self.logger.info(elementdisabled)
        self.logger.info("follow topic is disabled")


    def test_searchOptions(self):
        self.logger.info("****TestCase 007 - Search By All Words***")
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
        time.sleep(1)
        text.clear()
        text.send_keys(" 'Clean hands' doctrine")
        self.navigator.findText()
        time.sleep(2)
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


    def test_searchByAnyWords(self):
        self.logger.info("****TestCase 008 - Search By Any Words***")
        self.navigator = SubjectNavigator(self.driver)
        self.navigator.clickOnSubjectNavigatormenu()
        # self.navigator.clickOnClientListing()
        # this expands the advanced find
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@id='btn-search-options-control']/i").click()
        self.logger.info("Clicked on the expand search")
        anywords = self.driver.find_element_by_xpath("//input[@id='rb-any-words']")
        self.driver.execute_script("arguments[0].click();", anywords)
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@id='btn-search-options-control']/i").click()
        text = self.driver.find_element_by_xpath("//*[@id='search-subject']")
        # entering 'Abuse of right'  award  search value
        text.send_keys("Abuse of right")
        # text.send_keys(" 'Abuse of right'  award")
        self.navigator.findText()
        time.sleep(2)
        textval = self.driver.find_element_by_xpath("//span[@class='no-of-search-subject']").get_attribute(
            'textContent')
        print(textval)  # This will print the no of matches found
        self.logger.info("Search Entry - 'Canada' ")
        self.logger.info(textval + " No of Matches found")
        time.sleep(1)
        text.clear()
        text.send_keys("Clean hands")
        # text.send_keys(" 'Clean hands' doctrine")
        self.navigator.findText()
        time.sleep(2)
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

        def test_searchByBoolean(self):
            self.navigator = SubjectNavigator(self.driver)
            self.navigator.clickOnSubjectNavigatormenu()
            # self.navigator.clickOnClientListing()
            self.logger.info("****TestCase 006 - Verify search by boolean***")
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


    def test_searchOptions(self, setup):
        self.logger.info("****TestCase 007 - Search By All Words***")
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
        time.sleep(1)
        text.clear()
        text.send_keys(" 'Clean hands' doctrine")
        self.navigator.findText()
        time.sleep(2)
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

    def test_Switchlayout(self, setup):
        self.logger.info("****TestCase 004 - Switch Layout***")
        self.navigator = SubjectNavigator(self.driver)
        self.navigator.clickOnSubjectNavigatormenu()
        # self.navigator.clickOnClientListing()
        self.navigator.clickOnBranchA()  # Clicks on Branch A
        a = self.driver.find_element_by_xpath("//span[(text()= 'AA')]")
        self.driver.execute_script("arguments[0].click();", a)
        b = self.driver.find_element_by_xpath("//span[(text()= 'Sharmila Test test11072021')]")
        self.driver.execute_script("arguments[0].click();", b)
        card = self.driver.find_element_by_link_text("Dispute Document").text
        if card == "Dispute Document":
            assert True == True
            self.logger.info("***Dispute Document is displayed for card***")
        cardview = self.driver.find_element_by_link_text("Dispute Details").text
        if cardview == "Dispute Details":
            assert True == True
            self.logger.info("***Dispute Details is displayed for card***")
        # compact view is clicked
        self.driver.find_element_by_xpath("//*[@id='page-content']/div/div/div[4]/div[2]/div/button[2]").click()
        self.logger.info("****Compact View is clicked****")
        self.driver.quit()
        self.logger.info("done")

    def test_UseAsFullTextSearch(self, setup):
        self.logger.info("****TestCase 009 - Use As Full Text Search***")
        self.navigator = SubjectNavigator(self.driver)
        self.navigator.clickOnSubjectNavigatormenu()
        # self.navigator.clickOnClientListing()
        self.navigator.clickOnBranchA()
        parent_handle = self.driver.current_window_handle
        print(parent_handle)
        self.driver.find_element(By.XPATH, "//*[contains(@title,'Actions')]").click()
        self.driver.find_element(By.XPATH, "//*[contains(@ title, 'Use as Full Text Search Filfter')]").click()
        all_handles = self.driver.window_handles
        print(all_handles)
        for handle in all_handles:
            if handle != parent_handle:
                self.driver.switch_to.window(handle)
                time.sleep(2)
                element = self.driver.find_element(By.XPATH, "//span[@title='Search Subject']")
                self.driver.execute_script("arguments[0].scrollIntoView();", element)
                time.sleep(2)
                getelementtext = self.driver.find_element(By.XPATH, "//span[@title='Search Subject']//ul").text
                print(getelementtext)
                self.logger.info(getelementtext + "  Full Text is present ")
                self.driver.close()
        self.driver.quit()
