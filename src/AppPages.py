from BaseApp import Base
from selenium.webdriver.common.by import By


class DostaevskySearchLocators:
    CITY_SPB = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.appcompat.widget.LinearLayoutCompat/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.ViewFlipper/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.ViewFlipper/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]')
    MENU = (By.ID, 'ru.dostaevsky.android:id/design_bottom_sheet')
    MAIN = (By.ID, 'ru.dostaevsky.android:id/vp_main')
    CATEGORIES = (By.ID, 'ru.dostaevsky.android:id/recyclerViewCategories')
    CATEGORY = (By.ID, 'ru.dostaevsky.android:id/recyclerViewCategory')


class Swipe(Base):

    def choose_city(self):
        self.find_element(DostaevskySearchLocators.CITY_SPB).click()
    
    def swipe_down_menu(self):
        element = self.find_element(DostaevskySearchLocators.MENU)
        x = round(element.location['x'] + element.size['width'] / 2)
        y1 = round(element.location['y'])
        y2 = round(element.location['y'] + element.size['height'])
        self.touch().press(None, x, y1).wait(100).move_to(None, x, y2).release().perform()

    def swipe_up_and_down_main(self):
        element = self.find_element(DostaevskySearchLocators.MAIN)
        x1 = round(element.size['width'] - 100)
        x2 = round(element.location['x'] + 100)
        y = round(element.location['y'] + element.size['height'] / 2)
        for _ in range(2):
            self.touch().press(None, x1, y).wait(100).move_to(None, x2, y).release().perform()
            self.touch().press(None, x2, y).wait(100).move_to(None, x1, y).release().perform()
    
    def swipe_left_and_right_categories(self):
        element = self.find_element(DostaevskySearchLocators.CATEGORIES)
        x = round(element.location['x'] + element.size['width'] / 2)
        y2 = round(element.location['y'])
        y1 = round(element.location['y'] + element.size['height'])
        for _ in range(2):
            self.touch().press(None, x, y1).wait(100).move_to(None, x, y2).release().perform()
            self.touch().press(None, x, y2).wait(100).move_to(None, x, y1).release().perform()
    

