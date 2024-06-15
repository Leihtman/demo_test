from ui_dataclasses.student_dataclass import Student, DateOfBirth
from ui_enums.hobbies_enum import HobbiesEnum
from ui_enums.month_enum import MonthEnum


class StudentGenerator:
    @staticmethod
    def get_success_full_student():
        return Student(
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
