import pytest
from datetime import datetime, timedelta

def test_date_operations():
    """Test basic date operations"""
    today = datetime.now()
    tomorrow = today + timedelta(days=1)
    assert tomorrow > today

def test_string_operations():
    """Test string manipulation"""
    text = "Hello, World!"
    assert text.upper() == "HELLO, WORLD!"
    assert text.split(',')[0] == "Hello"

@pytest.mark.parametrize("test_input,expected", [
    ("3+5", 8),
    ("2+4", 6),
    ("6+9", 15),
])
def test_eval(test_input, expected):
    """Test basic arithmetic operations"""
    assert eval(test_input) == expected

def test_list_operations():
    """Test list operations"""
    numbers = [1, 2, 3, 4, 5]
    assert len(numbers) == 5
    assert sum(numbers) == 15
    assert max(numbers) == 5

@pytest.mark.slow
def test_large_operation():
    """Test with large numbers"""
    result = sum(range(1000000))
    assert result == 499999500000
