import pytest
from pydantic import ValidationError

from calculator import Calculator


def test_addition():
    result = Calculator(
        input_1=1,
        input_2=2,
        action='1'
    ).perform()
    assert result == 1 + 2


def test_subtract():
    result = Calculator(
        input_1=1,
        input_2=2,
        action='2'
    ).perform()
    assert result == 1 - 2


def test_multiply():
    result = Calculator(
        input_1=1,
        input_2=2,
        action='3'
    ).perform()
    assert result == 1 * 2


def test_divide():
    result = Calculator(
        input_1=1,
        input_2=2,
        action='4'
    ).perform()
    assert result == 1 / 2


def test_invalid_action():
    with pytest.raises(KeyError):
        Calculator(
            input_1=1,
            input_2=2,
            action='8'
        ).perform()


def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        Calculator(
            input_1=1,
            input_2=0,
            action='4'
        ).perform()


def test_pydantic_errors():
    with pytest.raises(ValidationError):
        Calculator(
            input_1='a',
            input_2=2,
            action='1'
        ).perform()