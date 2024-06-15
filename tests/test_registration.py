from pages.registration_page import RegistrationPage
from pages.registration_submit_modal import RegistrationSubmitModal
from ui_generators.student_generator import StudentGenerator


def test_success_registration(browser):
    # Arrange
    test_student = StudentGenerator.get_success_full_student()
    registration_page = RegistrationPage(browser)
    registration_page.open_page()
    registration_page.send_keys(element=registration_page.first_name_field, value=test_student.first_name)
    registration_page.send_keys(element=registration_page.last_name_field, value=test_student.last_name)
    registration_page.send_keys(element=registration_page.user_email_field, value=test_student.email)
    registration_page.select_gender(test_student.gender)
    registration_page.send_keys(element=registration_page.user_number_field, value=test_student.mobile)
    registration_page.set_date_of_birth(test_student.date_of_birth)
    registration_page.add_subjects(test_student.subjects)
    registration_page.select_hobbies_checkbox(test_student.hobbies)
    registration_page.upload_image(test_student.picture_file_name)
    registration_page.send_keys(element=registration_page.current_address_text_area, value=test_student.current_address)
    registration_page.select_state(test_student.state)
    registration_page.select_city(test_student.city)
    # Act
    registration_page.click(element=registration_page.submit_button)
    # Assert
    submit_modal = RegistrationSubmitModal(browser)
    submit_modal.assert_element_displayed(*submit_modal.modal_data)
    submit_modal.check_and_assert_title_displayed()
    expected_data_map = submit_modal.prepare_expected_data_map(student=test_student)
    submit_modal.check_and_assert_table_fields(expected_data_map)
