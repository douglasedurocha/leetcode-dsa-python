import pytest
from src.leetcode.contains_duplicate import contains_duplicate

@pytest.mark.parametrize(
    "nums,expected",
    [
        ([1, 2, 3, 1], True),  # Contains duplicate
        ([1, 2, 3, 4], False),  # No duplicates
        ([], False),  # Empty array
        ([1], False),  # Single element
        ([1, 1], True),  # Two identical elements
        ([-1, -1], True),  # Negative duplicates
        ([0, 0], True),  # Zero duplicates
    ]
)
def test_contains_duplicate(nums, expected):
    """
    Tests the `contains_duplicate` function across multiple scenarios:
    - normal and duplicate values
    - empty and single-element arrays
    - negative and zero values
    """
    result = contains_duplicate(nums)
    assert result == expected, f"Expected {expected} but got {result} for nums={nums}"
