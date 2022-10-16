from appium import webdriver
from appium.webdriver.extensions.android.gsm import GsmSignalStrength
from appium.webdriver.extensions.android.network import NetSpeed
from settings import Settings
import pytest
import logging


class ErorrConnection(Exception):
    pass


@pytest.fixture(scope="session", autouse=True, name="driver")
def connection() -> webdriver.Remote:
    try:
        desired_caps = {
            'platformName': 'Android',
            'newCommandTimeout': '30',
            'language': 'en',
            'locale': 'RU',
            'orientation': 'PORTRAIT',
            'unicodeKeyboard': 'true',
            'resetKeyboard': 'true',
            'noReset': 'false',
            'fastReset': 'true',
            'clearSystemFiles': 'true'
        }
        logging.info('Start connecting to device')
        driver = webdriver.Remote(Settings.HOST + '/wd/hub', desired_caps)
        logging.info('Connecting succesfull')
    except:
        logging.warning('Could not connect to device')
        raise ErorrConnection('Could not connect to device')
    yield driver
    driver.quit()
    logging.info('Disconnecting from device')


@pytest.fixture(name='sort')
def sort(driver: webdriver.Remote) -> None:
        driver.set_gsm_signal(GsmSignalStrength.GREAT)
        driver.set_network_speed(NetSpeed.FULL)
        driver.start_activity('com.android.vending', '.AssetBrowserActivity')


@pytest.fixture(name='swipe')
def swipe(driver: webdriver.Remote) -> None:
        driver.set_gsm_signal(GsmSignalStrength.GREAT)
        driver.set_network_speed(NetSpeed.FULL)
        driver.install_app('C:/Workflow/mobile-automation/test.apk')
        driver.start_activity('ru.dostaevsky.android', None)
        logging.info('App installed')
