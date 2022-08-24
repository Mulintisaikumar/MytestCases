from selenium.webdriver.common.by import By


class CheckOutpage:
    def __init__(self,driver):
        self.driver = driver

     #driver.find_elements_by_css_selector(".card-tittle a")
    #driver.find_element_by_xpath("//button[@class='btn btn-success'])
    cardTitle = (By.CSS_SELECTOR," .card-tittle a")
    cardFooter = (By.CSS_SELECTOR, ".card-footer button")
    checkOut = (By.CSS_SELECTOR,"//button[@class='btn btn-success']")


    def getCardTitles(self):
        return self.driver.find_elements(*CheckOutpage.cardTitle)
    def getCardFooter(self):
        return self.driver.find_elements(*CheckOutpage.cardFooter)
    def checkOutItems(self):
         self.driver.find_elements(*CheckOutpage.checkOut).click()
         confirmpage = ConfirmPage(self.driver)
         return confirmpage


