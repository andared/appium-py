from appium import webdriver
from appium.webdriver.extensions.android.gsm import GsmSignalStrength
from appium.webdriver.extensions.android.network import NetSpeed
from settings import Settings
import pytest
import logging


class ErorrConnection(Exception):
    pass


@pytest.fixture()
def driver_sort() -> webdriver.Remote:
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
        driver.set_gsm_signal(GsmSignalStrength.GREAT)
        driver.set_network_speed(NetSpeed.FULL)
        driver.start_activity('com.android.vending', '.AssetBrowserActivity')
    except:
        logging.warning('Could not connect to device')
        raise ErorrConnection('Could not connect to device')
    yield driver
    driver.quit()
    logging.info('Disconnecting from device')


@pytest.fixture()
def driver_swipe() -> webdriver.Remote:
    try:
        desired_caps = {
            'platformName': 'Android',
            'appium:app': Settings.APK,
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
        logging.info('App installed')
        driver.set_gsm_signal(GsmSignalStrength.GREAT)
        driver.set_network_speed(NetSpeed.FULL)
    except ErorrConnection:
        logging.warning('Could not connect to device')
        raise ErorrConnection('Could not connect to device')
    yield driver
    driver.remove_app('ru.dostaevsky.android')
    driver.quit()
    logging.info('Disconnecting from device')
