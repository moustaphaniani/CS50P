import pytest
from seasons import calculate

def main():
    test_errors()
    test_ok()
    test_cs50()


def test_errors():
    with pytest.raises(SystemExit):
        calculate("20240101")
    with pytest.raises(SystemExit):
        calculate("01-01-2024")
    with pytest.raises(SystemExit):
        calculate("2024-12-31")
    with pytest.raises(SystemExit):
        calculate("January 1st, 2024")


def test_ok():
    assert calculate("2024-07-01") == 'forty-one thousand, seven hundred sixty'
    assert calculate("2024-07-29") == 'one thousand, four hundred forty'


def test_cs50():
    assert calculate("2023-07-31") == 'five hundred twenty-five thousand, six hundred'
    assert calculate("2022-07-31") == 'one million, fifty-one thousand, two hundred'

if __name__ == "__main__":
    main()
