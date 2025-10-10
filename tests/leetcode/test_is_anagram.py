import pytest
from src.leetcode.is_anagram import is_anagram

@pytest.mark.parametrize(
    "s,t,expected",
    [
        ("anagram", "nagaram", True),  # classic anagram case
        ("rat", "car", False),  # not anagrams
        ("", "", True),  # empty strings
        ("a", "a", True),  # single character, same
        ("a", "b", False),  # single character, different
        ("listen", "silent", True),  # longer anagrams
        ("hello", "world", False),  # different lengths
        ("abc", "bca", True),  # reordered characters
        ("aabb", "abab", True),  # repeated characters
        ("aabb", "abbb", False),  # different character counts
        ("", "a", False),  # one empty, one not
        ("a", "", False),  # one not empty, one empty
        ("abcdef", "fedcba", True),  # reverse order
        ("a", "aa", False),  # different lengths
        ("aa", "a", False),  # different lengths
        ("anagram", "anagram", True),  # identical strings
        ("123", "321", True),  # numbers as characters
        ("!@#", "#@!", True),  # special characters
        ("aA", "Aa", True),  # case sensitive (same case)
        ("a", "A", False),  # case sensitive (different case)
    ]
)
def test_is_anagram(s, t, expected):
    """
    Tests the `is_anagram` function across multiple scenarios:
    - classic anagram cases
    - edge cases with empty strings
    - single character comparisons
    - different length strings
    - repeated characters
    - case sensitivity
    - special characters and numbers
    """
    result = is_anagram(s, t)
    assert result == expected, f"Expected {expected} but got {result} for s='{s}' t='{t}'"
