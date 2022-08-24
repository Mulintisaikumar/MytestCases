from selenium.webdriver.common.by import By


class Homepage:

    def __init__(self,driver):
        self.driver = driver
    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    name = (By.CSS_SELECTOR, "[name= 'name']")
    email1 = (By.CSS_SELECTOR, "a[href*='email1']")
    check = (By.ID, "a[href*='shop']")
    gender = (By.ID, "exampleFormControlSelect1")
    submit = (By.XPATH, "//input[@value='Submit']")
    successMessage = (By.CSS_SELECTOR, "[class*='alert-success']")



    def shopitem(self):
        self.driver.find_element(*Homepage.shop)
        checkOutpage = CheckOutPage(self.driver)
        return checkOutpage
       #self.find_element_by_css_selector("a[href*='shop']").click()
    def getName(self):
        return self.driver.find_element(*Homepage.name)
    def getemail1(self):
        return self.driver.find_element(*Homepage.email1)
    def getCheckBox(self):
        return self.driver.find_element(*Homepage.check)
    def getGender(self):
        return self.driver.find_element(*Homepage.gender)
    def submitForm(self):
        return self.driver.find_element(*Homepage.submit)
    def getSuccessMessage(self):
        return self.driver.find_element(*Homepage.successMessage)
