import os

import allure
from page_objects import PageElement
from selenium.webdriver import Keys, ActionChains

from config.settings import get_settings
from pages.base_page import BasePage
from ui_dataclasses.student_dataclass import DateOfBirth
from ui_enums.hobbies_enum import HobbiesEnum

settings = get_settings()


class RegistrationPage(BasePage):
    first_name_field = PageElement(id_="firstName")
    last_name_field = PageElement(id_="lastName")
    user_email_field = PageElement(id_="userEmail")
    user_number_field = PageElement(id_="userNumber")
    date_of_birth_field = PageElement(id_="dateOfBirthInput")
    subjects_field = PageElement(id_="subjectsInput")
    file_upload_button = PageElement(id_="uploadPicture")
    current_address_text_area = PageElement(id_="currentAddress")
    city_selector = PageElement(id_="city")
    month_of_birth_field = PageElement(xpath="//*[@id='dateOfBirth']//select[@class='react-datepicker__month-select']")
    year_of_birth_field = PageElement(xpath="//*[@id='dateOfBirth']//select[@class='react-datepicker__year-select']")
    state_selector = PageElement(xpath="//div[text()='Select State']")
    subjects_element = PageElement(css=".subjects-auto-complete__value-container")
    gender_radio_button_xpath_str = "//input[@name='gender'][@type='radio'][@value='{gender}']"
    month_of_birth_xpath_str = "//*[@id='dateOfBirth']//option[@value='{month}']"
    year_of_birth_xpath_str = "//*[@id='dateOfBirth']//option[@value='{year}']"
    day_of_birth_xpath_str = "//div[@id='dateOfBirth']//div[text()='{day}' and contains(@aria-label, '{month}')]"
    hobby_checkbox_xpath_str = "//input[@type='checkbox'][@value='{hobby_number}']"

    def __init__(self, browser):
        super().__init__(browser)
        self.url = settings.base_url + "/automation-practice-form"

    @allure.step("RP: Select student gender")
    def select_gender(self, gender_value: str):
        ready_xpath_str = self.gender_radio_button_xpath_str.format(gender=gender_value)
        detected_element = self.find_element_by_xpath(ready_xpath_str)
        detected_element.send_keys(Keys.SPACE)

    @allure.step("RP: Select month of birth")
    def select_month_of_birth(self, month_value: int):
        self.month_of_birth_field.click()
        ready_xpath_str = self.month_of_birth_xpath_str.format(month=month_value)
        detected_element = self.find_element_by_xpath(ready_xpath_str)
        self.click(detected_element)

    @allure.step("RP: Select year of birth")
    def select_year_of_birth(self, year_value: int):
        self.year_of_birth_field.click()
        ready_xpath_str = self.year_of_birth_xpath_str.format(year=year_value)
        detected_element = self.find_element_by_xpath(ready_xpath_str)
        self.click(detected_element)

    @allure.step("RP: Select day of birth")
    def select_day_of_birth(self, day_value: int, month_value: str):
        ready_xpath_str = self.day_of_birth_xpath_str.format(day=day_value, month=month_value)
        detected_element = self.find_element_by_xpath(ready_xpath_str)
        self.click(detected_element)

    @allure.step("RP: Set date of birth")
    def set_date_of_birth(self, date_of_birth: DateOfBirth):
        self.click(element=self.date_of_birth_field)
        self.select_month_of_birth(date_of_birth.month.value.number)
        self.select_year_of_birth(date_of_birth.year)
        self.select_day_of_birth(date_of_birth.day, date_of_birth.month.value.name)

    @allure.step("RP: Add subject")
    def add_subjects(self, subjects: list[str]):
        for subject in subjects:
            self.subjects_element.click()
            self.send_keys(self.subjects_field, subject)
            self.send_keys(self.subjects_field, Keys.ENTER)

    @allure.step("RP: Select hobby checkbox")
    def select_hobbies_checkbox(self, hobbies: list[HobbiesEnum]):
        for hobby in hobbies:
            ready_xpath_str = self.hobby_checkbox_xpath_str.format(hobby_number=hobby.value.number)
            detected_element = self.find_element_by_xpath(ready_xpath_str)
            ActionChains(self.browser).move_to_element(detected_element).click().perform()

    @allure.step("RP: Upload image")
    def upload_image(self, image_name: str):
        data_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data'))
        file_path = os.path.join(data_dir, image_name)
        self.send_keys(self.file_upload_button, file_path)

    @allure.step("RP: Select state")
    def select_state(self, state_name: str):
        self.state_selector.click()
        detected_element = self.find_element_by_text(state_name)
        self.click(detected_element)

    @allure.step("RP: Select city")
    def select_city(self, city_name: str):
        self.city_selector.click()
        detected_element = self.find_element_by_text(city_name)
        self.click(detected_element)
