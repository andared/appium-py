from appium.webdriver.extensions.android.gsm import GsmSignalStrength
from appium.webdriver.extensions.android.network import NetSpeed
from settings import Settings
from appium import webdriver
import pytest
import logging


@pytest.fixture(scope="session", name="driver")
def driver() -> webdriver.Remote:
    desired_caps = {
        'platformName': 'Android',
        'appium:app': Settings.APK
    }
    logging.info('Start connecting to device')
    driver = webdriver.Remote(Settings.HOST + '/wd/hub', desired_caps)
    logging.info('Connecting succesfull')
    logging.info('App installed')
    driver.set_gsm_signal(GsmSignalStrength.GREAT)
    yield driver
    driver.remove_app('ru.dostaevsky.android')
    logging.info('Disconnecting from device')
    driver.quit()


@pytest.fixture(autouse=True)
def check_app(driver: webdriver.Remote):
    if driver.is_app_installed('ru.dostaevsky.android'):
        driver.launch_app()
    driver.implicitly_wait(10)
