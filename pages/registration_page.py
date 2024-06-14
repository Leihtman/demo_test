from page_objects import PageElement
from config.settings import get_settings
from pages.base_page import BasePage

settings = get_settings()


class RegistrationPage(BasePage):
    first_name = PageElement(id_="firstName")
    last_name = PageElement(id_="lastName")
    user_email = PageElement(id_="userEmail")
    male_radio_button = PageElement(xpath="//input[@name='gender'][@type='radio'][@value='Male']")
    female_radio_button = PageElement(xpath="//input[@name='gender'][@type='radio'][@value='Female']")
    other_radio_button = PageElement(xpath="//input[@name='gender'][@type='radio'][@value='Other']")
    user_number = PageElement(id_="userNumber")
    date_of_birth_field = PageElement(id_="dateOfBirthInput")
    month_of_birth_field = PageElement(xpath="//*[@id='dateOfBirth']//select[@class='react-datepicker__month-select']")
    year_of_birth_field = PageElement(xpath="//*[@id='dateOfBirth']//select[@class='react-datepicker__year-select']")
    day_of_birth = PageElement(xpath="//input[@name='gender'][@type='radio'][@value='Other']")

    login = PageElement(css='input[type="submit"]')

    def __init__(self, browser):
        super().__init__(browser)
        self.url = settings.base_url + "/automation-practice-form"

    def get_month_of_birth_element(self, month_value: int):
        selector_type, value = PageElement(xpath=f"//*[@id='dateOfBirth']//option[@value='{month_value}']").locator
        return self.browser.find_element(selector_type, value)

    def get_year_of_birth_element(self, year_value: int):
        selector_type, value = PageElement(xpath=f"//*[@id='dateOfBirth']//option[@value='{year_value}']").locator
        return self.browser.find_element(selector_type, value)

    def get_day_of_birth_element(self, day_value: int, month_value: str):
        selector_type, value = PageElement(
            xpath=f"//div[@id='dateOfBirth']//div[text()='{day_value}' and contains(@aria-label, '{month_value}')]"
        ).locator
        return self.browser.find_element(selector_type, value)

    def select_month_of_birth(self, month_number: int):
        self.month_of_birth_field.click()
        self.get_month_of_birth_element(month_number).click()

    def select_year_of_birth(self, year_number: int):
        self.year_of_birth_field.click()
        self.get_year_of_birth_element(year_number).click()

    def select_day_of_birth(self, day_number: int, month_str: str):
        self.get_day_of_birth_element(day_number, month_str).click()
