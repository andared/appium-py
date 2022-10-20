from appium.webdriver.common.touch_action import TouchAction
from appium import webdriver


class Base:
    
    def __init__(self, driver: webdriver.Remote) -> None:
        self.driver = driver
    
    def find_element(self, locator):
        return self.driver.find_element(locator)

    def touch(self) -> TouchAction:
        return TouchAction(self.driver)
