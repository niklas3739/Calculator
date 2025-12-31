import pytest
from app.services.calculator import add, subtract, multiply, divide, modulo

@pytest.mark.parametrize(
    "a,b,expected",
    [
        (1, 2, 3),
        (-1, 1, 0),
        (2.5, 0.5, 3.0),
        (0, 0, 0),
    ],
)
def test_add(a, b, expected):
    assert add(a, b) == expected

@pytest.mark.parametrize(
    "a,b,expected",
    [
        (5, 2, 3),
        (2, 5, -3),
        (-1, -1, 0),
    ],
)
def test_subtract(a, b, expected):
    assert subtract(a, b) == expected

@pytest.mark.parametrize(
    "a,b,expected",
    [
        (3, 4, 12),
        (-2, 3, -6),
        (2.5, 2, 5.0),
        (0, 10, 0),
    ],
)
def test_multiply(a, b, expected):
    assert multiply(a, b) == expected

@pytest.mark.parametrize(
    "a,b,expected",
    [
        (10, 2, 5),
        (-9, 3, -3),
        (5, 2, 2.5),
    ],
)
def test_divide(a, b, expected):
    assert divide(a, b) == expected

def test_divide_by_zero_raises():
    with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):
        divide(1, 0)


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (10, 2, 0),
        (-9, 2, 1),
        (5, 3, 2),
    ],
)
def test_modulo(a, b, expected):
    assert modulo(a, b) == expected

def test_divide_by_zero_raises():
    with pytest.raises(ZeroDivisionError, match="Cannot modulo by zero"):
        modulo(1, 0)
