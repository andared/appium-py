import logging
from enum import Enum
from src.BaseApp import Base
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class var(Enum):
    drinks = 'Напитки'
    juice = 'Сок'
    size = '0,97 л'
    price = '189'


class DostaevskySearchLocators:
    CITY_SPB = [By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.appcompat.widget.LinearLayoutCompat/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.ViewFlipper/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.ViewFlipper/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]']
    BOTTOM = [By.ID, 'ru.dostaevsky.android:id/design_bottom_sheet']
    MAIN = [By.ID, 'ru.dostaevsky.android:id/vp_main']
    CATEGORIES = [By.ID, 'ru.dostaevsky.android:id/recyclerViewCategories']
    CATEGORY = [By.ID, 'ru.dostaevsky.android:id/recyclerViewCategory']
    MENU = [By.ID, 'ru.dostaevsky.android:id/bottomNavigationCatalogMenuId']
    DRINKS = [By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/androidx.appcompat.widget.LinearLayoutCompat/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.ViewFlipper/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ViewFlipper/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[6]/android.widget.RelativeLayout/android.widget.TextView']
    TABS = [By.ID, 'ru.dostaevsky.android:id/tabLayoutCatalog']
    DRINKPAGE = [By.ID, 'ru.dostaevsky.android:id/viewPagerCatalog']
    PRODUCTS = [By.ID, 'ru.dostaevsky.android:id/rootProductView']
    
    def product(n):
        return [By.XPATH, f'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/androidx.appcompat.widget.LinearLayoutCompat/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.ViewFlipper/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ViewFlipper/android.widget.RelativeLayout/android.widget.FrameLayout/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/android.widget.ViewFlipper/android.widget.FrameLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[{n}]/android.view.ViewGroup/androidx.appcompat.widget.LinearLayoutCompat/android.widget.TextView']

    def price(n):
        return [By.XPATH, f'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/androidx.appcompat.widget.LinearLayoutCompat/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.ViewFlipper/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ViewFlipper/android.widget.RelativeLayout/android.widget.FrameLayout/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/android.widget.ViewFlipper/android.widget.FrameLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[{n}]/android.view.ViewGroup/androidx.appcompat.widget.LinearLayoutCompat/android.view.ViewGroup/android.widget.TextView[2]']


class SelectCityActivityRE(Base):

    def choose_city(self) -> None:
        try:
            loc = DostaevskySearchLocators.CITY_SPB
            self.find_element(loc[0], loc[1]).click()
            logging.info('Tap on city SPB')
        except NoSuchElementException:
            pass


class MainActivityRE(Base):

    def click_drinks(self) -> None:
        loc = DostaevskySearchLocators.DRINKS
        self.find_element(loc[0], loc[1]).click()
        logging.info('Tap on Drinks')
    

    def click_menu(self) -> None:
        loc = DostaevskySearchLocators.MENU
        self.find_element(loc[0], loc[1]).click()
        logging.info('Tap on menu')
    

    def swipe_up_categories(self) -> None:
        loc = DostaevskySearchLocators.CATEGORIES
        element = self.find_element(loc[0], loc[1])
        x = round(element.location['x'] + element.size['width'] / 2)
        y2 = round(element.location['y'])
        y1 = round(element.location['y'] + element.size['height'])
        self.touch().press(None, x, y1).wait(100).move_to(None, x, y2).release().perform()
        logging.info('Swipe up categories')
    

    def swipe_down_categories(self) -> None:
        loc = DostaevskySearchLocators.CATEGORIES
        element = self.find_element(loc[0], loc[1])
        x = round(element.location['x'] + element.size['width'] / 2)
        y2 = round(element.location['y'])
        y1 = round(element.location['y'] + element.size['height'])
        self.touch().press(None, x, y2).wait(100).move_to(None, x, y1).release().perform()
        logging.info('Swipe down categories')
    

    def swipe_left_main(self) -> None:
        loc = DostaevskySearchLocators.MAIN
        element = self.find_element(loc[0], loc[1])
        x1 = round(element.size['width'] - 100)
        x2 = round(element.location['x'] + 100)
        y = round(element.location['y'] + element.size['height'] / 2)
        self.touch().press(None, x1, y).wait(200).move_to(None, x2, y).release().perform()
        logging.info('Swipe left promo')


    def swipe_down_bottom(self) -> None:
        loc = DostaevskySearchLocators.BOTTOM
        element = self.find_element(loc[0], loc[1])
        x = round(element.location['x'] + element.size['width'] / 2)
        y1 = round(element.location['y'])
        y2 = round(element.location['y'] + element.size['height'])
        self.touch().press(None, x, y1).wait(200).move_to(None, x, y2).release().perform()
        logging.info('Swipe down bottom')


    def swipe_right_main(self) -> None:
        loc = DostaevskySearchLocators.MAIN
        element = self.find_element(loc[0], loc[1])
        x1 = round(element.size['width'] - 100)
        x2 = round(element.location['x'] + 100)
        y = round(element.location['y'] + element.size['height'] / 2)
        self.touch().press(None, x2, y).wait(200).move_to(None, x1, y).release().perform()
        logging.info('Swipe right promo')
    

    def swipe_up_category(self) -> None:
        loc = DostaevskySearchLocators.CATEGORY
        element = self.find_element(loc[0], loc[1])
        x = round(element.location['x'] + element.size['width'] / 2)
        y2 = round(element.location['y'])
        y1 = round(element.location['y'] + element.size['height'])
        self.touch().press(None, x, y1).wait(200).move_to(None, x, y2).release().perform()
        logging.info('Swipe up hot dishes')


class DrinksPage(Base):

    def short_swipe_down_drinks(self) -> None:
        loc = DostaevskySearchLocators.DRINKPAGE
        element = self.find_element(loc[0], loc[1])
        x = round(element.location['x'] + element.size['width'] / 2)
        y1 = round(element.location['y'] + element.size['height'] / 6)
        y2 = round(element.location['y'] + element.size['height'] * 5 / 6)
        self.touch().press(None, x, y1).wait(500).move_to(None, x, y2).release().perform()
        logging.info('Short swipe down drinks')


    def swipe_up_drinks(self) -> None:
        loc = DostaevskySearchLocators.DRINKPAGE
        element = self.find_element(loc[0], loc[1])
        x = round(element.location['x'] + element.size['width'] / 2)
        y2 = round(element.location['y'])
        y1 = round(element.location['y'] + element.size['height'])
        self.touch().press(None, x, y1).wait(100).move_to(None, x, y2).release().perform()
        logging.info('Swipe up drinks')
    

    def check_juices(self) -> None:
        loc = DostaevskySearchLocators.PRODUCTS
        n = len(self.find_elements(loc[0], loc[1]))
        self.driver.implicitly_wait(1)
        for i in range(1, n):
            loc = DostaevskySearchLocators.product(i)
            try:
                txt = self.find_element(loc[0], loc[1]).text
                if var.juice.value in txt:
                    assert var.size.value in txt, txt
                    logging.info(txt)
                    loc = DostaevskySearchLocators.price(i)
                    txt = self.find_element(loc[0], loc[1]).text
                    assert var.price.value in txt, txt
                    logging.info(txt[2:])
            except NoSuchElementException:
                pass
