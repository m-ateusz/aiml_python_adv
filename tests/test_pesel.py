import pytest

from testing.pesel import Pesel
from datetime import date

from unittest.mock import Mock

def test_22():
    assert Pesel('22222222222').birthday == date(2022, 2, 22)

def test_11():
    assert Pesel('11111111111').birthday == date(1911, 11, 11)

def test_23():
    api = Mock()
    api.test.return_value = 200
    assert api.test() == 200


