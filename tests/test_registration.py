from config.settings import get_settings
from pages.registration_page import RegistrationPage

settings = get_settings()


def test_success_registration(browser):
    registration_page = RegistrationPage(browser)
    registration_page.open_page()
    pass
