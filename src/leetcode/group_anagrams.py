from typing import List

def group_anagrams(strs: List[str]) -> List[List[str]]:
    anagram_map = {}
    for s in strs:
        s_sorted = "".join(sorted(s))
        anagram_map[s_sorted] = anagram_map.get(s_sorted, []) + [s]
    return list(anagram_map.values())