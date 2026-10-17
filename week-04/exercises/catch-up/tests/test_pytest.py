"""The same calculator behaviour in pytest's parameterised style."""
import pytest
from calculator import add, subtract, divide


@pytest.mark.parametrize('first,second,expected', [(1, 1, 2), (1, 2, 3), (-2, 2, 0)])
def test_add(first, second, expected):
    assert add(first, second) == expected


def test_subtract():
    assert subtract(7, 2) == 5


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)
