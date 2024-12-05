import pytest
from main import factorial

def test_factorial_positive():
    assert factorial(5) == 120
    assert factorial(0) == 1

def test_factorial_negative():
    with pytest.raises(ValueError):
        factorial(-1)
