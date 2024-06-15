from dataclasses import dataclass
from typing import Optional

from ui_enums.month_enum import MonthEnum


@dataclass
class DateOfBirth:
    day: int
    month: MonthEnum
    year: int


@dataclass
class Student:
    first_name: str
    last_name: str
    email: Optional[str]
    gender: str
    mobile: int
    date_of_birth: DateOfBirth
    subjects: Optional[list]
    hobbies: Optional[list]
    picture_file_name: Optional[str]
    current_address: str
    state: str
    city: str
