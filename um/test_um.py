from um import count
import pytest

def test_case_ins():
    assert count("Um um") == 2
    assert count("um UM Um") == 3

def test_with_char():
    assert count("um, is cool") == 1
    assert count("Um?") == 1

def test_inside_words():
    assert count("ummmmm yummy") == 0

