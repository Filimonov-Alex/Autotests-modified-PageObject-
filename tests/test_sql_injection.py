import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datafortests import sql_injections
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.welcome_page import WelcomePage
import time


@pytest.mark.parametrize("login, password",
                         sql_injections
                         )
def test_sql_injection(browser, login, password):
    print("Тестирование на защиту от sql-инъекций:")
    home_page = HomePage(browser, "http://testfire.net/index.jsp")
    login_page = LoginPage(
        browser, "https://testfire.net/login.jsp", login, password)
    welcome_page = WelcomePage(browser, "http://testfire.net/bank/main.jsp")
    home_page.open_page()
    assert home_page.opened(), "Главная страница не открылась"
    print("Главная страница открыта")
    home_page.login_link_click()
    print("Страница авторизации открыта")
    login_page.enter_login()
    login_page.enter_password()
    login_page.btn_click()
    print("Данные загружены в форму и отправлены на сервер")
    assert welcome_page.opened(), f"Для SQL-инъекции: {
        login} аутентификация не произошла. Защита сработала, уязвимость не обнаружена."
    print(f"Для SQL-инъекции {
          login} произошла аутентификация. Обнаружена уязимость.")
