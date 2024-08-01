import pytest
from plates import is_valid

def main():
    test_plates_1()
    test_plates_2()
    test_plates_3()
    test_plates_4()
    test_plates_5()


def test_plates_1():
    assert is_valid("CA1") == True
    assert is_valid("AAA222") == True


def test_plates_2():
    assert is_valid("ca1") == True
    assert is_valid("aaa222") == True


def test_plates_3():
    assert is_valid("1a") == False
    assert is_valid("a1a") == False
    assert is_valid("aa22aa") == False


def test_plates_4():
    assert is_valid("a") == False
    assert is_valid("A") == False
    assert is_valid("1") == False
    assert is_valid("abcdefg") == False
    assert is_valid("ABCDEFG") == False
    assert is_valid("1234567") == False
    assert is_valid("ABCD1234") == False


def test_plates_5():
    assert is_valid("AB01") == False
    assert is_valid("AB1") == True
    assert is_valid("123") == False
    assert is_valid("12AB") == False
    assert is_valid("1A2B") == False
    assert is_valid("A1B2C3") == False
    assert is_valid("AB.12") == False
    assert is_valid("AB12.") == False
    assert is_valid("AB 12") == False
    assert is_valid("AB12 ") == False
    assert is_valid("AB!12") == False
    assert is_valid("AB12!") == False
