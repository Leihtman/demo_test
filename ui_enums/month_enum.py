from enum import Enum

from ui_dataclasses.month_dataclass import Month


class MonthEnum(Enum):
    JANUARY = Month(number=0, name="January")
    FEBRUARY = Month(number=1, name="February")
    MARCH = Month(number=2, name="March")
    APRIL = Month(number=3, name="April")
    MAY = Month(number=4, name="May")
    JUNE = Month(number=5, name="June")
    JULY = Month(number=6, name="July")
    AUGUST = Month(number=7, name="August")
    SEPTEMBER = Month(number=8, name="September")
    OCTOBER = Month(number=9, name="October")
    NOVEMBER = Month(number=10, name="November")
    DECEMBER = Month(number=11, name="December")
