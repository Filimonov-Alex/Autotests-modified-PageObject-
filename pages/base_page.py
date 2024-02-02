from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open_page(self):
        self.browser.get(self.url)

    def find(self, args):
        return self.browser.find_element(*args)

    def opened(self):
        if self.browser.current_url == self.url:
            return True
        else:
            return False

    def wait_to_load(self, element):
        self.wait = WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable((element)))
