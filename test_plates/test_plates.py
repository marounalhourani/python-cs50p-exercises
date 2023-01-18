from plates import is_valid

def test_len():
    assert is_valid("d") == False
    assert is_valid("marounhourani") == False
    assert is_valid("maro") == True

def test_first_2_char():
    assert is_valid("24maro") == False
    assert is_valid("1hi") == False
    assert is_valid("b2hi") == False
    assert is_valid("CS50") == True

def test_punctuation():
    assert is_valid("hi hi") == False
    assert is_valid("Hello!") == False
    assert is_valid("Hello") == True

def test_numbers():
    assert is_valid("CS05") == False
    assert is_valid("CS50p") == False
    assert is_valid("CS2020") == True

def test_not_beginning_alpha():
    assert is_valid("50") == False
    assert is_valid("9tou") == False
    assert is_valid("m6here") == False

