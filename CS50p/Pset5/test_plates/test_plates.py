from plates import is_valid

def test():
    assert is_valid("au05") == False
    assert is_valid("ng103") == True
    assert is_valid("ng14k") == False
    assert is_valid("Pu5.15") == False
    assert is_valid("L") == False
    assert is_valid("ABCDEFGH") == False
    assert is_valid("12456") == False
