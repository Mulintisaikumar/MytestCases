from selenium import webdriver
import time
import pytest

from selenium.webdriver.common.by import  By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from PythonSelFramework.PageObjects.Checkoutpage import CheckOutpage
from PythonSelFramework.PageObjects.Homepage import Homepage
from PythonSelFramework.Utility.BaseClass import BaseClass


@pytest.mark.usefixtures("setup")

class TestOne(BaseClass1):

    def test_e2e(self):
        log = self.getLogger()
        homepage = Homepage(self.driver)
        checkOutpage = Homepage.shopitem()
        chekOutPage = CheckOutpage(self.driver)
        log.info("getting all the card tittles")
        #self.find_element_by_css_selector("a[href*='shop']").click()
        #cards = self.driver.find_elements_by_css_selector(".card-tittle a")
        cards = checkoutpage.getcardTitles()
        i = -1
        for card in cards:
            i +=1
            cardText = card.text
            log.info(cardText)
            print(cardText)
            if cardText == "Blackberry":
                chekOutPage.getCardFooter()[i].click()
                                                                 #self. driver.find_element_by_css_selector(".card-footer button")[i].click()

        self. driver.find_element_by_css_selector("a[class*='btn-primary']").click()

        confirmpage = checkOutpage.checkOutItems()
        log.info("Entering country name as ind")
        self. driver.find_element_by_xpath("//button[@class='btn btn-success']").click()
        self. driver.find_element_by_id("country").send_keys("ind")
        self.verifyLinkPresence("india")
        element = WebDriverWait(self. driver,10).until(
            EC.presence_of_element_located((By.LINK_TEXT,"india")))
        self. driver.find_element_by_link_text("india").click()
        self. driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
        self. driver.find_element_by_css_selector("[type='submit']").click()
        textMatch = self. driver.find_element_by_css_selector("[class*=alert-success']").text

        assert  ("Success! Thank You!" in textMatch)





