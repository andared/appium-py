from enum import Enum
import logging
import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from appium import webdriver
import pytest


class Search(Enum):
        dost = 'dostaevsky'
        Dost = 'DOSTAЕВСКИЙ — Доставка еды'
        open = 'Open'


@pytest.mark.sorting
def test_sorting(driver: webdriver.Remote):
        driver.implicitly_wait(10)
        assert driver.current_activity == '.AssetBrowserActivity'
        assert driver.current_package == 'com.android.vending'
        try:
                driver.find_element(By.ACCESSIBILITY_ID, 'Search Google Play').click()
        except NoSuchElementException:
                driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ImageView[1]').click()
        driver.find_element(
                By.XPATH, (
                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.EditText'
                )
        ).send_keys(Search.dost.value)
        driver.find_element(By.ACCESSIBILITY_ID, f'Search for "{Search.dost.value}" ').click()
        it = driver.find_element(
                By.XPATH, (
                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[1]/android.widget.TextView[1]'
                )
        ).text 
        if it == Search.Dost.value:
                driver.find_element(By.ACCESSIBILITY_ID, 'Image of app or game icon for DOSTAЕВСКИЙ — Доставка еды').click()
        name = driver.find_element(
                By.XPATH, (
                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.TextView'
                )
        ).text
        assert name == Search.Dost.value
        driver.find_element(
                By.XPATH,(
                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.FrameLayout[1]'
                )
        ).click()
        time.sleep(20)
        open = driver.find_element(
                By.XPATH,(
                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.Button[2]'
                )
        )
        assert open.text == Search.open.value
        open.click()
        time.sleep(5)
        assert driver.current_activity == '.ui.selectcityRE.SelectCityActivityRE'
        assert driver.current_package == 'ru.dostaevsky.android'

