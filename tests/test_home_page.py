import time
from selenium.webdriver.common.by import By
from src.pages.home_page import HomePage


class Test_Home_Page:
    def test_is_open_home_page(self, driver):
        HomePage(driver)
        assert driver.title == HomePage.get_title()

