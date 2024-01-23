from bank import value

def test():
    assert value("hello") == 0
    assert value("Hello") == 0
    assert value("hi") == 20
    assert value("Hi") == 20
    assert value("you'r wellcome") == 100
