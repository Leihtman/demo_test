from selenium.webdriver import Keys

from config.settings import get_settings
from pages.registration_page import RegistrationPage
from ui_enums.hobbies_enum import HobbiesEnum
from ui_enums.month_enum import MonthEnum

settings = get_settings()


def test_success_registration(browser):
    registration_page = RegistrationPage(browser)
    registration_page.open_page()
    registration_page.first_name_field.send_keys("John")
    registration_page.last_name_field.send_keys("Doe")
    registration_page.user_email_field.send_keys("test@gmail.com")
    registration_page.male_radio_button.send_keys(Keys.SPACE)
    registration_page.user_number_field.send_keys(89991232211)
    registration_page.date_of_birth_field.click()
    registration_page.select_month_of_birth(MonthEnum.SEPTEMBER.value.number)
    registration_page.select_year_of_birth(1994)
    registration_page.select_day_of_birth(6, MonthEnum.SEPTEMBER.value.name)
    registration_page.add_subject("English")
    registration_page.add_subject("Maths")
    registration_page.select_hobby_checkbox(HobbiesEnum.READING.value)
    registration_page.upload_image("img.png")
    print("result")
    pass
