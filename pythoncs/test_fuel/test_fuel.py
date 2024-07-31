from fuel import convert, gauge

import pytest

def test_convert():
    assert convert('3/4') == 75
    assert convert('1/3') == 33
    assert convert('0/100') == 0
    assert convert('2/3') == 67
    assert convert('99/100') == 99


def test_gauge():
    assert gauge(75) == "75%"
    assert gauge(33) == "33%"
    assert gauge(67) == "67%"
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(99) == "F"

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert('100/0')
        convert('0/0')
        convert('1/0')

def test_value_error():
    with pytest.raises(ValueError):
        convert("2/1")

