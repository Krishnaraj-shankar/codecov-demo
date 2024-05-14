from .calculator import Calculator

calc = Calculator()


def test_add():
    assert calc.add(1, 2) == 3.0
    assert calc.add(1.0, 2.0) == 3.0
    assert calc.add(0, 2.0) == 2.0
    assert calc.add(2.0, 0) == 2.0
    assert calc.add(-4, 2.0) == -2.0

def test_subtract():
    assert calc.subtract(1, 2) == -1.0
    assert calc.subtract(2, 1) == 1.0
    assert calc.subtract(1.0, 2.0) == -1.0
    assert calc.subtract(0, 2.0) == -2.0
    assert calc.subtract(2.0, 0.0) == 2.0
    assert calc.subtract(-4, 2.0) == -6.0

def test_multiply():
    assert calc.multiply(1, 2) == 2.0
    assert calc.multiply(1.0, 2.0) == 2.0
    assert calc.multiply(0, 2.0) == 0.0
    assert calc.multiply(2.0, 0.0) == 0.0
    assert calc.multiply(-4, 2.0) == -8.0

def test_divide():
    assert calc.divide(1, 2) == 0.5
    assert calc.divide(1.0, 2.0) == 0.5
    assert calc.divide(0, 2.0) == 0
    assert calc.divide(-4, 2.0) == -2.0