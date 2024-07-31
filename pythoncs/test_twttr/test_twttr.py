from twttr import shorten
import pytest
def test_twitter():
    assert shorten("twitter") == "twttr"
    assert shorten("post") == "pst"

def test_name():
    assert shorten("Alice") == "lc"
    assert shorten("George") == "Grg"

def test_number():
    assert shorten('1') == '1'

def test_punct():
    assert shorten("Dipak!") == "Dpk!"

def test_int():
    with pytest.raises(TypeError):
        shorten(1)
