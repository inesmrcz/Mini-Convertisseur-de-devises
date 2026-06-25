from app_functions import convert


def test_convert_eur_usd():
    rates = {"EUR": 1, "USD": 1.1}
    assert round(convert(10, "EUR", "USD", rates), 2) == 11.0


def test_convert_usd_eur():
    rates = {"EUR": 1, "USD": 1.1}
    assert round(convert(11, "USD", "EUR", rates), 2) == 10.0


def test_convert_same_currency():
    rates = {"EUR": 1, "USD": 1.1}
    assert convert(10, "EUR", "EUR", rates) == 10


def test_convert_negative():
    rates = {"EUR": 1, "USD": 1.1}
    assert convert(-5, "EUR", "USD", rates) is None


def test_convert_zero():
    rates = {"EUR": 1, "USD": 1.1}
    assert convert(0, "EUR", "USD", rates) is None
