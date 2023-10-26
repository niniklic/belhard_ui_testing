import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from src.constants import BASE_URL
import os


@pytest.fixture(scope="function")
def driver(request):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver.get(BASE_URL)
    driver.implicitly_wait(1)
    yield driver
    driver.quit()
