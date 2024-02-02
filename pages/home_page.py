from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class HomePage(BasePage):

    def __init__(self, browser, url):
        super().__init__(browser, url)
        self.login_link_selector = (By.ID, "LoginLink")

    def login_link_click(self):
        self.find(self.login_link_selector).click()
