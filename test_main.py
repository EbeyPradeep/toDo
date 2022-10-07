import pytest

from main import add_numbers

test_cases = [(1, 3, 4), (3, 4, 7), (3, 5, 8), (4, 2, 6)]


@pytest.mark.parametrize("a,b, expected_result", test_cases)
def test_add_numbers(a, b, expected_result):
    assert add_numbers(a, b) == {"result": expected_result}

@pytest.mark.parametrize("a,b, expected_result", test_cases)
def test_add_numbers(a, b, expected_result):
    assert add_numbers(a, b) == {"result": expected_result}




