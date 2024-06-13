from page_objects import PageElement
from config.settings import get_settings
from pages.base_page import BasePage

settings = get_settings()


class RegistrationPage(BasePage):
    username = PageElement(id_='username')
    password = PageElement(name='password')
    login = PageElement(css='input[type="submit"]')

    def __init__(self, webdriver):
        super().__init__(webdriver)
        self.url = settings.base_url + "/automation-practice-form"
