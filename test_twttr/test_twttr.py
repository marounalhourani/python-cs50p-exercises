from twttr import shorten

def test_lower_case():
    assert shorten("maroun") == "mrn"
    assert shorten("hello world") == "hll wrld"
    assert shorten("hair cut") == "hr ct"

def test_upper_case():
    assert shorten("MArUn") == "Mrn"
    assert shorten("AOU") == ""
    assert shorten("GOOD GAME") == "GD GM"

def test_with_numb():
    assert shorten("Hello024") == "Hll024"
    assert shorten("024") == "024"

def test_no_input():
    assert shorten("") == ""

def test_punctuation():
    assert shorten("hello, my name is: ") == "hll, my nm s: "