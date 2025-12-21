from dataclasses import dataclass, field
from datetime import date
from enum import IntEnum
import re

PESEL_RE = re.compile(r'^\d{11}$')
DATA_RE = re.compile(r'^(\d\d)(\d\d)(\d\d).*')
class GENDER(IntEnum):
    MALE = 0
    FEMALE = 1

@dataclass
class Pesel:
    number: str
    birthday: date = field(init=False)
    gender: GENDER = field(init=False)

    def __post_init__(self):
        if not re.match(PESEL_RE, self.number):
            raise ValueError("Invalid PESEL number")

        match = re.match(DATA_RE, self.number)
        y,m,d = [int(i) for i in match.groups()]

        match m:
            case M if M<20:
                y += 1900
            case M if M<40:
                y += 2000
            case M if M<60:
                y += 2100
            case M if M<80:
                y += 2200
            case _:
                y += 1800
        m %= 20

        print(f'{y=} {m=} {d=}')
        self.birthday = date(y, m, d)
