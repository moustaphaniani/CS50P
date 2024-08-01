import pytest
from fuel import convert, gauge

def main():
    test_fuel_errors()
    test_fuel_convert()
    test_fuel_gauge()


def test_fuel_errors():
    with pytest.raises(ValueError):
        convert("2/A")
    with pytest.raises(ValueError):
        convert("9/1")
    with pytest.raises(ValueError):
        convert("9/8")
    with pytest.raises(ValueError):
        convert("1?2")
    with pytest.raises(ValueError):
        convert("3,4")
    with pytest.raises(ValueError):
        convert("2.4")
    with pytest.raises(ZeroDivisionError):
        convert("5/0")


def test_fuel_convert():
    assert convert("1/1") == 100
    assert convert("99/100") == 99
    assert convert("0/1") == 0
    assert convert("1/100") == 1
    assert convert("2/4") == 50
    assert convert("1/4") == 25
    assert convert("3/4") == 75
    assert convert("4/4") == 100


def test_fuel_gauge():
    assert gauge(100) == "F"
    assert gauge(99) == "F"
    assert gauge(98) == "98%"
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(2) == "2%"
    assert gauge(50) == "50%"
    assert gauge(25) == "25%"
    assert gauge(75) == "75%"


if __name__ == "__main__":
    main()
