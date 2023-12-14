from selenium.webdriver.common.by import By

class peoductPage():

     def __init__(self, driver):
         self.driver = driver
         product_element = self.driver.find_element(By.ID, "bigCookie")
