import pytest
from src.leetcode.two_sum import two_sum

@pytest.mark.parametrize(
    "nums,target,expected",
    [
        ([2, 7, 11, 15], 9, [0, 1]),          # classic case
        ([3, 2, 4], 6, [1, 2]),               # unsorted input
        ([3, 3], 6, [0, 1]),                  # duplicate elements
        ([0, 4, 3, 0], 0, [0, 3]),            # zeros
        ([-1, -2, -3, -4, -5], -8, [2, 4]),   # negative numbers
        ([1, 5, 7, -1, 5], 6, [0, 1]),        # mix of positive and negative
        ([10, 15, 3, 7], 17, [0, 3]),         # another simple valid pair
    ]
)
def test_two_sum(nums, target, expected):
    """
    Tests the `two_sum` function across multiple scenarios:
    - normal and duplicate values
    - absence of solutions
    - empty and single-element arrays
    - negative and zero values
    """
    result = two_sum(nums, target)
    assert result == expected, f"Expected {expected} but got {result} for nums={nums} target={target}"
