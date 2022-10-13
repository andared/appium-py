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
            'unicodeKeyboard': 'true',
            'resetKeyboard': 'true',
            'noReset': 'true',
            'appActivity': '.AssetBrowserActivity',
            'appPackage': 'com.android.vending'
        }
        logging.info('Start connecting to device')
        driver = webdriver.Remote(Settings.HOST + '/wd/hub', desired_caps)
        logging.info('Connecting succesfull')
        driver.set_gsm_signal(GsmSignalStrength.GREAT)
        driver.set_network_speed(NetSpeed.FULL)
    except:
        logging.warning('Could not connect to device')
        raise ErorrConnection('Could not connect to device')
    yield driver
    #driver.quit()
    logging.info('Disconnecting from device')
