from jar import Jar
import pytest

def test_init():
    jar = Jar(25, 10)
    assert jar.capacity == 25
    assert jar.size == 10

    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar1 =Jar()
    jar2 = Jar(15)

    assert jar1.capacity == 12
    assert jar2.capacity == 15

    with pytest.raises(ValueError):
        test = jar1.deposit(15)
    with pytest.raises(ValueError):
        test = jar2.deposit(16)




def test_withdraw():
    jar1 =Jar()
    jar2 = Jar(15,5)

    assert jar1.size == 0
    assert jar2.size == 5

    with pytest.raises(ValueError):
        test = jar1.withdraw(15)
    with pytest.raises(ValueError):
        test = jar2.withdraw(16)
