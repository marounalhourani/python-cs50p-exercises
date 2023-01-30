from working import convert
import pytest
from contextlib import nullcontext as does_not_raise

def test_AM():
    assert convert("9 AM to 11 AM") == "09:00 to 11:00"
    assert convert("9:20 AM to 11:20 AM") == "09:20 to 11:20"

def test_PM():
    assert convert("9 PM to 10 PM") == "21:00 to 22:00"
    assert convert("8:30 PM to 10:20 PM") == "20:30 to 22:20"

def test_12():
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"

def test_error():
    with pytest.raises(ValueError):
        convert("13 AM to 2 PM")
        convert("nothing")
        convert("")
        convert("5AM to 8PM")
        convert("5 AM 8 PM")
        convert("22 AM 24 AM")

def test_format():
    with pytest.raises(ValueError):
        convert("8 AM - 10 PM")

def test_time():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"
    assert convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"

def test_wrong_hour():
    with pytest.raises(ValueError):
        convert("22 PM to 15 AM")

def test_wrong_min():
   with pytest.raises(ValueError):
        convert("2:77 PM to 10:24 AM")

