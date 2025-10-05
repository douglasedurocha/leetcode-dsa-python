import pytest
from src.dsa.binary_search import binary_search

@pytest.mark.parametrize(
    "arr, target, expected",
    [
        ([1, 2, 3, 4, 6], 6, 4),
        ([2, 3, 4, 5], 5, 3),
        ([1, 1, 3, 4, 8], 2, -1),
        ([], 5, -1),
        ([1], 1, 0),
        ([1], 0, -1),
    ]
)
def test_binary_search(arr, target, expected):
    """
    """
    result = binary_search(arr, target)
    assert result == expected, f"Expected {expected} but got {result} for arr={arr} target={target}"