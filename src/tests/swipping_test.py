from src.AppPages import SelectCityActivityRE, MainActivityRE
import pytest


@pytest.mark.swiping
def test_swiping(driver):
    SelectCityActivityRE(driver).choose_city()
    main = MainActivityRE(driver)
    main.swipe_down_bottom()
    for _ in range(2):
        main.swipe_left_main()
        main.swipe_right_main()
    for _ in range(2):
        main.swipe_up_categories()
        main.swipe_down_categories()
    main.click_menu()
    main.swipe_up_category()
