import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class LoginPage(BasePage):

    def __init__(self, browser, url, login, password):
        super().__init__(browser, url)
        self.login = login
        self.password = password
        self.login_selector = (By.ID, "uid")
        self.password_selector = (By.ID, "passw")
        self.button_selector = (By.NAME, "btnSubmit")

    def enter_login(self):
        self.find(self.login_selector).send_keys(self.login)

    def enter_password(self):
        self.find(self.password_selector).send_keys(self.password)

    def btn_click(self):
        self.find(self.button_selector).click()

    def page_wait(self):
        self.wait_to_load(self.button_selector)
