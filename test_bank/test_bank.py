from bank import value

def test_entire_phrase():
    assert value("hello my name is") == 0
    assert value("Hello there") == 0
    assert value("hey, ny name is: ") == 20

def test_case_insensitivity():
    assert value("hello") == 0
    assert value("HELLO") == 0

def test_incorrect():
    assert value("maroun") == 100

# returns 0 if that str starts with “hello”,
# 20 if that str starts with an “h” (but not “hello”),
# or 100 otherwise, treating the str case-insensitively.
# You can assume that the string passed to the value function will not contain any leading spaces.
#  Only main should call print.