from pages.base_page import BasePage
from ui_dataclasses.student_dataclass import Student


class RegistrationSubmitModal(BasePage):
    header_title_xpath_str = "//div[@class='modal-title h4']"
    table_field_pattern = "//tr/td[text()='{field_name}']/following-sibling::td"

    @staticmethod
    def prepare_expected_data_map(student: Student):
        data_map = {
            "Student Name": f"{student.first_name} {student.last_name}",
            "Student Email": student.email,
            "Gender": student.gender,
            "Mobile": str(student.mobile),
            "Date of Birth": f"{student.date_of_birth.day:02} {student.date_of_birth.month.value.name},{student.date_of_birth.year}",
            "Subjects": f", ".join(student.subjects),
            "Hobbies": f", ".join([hobby.value.name for hobby in student.hobbies]),
            "Picture": student.picture_file_name,
            "Address": student.current_address,
            "State and City": f"{student.state} {student.city}",
        }
        return data_map

    def check_and_assert_table_fields(self, table_data_expected: dict):
        for field_name, expected_value in table_data_expected.items():
            field_xpath_str = self.table_field_pattern.format(field_name=field_name)
            self.get_text_and_assert_by_xpath(field_xpath_str, expected_value)
