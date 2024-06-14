from selenium.webdriver import Keys

from config.settings import get_settings
from pages.registration_page import RegistrationPage
from ui_enums.month_enum import MonthEnum

settings = get_settings()


def test_success_registration(browser):
    registration_page = RegistrationPage(browser)
    registration_page.open_page()
    registration_page.first_name.send_keys("John")
    registration_page.last_name.send_keys("Doe")
    registration_page.user_email.send_keys("test@gmail.com")
    registration_page.male_radio_button.send_keys(Keys.SPACE)
    registration_page.user_number.send_keys(89991232211)
    registration_page.date_of_birth_field.click()
    registration_page.select_month_of_birth(MonthEnum.SEPTEMBER.value.number)
    registration_page.select_year_of_birth(1994)
    registration_page.select_day_of_birth(6, MonthEnum.SEPTEMBER.value.name)
    print("result")
    pass
