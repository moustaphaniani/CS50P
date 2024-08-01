# reimplement Setting up my twttr from Problem Set 2, restructuring your code per the below, wherein
# shorten expects a str as input and returns that same str but with all vowels (A, E, I, O, and U) omitted,
# whether inputted in uppercase or lowercase.
# Then, in a file called test_twttr.py, implement one or more functions that collectively test your
# implementation of shorten thoroughly, each of whose names should begin with test_ so that you can
# execute your tests with: pytest test_twttr.py

import pytest
from twttr import shorten

def main():
    test_twttr_lowcase()
    test_twttr_upercase()
    test_twttr_mixedcase()
    test_twttr_vowels()
    test_twttr_mixedcase()
    test_twttr_numbers()
    test_twttr_punctuation()


def test_twttr_lowcase():
    assert shorten("carlos") == "crls"


def test_twttr_upercase():
    assert shorten("CARLOS") == "CRLS"


def test_twttr_mixedcase():
    assert shorten("Carlos") == "Crls"


def test_twttr_vowels():
    assert shorten("aeiou") == ""
    assert shorten("AEIOU") == ""


def test_twttr_numbers():
    assert shorten("123") == "123"


def test_twttr_punctuation():
    assert shorten("!?") == "!?"


if __name__ == "__main__":
    main()
