import pytest
from src.dsa.bubble_sort import bubble


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([], []),
        ([1], [1]),
        ([1, 2, 3], [1, 2, 3]),
        ([3, 2, 1], [1, 2, 3]),
        ([5, 1, 3, 2, 4], [1, 2, 3, 4, 5]),
        ([2, 2, 2], [2, 2, 2]),
        ([4, 2, 5, 2, 3], [2, 2, 3, 4, 5]),
        ([-1, -3, 0, 2], [-3, -1, 0, 2]),
    ],
)
def test_bubble_sort(arr, expected):
    """
    Tests the `bubble` function with various arrays, covering a variety of scenarios
    including normal cases, edge cases, duplicates, empty arrays, and no-match situations.
    """
    result = bubble(arr)
    assert result == expected, f"Expected {expected} but got {result} for arr={arr}"
