import pytest
from dsa.two_pointers import two_pointers

@pytest.mark.parametrize(
    "arr,target,expected",
    [
        ([1, 2, 3, 4, 6], 6, [2, 4]),
        ([2, 3, 4, 5], 9, [4, 5]),
        ([1, 2, 3], 7, []),
        ([], 5, []),
        ([5, 25, 75], 100, [25, 75]),
        ([1, 1, 1, 2, 3], 4, [1, 3]),
        ([1, 2, 4, 4], 8, [4, 4]),
    ]
)
def test_two_pointers(arr, target, expected):
    """
    Tests the `two_pointers` function with sorted arrays, covering a variety of scenarios 
    including normal cases, edge cases, duplicates, empty arrays, and no-match situations.
    """
    result = two_pointers(arr, target)
    assert result == expected, f"Expected {expected} but got {result} for arr={arr} target={target}"
