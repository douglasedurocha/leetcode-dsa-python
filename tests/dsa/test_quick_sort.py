import pytest
from src.dsa.quick_sort import quick_sort

@pytest.mark.parametrize(
    "arr, expected",
    [
        ([], []),
        ([1], [1]),
        ([1, 2, 3], [1, 2, 3]),
        ([3, 2, 1], [1, 2, 3]),
        ([5, 1, 3, 2, 4], [1, 2, 3, 4, 5]),
        ([2, 2, 2], [2, 2, 2]),
        ([9, 3, 7, 4, 69, 420, 42], [3, 4, 7, 9, 42, 69, 420]),
        ([4, 2, 5, 2, 3], [2, 2, 3, 4, 5]),
        ([-1, -3, 0, 2], [-3, -1, 0, 2]),
    ],
)
def test_quick_sort(arr, expected):
    """
    Tests the `quick_sort` function with various arrays, covering a variety of scenarios
    including normal cases, edge cases, duplicates, empty arrays, and no-match situations.
    """
    result = quick_sort(arr)
    assert result == expected, f"Expected {expected} but got {result} for arr={arr}"