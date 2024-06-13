from page_objects import PageElement
from config.settings import get_settings
from pages.base_page import BasePage

settings = get_settings()


class RegistrationPage(BasePage):
    first_name = PageElement(id_='firstName')
    last_name = PageElement(id_='lastName')
    user_email = PageElement(id_='userEmail')
    male_radio_button = PageElement(xpath='//input[@name=\'gender\'][@type=\'radio\'][@value=\'Male\']')
    female_radio_button = PageElement(xpath='//input[@name=\'gender\'][@type=\'radio\'][@value=\'Female\']')
    other_radio_button = PageElement(xpath='//input[@name=\'gender\'][@type=\'radio\'][@value=\'Other\']')
    user_number = PageElement(id_='userNumber')
    login = PageElement(css='input[type="submit"]')

    def __init__(self, webdriver):
        super().__init__(webdriver)
        self.url = settings.base_url + "/automation-practice-form"
