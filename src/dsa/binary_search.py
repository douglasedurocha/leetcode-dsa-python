from typing import List

# Consider the arr is sorted
def binary_search(arr: List, target: int):
    lo, hi = 0, len(arr)
    
    while (lo < hi):
        mid = (lo + hi) // 2
        v = arr[mid]
        
        if (v == target):
            return mid
        elif (v < target):
            lo = mid + 1
        else:
            hi = mid
            
    return -1