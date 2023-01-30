from numb3rs import validate
import pytest

# def test_not_numeric():
#     assert validate("1.5.r.2") == False
#     assert validate("my is is 0.0.0.0") == False
#     assert validate("zero.zero.zero.zero") == False

# def test_correct_ip():
#     assert validate("0.0.0.0") == True
#     assert validate("255.255.255.255") == True
#     assert validate("66.25.7.0") == True

def test_range():
    assert validate(r"255.255.255.255") == True
    assert validate(r"999.255.255.255") == False
    assert validate(r"255.999.255.255") == False
    assert validate(r"255.255.999.255") == False
    assert validate(r"255.255.255.999") == False


def test_format():
    assert validate(r"1.2.3.4") == True
    assert validate(r"1.2.3") == False
    assert validate(r"1.2") == False
    assert validate(r"1") == False

# def test_first_part():
#     assert validate("0") == True
#     assert validate("255") == True
#     assert validate("700") == False

# def test_five_byte():
#     assert validate("0.0.0.0.0") == True
#     assert validate("5.5.5.5.5") == True