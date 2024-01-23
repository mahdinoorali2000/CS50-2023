from fuel import convert, gauge
import pytest

def test_convert():
    assert convert("1/4") == 25
    assert convert("10/10") == 100

    with pytest.raises(ValueError):
        convert("y/o")

    with pytest.raises(ZeroDivisionError):
        convert("8/0")

def test_gauge():
    assert gauge(99) == "F"
    assert gauge(1) == "E"
    assert gauge(54) == "54%"


