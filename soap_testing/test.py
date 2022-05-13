import pytest


def test_add(calculator):
    result = calculator.add(5, 6)
    assert result == 11


def test_subtract(calculator):
    result = calculator.subtract(20, 6)
    assert result == 14


def test_divide(calculator):
    result = calculator.divide(10, 5)
    assert result == 2


def test_multiply(calculator):
    result = calculator.multiply(8, 6)
    assert result == 48


def test_divide_by_zero(calculator):
    with pytest.raises(Exception):
        calculator.divide(1, 0)
