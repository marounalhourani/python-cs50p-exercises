from fuel import convert, gauge
import pytest

def test_ZeroDivisionError():
    with pytest.raises(ZeroDivisionError):
        convert("100/0")

def test_ValueError():
    with pytest.raises(ValueError):
        convert("cat/dog")

def test_convert():
    assert convert("50/100") == 50
    assert convert("1/100") == 1
    assert convert("99/100") == 99

def test_gauge():
    assert gauge(50) == "50%"
    assert gauge(100) =="F"
    assert gauge(1) =="E"
    assert gauge(99) == "F"