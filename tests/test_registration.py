from selenium.webdriver import Keys

from config.settings import get_settings
from pages.registration_page import RegistrationPage

settings = get_settings()


def test_success_registration(browser):
    registration_page = RegistrationPage(browser)
    registration_page.open_page()
    registration_page.first_name.send_keys("John")
    registration_page.last_name.send_keys("Doe")
    registration_page.user_email.send_keys("test@gmail.com")
    registration_page.male_radio_button.send_keys(Keys.SPACE)
    registration_page.user_number.send_keys(89991232211)
    pass
