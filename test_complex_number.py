import pytest
from complex_number import ComplexNumber


def test_complex_number_creation():
    num = ComplexNumber(1, 2)
    assert num.real == 1
    assert num.imaginary == 2


def test_complex_number_str():
    num1 = ComplexNumber(1, 2)
    num2 = ComplexNumber(-1, -2)
    num3 = ComplexNumber(1, -2)
    num4 = ComplexNumber(-1, 2)
    assert str(num1) == "1 + 2i"
    assert str(num2) == "-1 - 2i"
    assert str(num3) == "1 - 2i"
    assert str(num4) == "-1 + 2i"


def test_complex_number_add():
    num1 = ComplexNumber(1, 2)
    num2 = ComplexNumber(3, 4)
    num3 = num1 + num2
    assert num3.real == 4
    assert num3.imaginary == 6
