import pytest
from numb3rs import validate

def main():
    test_error_quantity()
    test_error_values()
    test_right()


def test_error_quantity():
    assert validate('0') == False
    assert validate('0.0') == False
    assert validate('0.0.0') == False
    assert validate('0.0.0.0.0') == False
    assert validate('0.0.0.0.0.0') == False


def test_error_values():
    assert validate('-1.0.0.0') == False
    assert validate('0.260.0.0') == False
    assert validate('0.0.0.999') == False
    assert validate('0.0.0.-1') == False


def test_right():
    assert validate('0.0.0.0') == True
    assert validate('255.255.255.255') == True
    assert validate('198.166.0.100') == True


if __name__ == "__main__":
    main()
