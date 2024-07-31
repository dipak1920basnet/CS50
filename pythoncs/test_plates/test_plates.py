from plates import is_valid

def test_check_len():
    assert is_valid("a") == False
    assert is_valid("1") == False
    assert is_valid("umbrellas") == False
    assert is_valid("a1") == False
    assert is_valid("0a") == False
    assert is_valid("1a") == False
    assert is_valid("11") == False
    assert is_valid("01") == False

def test_check_plate():
    assert is_valid("CS05") == False
    assert is_valid("CS50") == True
    assert is_valid("CS50P") == False
    assert is_valid("PI3.14") == False
    assert is_valid("H") == False
    assert is_valid("OUTATIME") == False
