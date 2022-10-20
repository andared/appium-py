from src.AppPages import SelectCityActivityRE, MainActivityRE
import pytest


@pytest.mark.sorting
def test_sorting(driver):
    SelectCityActivityRE(driver).choose_city()
    main = MainActivityRE(driver)
    main.swipe_down_bottom()
    main.swipe_up_categories()
    main.click_drinks()
    main.swipe_up_drinks()
    for _ in range(3):
        main.check_juices()
        main.short_swipe_down_category()
