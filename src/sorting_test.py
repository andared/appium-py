from enum import Enum
import logging
import time
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from appium import webdriver
import pytest


class Search(Enum):
        dost = 'достаевский'
        app = 'DOSTAЕВСКИЙ — Доставка еды'
        score = '3.0'
        desc = 'Order pizza 🍕, sushi 🍣, wok 🥡, burgers 🍔, shawarma and get a cake as a gift 🎁'


@pytest.mark.sorting
def test_sorting(driver_sort: webdriver.Remote):
        driver = driver_sort
        touch = TouchAction(driver)
        driver.implicitly_wait(5)
        assert driver.current_activity == '.AssetBrowserActivity'
        assert driver.current_package == 'com.android.vending'
        logging.info('Play Market opened')
        driver.find_element(By.ACCESSIBILITY_ID, 'Search Google Play').click()
        logging.info('Search box found')
        driver.find_element(
                By.XPATH, (
                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.EditText'
                )
        ).send_keys(Search.dost.value)
        logging.info(f'Text {Search.dost.value} input')
        driver.find_element(By.ACCESSIBILITY_ID, f'Search for "{Search.dost.value}" ').click()
        logging.info('The correct option found')
        timeout = time.time() + 30
        app = False
        while time.time() < timeout:
                try:
                        app = driver.find_element(By.XPATH, f'//android.view.View[@content-desc="Image of app or game icon for {Search.app.value}"]')
                        break
                except NoSuchElementException:
                        view = driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout')
                        x = round((view.location['x'] + view.size['width'] / 2))
                        y1 = round((view.location['y'] + view.size['height']))
                        y2 = round((view.location['y'] + view.size['height']) / 3)
                        touch.press(None, x, y1).wait(1000).move_to(None, x, y2).release().perform()
        assert app
        logging.info('The correct app found')
        app.click()
        app = driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[2]/android.widget.TextView[1]').text
        score = driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[2]/android.widget.HorizontalScrollView[1]/android.view.View[1]/android.widget.TextView[1]').text
        driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[2]/android.view.View[2]/android.widget.Button')
        driver.find_element(By.ACCESSIBILITY_ID, 'Screenshot "1" of "6"')
        desc = driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[2]/android.widget.TextView[4]').text
        assert app == Search.app.value
        assert score == Search.score.value
        assert desc == Search.desc.value
