import pytest
from working import convert


def test_convert():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("8 PM to 8 AM") == "20:00 to 08:00"
    assert convert("8:00 PM to 8:00 AM") == "20:00 to 08:00"
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"


def test_value_error():
    with pytest.raises(ValueError):
        convert("8:60 AM - 4:60 PM")
    with pytest.raises(ValueError):
        convert("9AM - 5PM")
    with pytest.raises(ValueError):
        convert("09:00 to 17:00")
    with pytest.raises(ValueError):
        convert("9 AM - 35 PM")
    with pytest.raises(ValueError):
        convert("17:07 AM - 45:10 PM")
    with pytest.raises(ValueError):
        convert("23:00 AM to 27:00 PM")

