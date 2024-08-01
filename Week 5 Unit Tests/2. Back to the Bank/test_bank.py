import pytest
from bank import value

def main():
    test_bank_letter_hello()
    test_bank_letter_h()
    test_bank_letters()
    test_bank_numbers()
    test_bank_punctuation()

def test_bank_letter_hello():
    assert value("hello") == 0


def test_bank_letter_h():
    assert value("Hi") == 20


def test_bank_letters():
    assert value("Carlos") == 100


def test_bank_numbers():
    assert value("123") == 100


def test_bank_punctuation():
    assert value("+++") == 100


if __name__ == "__main__":
    main()
