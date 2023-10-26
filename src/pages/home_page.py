import time
from selenium.webdriver.common.by import By
from src.pages.base_page import BasePage


class HomePageLocators:
    title = "Интернет-магазин МТС | Рассрочка на смартфоны и гаджеты"




class HomePage(BasePage):

    @staticmethod
    def get_title():
        return HomePageLocators.title
