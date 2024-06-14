import os

from page_objects import PageElement
from selenium.webdriver import Keys, ActionChains

from config.settings import get_settings
from pages.base_page import BasePage

settings = get_settings()


class RegistrationPage(BasePage):
    first_name_field = PageElement(id_="firstName")
    last_name_field = PageElement(id_="lastName")
    user_email_field = PageElement(id_="userEmail")
    male_radio_button = PageElement(xpath="//input[@name='gender'][@type='radio'][@value='Male']")
    female_radio_button = PageElement(xpath="//input[@name='gender'][@type='radio'][@value='Female']")
    other_radio_button = PageElement(xpath="//input[@name='gender'][@type='radio'][@value='Other']")
    user_number_field = PageElement(id_="userNumber")
    date_of_birth_field = PageElement(id_="dateOfBirthInput")
    month_of_birth_field = PageElement(xpath="//*[@id='dateOfBirth']//select[@class='react-datepicker__month-select']")
    year_of_birth_field = PageElement(xpath="//*[@id='dateOfBirth']//select[@class='react-datepicker__year-select']")
    subjects_element = PageElement(css=".subjects-auto-complete__value-container")
    subjects_field = PageElement(id_="subjectsInput")
    file_upload_button = PageElement(id_="uploadPicture")
    current_address_text_area = PageElement(id_="currentAddress")
    state_selector = PageElement(xpath="//div[text()='Select State']")
    city_selector = PageElement(id_="city")

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

    def get_hobby_element(self, hobby_number: int):
        selector_type, value = PageElement(xpath=f"//input[@type='checkbox'][@value='{hobby_number}']").locator
        return self.browser.find_element(selector_type, value)

    def select_month_of_birth(self, month_number: int):
        self.month_of_birth_field.click()
        self.get_month_of_birth_element(month_number).click()

    def select_year_of_birth(self, year_number: int):
        self.year_of_birth_field.click()
        self.get_year_of_birth_element(year_number).click()

    def select_day_of_birth(self, day_number: int, month_str: str):
        self.get_day_of_birth_element(day_number, month_str).click()

    def add_subject(self, value: str):
        self.subjects_element.click()
        self.subjects_field.send_keys(value)
        self.subjects_field.send_keys(Keys.ENTER)

    def select_hobby_checkbox(self, hobby_number: int):
        element = self.get_hobby_element(hobby_number)
        ActionChains(self.browser).move_to_element(element).click().perform()

    def upload_image(self, image_name: str):
        data_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data'))
        file_path = os.path.join(data_dir, image_name)
        self.file_upload_button.send_keys(file_path)

    def select_state(self, state_name: str):
        self.state_selector.click()
        self.get_element_by_text(state_name).click()

    def select_city(self, city_name: str):
        self.city_selector.click()
        self.get_element_by_text(city_name).click()
