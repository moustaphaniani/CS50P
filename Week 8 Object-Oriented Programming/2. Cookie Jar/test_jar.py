import pytest
from jar import Jar

def main():
    test_init()
    test_str()
    test_deposit()
    test_withdraw()


def test_init():
    jar = Jar(180, 10)
    assert jar.capacity == 180
    assert jar.size == 10


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    assert jar.deposit(1) == 1
    assert jar.deposit(1) == 2
    with pytest.raises(ValueError):
        jar.deposit(-2)
    assert jar.deposit(2) == 4
    assert jar.deposit(4) == 8
    assert jar.deposit(4) == 12
    with pytest.raises(ValueError):
        jar.deposit(1)


def test_withdraw():
    jar = Jar()
    assert jar.deposit(12) == 12
    assert jar.withdraw(1) == 11
    assert jar.withdraw(1) == 10
    with pytest.raises(ValueError):
        jar.withdraw(-2)
    assert jar.withdraw(2) == 8
    assert jar.withdraw(4) == 4
    assert jar.withdraw(4) == 0
    with pytest.raises(ValueError):
        jar.withdraw(1)


if __name__ == "__main__":
    main()
