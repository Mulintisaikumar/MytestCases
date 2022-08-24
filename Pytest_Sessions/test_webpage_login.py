from selenium import webdriver
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

def test_google():
    driver = webdriver.Chrome("C:\\chromedriver.exe")

    driver.get("https://www.google.com/")
    assert driver.title=="Google"
    driver.quit()

def test_rediff():
    driver = webdriver.Chrome("C:\\chromedriver.exe")
    driver.implicitly_wait(5)
    driver.get("https://www.rediff.com/")
    assert driver.title=="Rediff.com: News | Rediffmail | Stock Quotes | Shopping"
    driver.quit()
