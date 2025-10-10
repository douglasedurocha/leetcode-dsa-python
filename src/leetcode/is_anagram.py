def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    
    s_countmap = {}
    t_countmap = {}
    
    for i in range(len(s)):
        s_countmap[s[i]] = s_countmap.get(s[i], 0) + 1
        t_countmap[t[i]] = t_countmap.get(t[i], 0) + 1
        
    return s_countmap == t_countmap