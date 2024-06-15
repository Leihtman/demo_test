from config.settings import get_settings
from pages.registration_page import RegistrationPage
from ui_dataclasses.student_dataclass import Student, DateOfBirth
from ui_enums.hobbies_enum import HobbiesEnum
from ui_enums.month_enum import MonthEnum

settings = get_settings()


def test_success_registration(browser):
    new_student = Student(
        first_name="Leihtman",
        last_name="Drop",
        email="test@gmail.com",
        gender="Female",
        mobile=89993334444,
        date_of_birth=DateOfBirth(
            day=6,
            month=MonthEnum.SEPTEMBER,
            year=1994
        ),
        subjects=["English", "Maths"],
        hobbies=[HobbiesEnum.READING.value],
        picture_file_name="img.png",
        current_address="Kazan, st. Baumana",
        state="Haryana",
        city="Panipat",
    )
    registration_page = RegistrationPage(browser)
    registration_page.open_page()
    registration_page.first_name_field.send_keys(new_student.first_name)
    registration_page.last_name_field.send_keys(new_student.last_name)
    registration_page.user_email_field.send_keys(new_student.email)
    registration_page.select_gender(new_student.gender)
    registration_page.user_number_field.send_keys(new_student.mobile)
    registration_page.date_of_birth_field.click()
    registration_page.select_month_of_birth(new_student.date_of_birth.month.value.number)
    registration_page.select_year_of_birth(new_student.date_of_birth.year)
    registration_page.select_day_of_birth(new_student.date_of_birth.day, new_student.date_of_birth.month.value.name)
    registration_page.add_subjects(new_student.subjects)
    registration_page.select_hobbies_checkbox(new_student.hobbies)
    registration_page.upload_image(new_student.picture_file_name)
    registration_page.current_address_text_area.send_keys(new_student.current_address)
    registration_page.select_state(new_student.state)
    registration_page.select_city(new_student.city)
    registration_page.submit_button.click()
    print("result")
    pass
