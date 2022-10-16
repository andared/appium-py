from enum import Enum
import logging
import time
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from appium import webdriver
import pytest


@pytest.mark.usefixtures('swipe')
@pytest.mark.swiping
def test_swiping(driver: webdriver.Remote):
    touch = TouchAction(driver)
    driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.appcompat.widget.LinearLayoutCompat/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.ViewFlipper/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.ViewFlipper/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]').click()
    stick = driver.find_element(By.ID, 'ru.dostaevsky.android:id/design_bottom_sheet')
    x = stick.location['x'] + stick.size['wight']
    y1 = stick.location['y']
    y2 = stick.location['y'] + stick.size['height']
    touch.press(None, x, y1).wait(100).move_to(None, x, y2).release().perform()