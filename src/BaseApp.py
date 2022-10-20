from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException
from appium import webdriver


class Base:
    
    def __init__(self, driver: webdriver.Remote) -> None:
        self.driver = driver
    
    def find_element(self, strategy, locator):
        return self.driver.find_element(strategy, locator)

    def find_elements(self, strategy, locator):
        return self.driver.find_elements(strategy, locator)

    def touch(self) -> TouchAction:
        return TouchAction(self.driver)
