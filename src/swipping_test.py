import time
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from appium import webdriver
import pytest


@pytest.mark.swiping
def test_swiping(driver_swipe: webdriver.Remote):
    driver = driver_swipe
    driver.implicitly_wait(10)
    touch = TouchAction(driver)
    driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.appcompat.widget.LinearLayoutCompat/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.ViewFlipper/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.ViewFlipper/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]').click()
    stick = driver.find_element(By.ID, 'ru.dostaevsky.android:id/design_bottom_sheet')
    x = round(stick.location['x'] + stick.size['width'] / 2)
    y1 = round(stick.location['y'])
    y2 = round(stick.location['y'] + stick.size['height'])
    touch.press(None, x, y1).wait(500).move_to(None, x, y2).release().perform()
    time.sleep(0.5)
    main = driver.find_element(By.ID, 'ru.dostaevsky.android:id/vp_main')
    x1 = round(main.size['width'] - 100)
    x2 = round(main.location['x'] + 100)
    y = round(main.location['y'] + main.size['height'] / 2)
    for _ in range(2):
        touch.press(None, x1, y).wait(500).move_to(None, x2, y).release().perform()
        time.sleep(0.5)
        touch.press(None, x2, y).wait(500).move_to(None, x1, y).release().perform()
    time.sleep(0.5)
    recycler = driver.find_element(By.ID, 'ru.dostaevsky.android:id/recyclerViewCategories')
    x = round(recycler.location['x'] + recycler.size['width'] / 2)
    y2 = round(recycler.location['y'])
    y1 = round(recycler.location['y'] + recycler.size['height'])
    for _ in range(2):
        touch.press(None, x, y1).wait(500).move_to(None, x, y2).release().perform()
        time.sleep(0.5)
        touch.press(None, x, y2).wait(500).move_to(None, x, y1).release().perform()
    time.sleep(0.5)
    driver.find_element(By.ID, 'ru.dostaevsky.android:id/bottomNavigationCatalogMenuId').click()
    recycler = driver.find_element(By.ID, 'ru.dostaevsky.android:id/recyclerViewCategory')
    x = round(recycler.location['x'] + recycler.size['width'] / 2)
    y2 = round(recycler.location['y'])
    y1 = round(recycler.location['y'] + recycler.size['height'])
    touch.press(None, x, y1).wait(100).move_to(None, x, y2).release().perform()
    time.sleep(1)
