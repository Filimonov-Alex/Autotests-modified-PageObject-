import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datafortests import default_auth_info
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.welcome_page import WelcomePage


@pytest.mark.parametrize("login, password",
                         default_auth_info
                         )
def test_default_data_auth(browser, login, password):
    print("Тестирование на использование учетных данных по умолчанию:")
    home_page = HomePage(browser, "http://testfire.net/index.jsp")
    login_page = LoginPage(
        browser, "https://testfire.net/login.jsp", login, password)
    welcome_page = WelcomePage(browser, "http://testfire.net/bank/main.jsp")
    home_page.open_page()
    assert home_page.opened(), "Главная страница не открылась"
    print("Главная страница открыта")
    home_page.login_link_click()
    browser.implicitly_wait(10)
    login_page.enter_login()
    login_page.enter_password()
    login_page.btn_click()
    print("Данные загружены в форму и отправлены на сервер")
    assert welcome_page.opened(), f"Для пары значений по умолчанию: {
        login}/{password} аутентификация не произошла. Уязвимость не обнаружена."
    print(f"Для пары значений по умолчанию {
          login}/{password} произошла аутентификация. Тест провален.")
