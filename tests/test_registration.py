from pages.registration_page import RegistrationPage
from ui_generators.student_generator import StudentGenerator


def test_success_registration(browser):
    new_student = StudentGenerator.get_success_full_student()
    registration_page = RegistrationPage(browser)
    registration_page.open_page()
    registration_page.send_keys(element=registration_page.first_name_field, value=new_student.first_name)
    registration_page.send_keys(element=registration_page.last_name_field, value=new_student.last_name)
    registration_page.send_keys(element=registration_page.user_email_field, value=new_student.email)
    registration_page.select_gender(new_student.gender)
    registration_page.send_keys(element=registration_page.user_number_field, value=new_student.mobile)
    registration_page.set_date_of_birth(new_student.date_of_birth)
    registration_page.add_subjects(new_student.subjects)
    registration_page.select_hobbies_checkbox(new_student.hobbies)
    registration_page.upload_image(new_student.picture_file_name)
    registration_page.send_keys(element=registration_page.current_address_text_area, value=new_student.current_address)
    registration_page.select_state(new_student.state)
    registration_page.select_city(new_student.city)
    registration_page.click(element=registration_page.submit_button)
    print("result")
    pass
