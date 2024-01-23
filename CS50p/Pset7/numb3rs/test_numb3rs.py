from numb3rs import validate

def test():
    assert validate("255.255.255.255") == True
    assert validate("512.512.512.512") == False
    assert validate("1.2.3.1000") == False
    assert validate("cat") == False
    assert validate("125.145.23.14.25") == False
    assert validate("hg.12.14.156") == False
    assert validate("14.152.24") == False
    assert validate("289.152.2.4") == False
    assert validate("14.456.24.23") == False
