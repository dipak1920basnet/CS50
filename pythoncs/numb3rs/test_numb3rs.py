from numb3rs import validate
import pytest


def test_dot():
    assert validate("255.8.8") == False
    assert validate("988.66.12.33.4") == False


def test_range():
    assert validate("-2.23.8.6") == False
    assert validate("0.264.447.9") == False
    assert validate("127.0.0.9") == True


# def test_value_error():
#     with pytest.raises(ValueError):
#         validate("12.cat.hello.9")
