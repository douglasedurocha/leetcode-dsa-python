import pytest
from src.leetcode.group_anagrams import group_anagrams

@pytest.mark.parametrize(
    "strs,expected",
    [
        (["eat", "tea", "tan", "ate", "nat", "bat"], [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]),  # classic case
        ([""], [[""]]),  # single empty string
        (["a"], [["a"]]),  # single character
        (["abc", "bca", "cab"], [["abc", "bca", "cab"]]),  # all anagrams
        (["abc", "def", "ghi"], [["abc"], ["def"], ["ghi"]]),  # no anagrams
        (["listen", "silent", "enlist"], [["listen", "silent", "enlist"]]),  # longer anagrams
        (["a", "a", "a"], [["a", "a", "a"]]),  # all same strings
        (["", "", ""], [["", "", ""]]),  # multiple empty strings
        ([], []),  # empty input
        (["a", "b", "c"], [["a"], ["b"], ["c"]]),  # single characters, no anagrams
        (["ab", "ba", "abc", "bca"], [["ab", "ba"], ["abc", "bca"]]),  # mixed lengths
    ]
)
def test_group_anagrams(strs, expected):
    """
    Tests the `group_anagrams` function across multiple scenarios:
    - normal anagram grouping
    - empty and single-element inputs
    - edge cases with empty strings
    - cases with no anagrams
    - cases with all anagrams
    - mixed length strings
    """
    result = group_anagrams(strs)
    
    # Sort each group and the overall result for comparison
    result_sorted = [sorted(group) for group in result]
    expected_sorted = [sorted(group) for group in expected]
    
    # Sort the list of groups to handle different ordering
    result_sorted.sort()
    expected_sorted.sort()
    
    assert result_sorted == expected_sorted, f"Expected {expected_sorted} but got {result_sorted} for strs={strs}"
