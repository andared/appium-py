from src.AppPages import SelectCityActivityRE, MainActivityRE, DrinksPage
import pytest


@pytest.mark.sorting
def test_sorting(driver):
    SelectCityActivityRE(driver).choose_city()
    main = MainActivityRE(driver)
    main.swipe_down_bottom()
    main.swipe_up_categories()
    main.click_drinks()
    drinks = DrinksPage(driver)
    drinks.swipe_up_drinks()
    for _ in range(4):
        drinks.check_juices()
        drinks.short_swipe_down_drinks()
