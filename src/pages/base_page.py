from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
import time
from selenium.common.exceptions import TimeoutException


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    # Метод для кликов по элементам страницы
    def click_element(self, locator, time=30):
        self.driver.execute_script("""
        let t = document.querySelectorAll('.osr-overlay, .noselect')
        Array.from(t).map(x=>{x.innerHTML = ""; x.className = ""})
        """)
        element = WebDriverWait(self.driver, time).until(EC.visibility_of_all_elements_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView();", element[0])
        return WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(locator)).click()

    # Метод для ввода текста
    def type_text(self, locator, text, time=30):
        return WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator)).send_keys(text)

    def check_element_visibility(self, locator):
        WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(locator))
        return True

    def quick_check_visibility(self, locator):
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False
