from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BasePage():
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

def _mouse_move(self, element):
    for _ in range(10000):
     actions = ActionChains(self.driver)
     actions.click(product_element).perform()
     time.sleep(1)