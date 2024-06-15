from enum import Enum

from ui_dataclasses.hobby_dataclass import Hobby


class HobbiesEnum(Enum):
    SPORTS = Hobby(number=1, name="Sports")
    READING = Hobby(number=2, name="Reading")
    MUSIC = Hobby(number=3, name="Music")
