import pytest

from testing.pesel import Pesel, GENDER
from datetime import date

from unittest.mock import Mock

@pytest.mark.parametrize(
   "pesel, bdate",
   [('22222222222', date(2022, 2, 22)),
    ('11111111111', date(1911, 11, 11)),
    ('80080811111', date(1980, 8, 8))]
)
def test_birthday(pesel, bdate):
    assert Pesel(pesel).birthday == bdate

# def test_11():
#     assert Pesel('11111111111').birthday == date(1911, 11, 11)

def test_gender():
    assert Pesel('11111111111').gender is not GENDER.FEMALE

class Checker:
    def check(self, code):
        if code == 200:
            result = 'OK'
        else:
            result = 'Error'
        return result

def test_ok():
    api = Mock()
    api.test.return_value = 200

    result = Checker().check(api.test())
    assert result == 'OK'


def test_error():
    api = Mock()
    api.test.return_value = 300

    result = Checker().check(api.test())
    assert 'ERROR' == result