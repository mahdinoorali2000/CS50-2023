from twttr import shorten

def test():
    assert shorten("hello") == "hll"
    assert shorten("aioue") == ""
    assert shorten("AIOUE") == ""
    assert shorten("hello, how are you? ") == "hll, hw r y? "
    assert shorten("142586") == "142586"
