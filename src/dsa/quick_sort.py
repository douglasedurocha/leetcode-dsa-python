# Complexity: O (N log N)

from typing import List

def qs(arr: List[int], lo: int, hi: int):
    if lo >= hi:
        return
    
    pivot = partition(arr, lo, hi)
    
    # weak sort left side
    qs(arr, lo, pivot - 1)
    # weak sort right side
    qs(arr, pivot + 1, hi)

def partition(arr: List[int], lo: int, hi: int) -> int:
    pivot = arr[hi]
    
    idx = lo - 1
    
    for i in range(lo, hi):
        if arr[i] <= pivot:
            idx += 1
            arr[i], arr[idx] = arr[idx], arr[i]
            
    idx += 1
    arr[hi] = arr[idx]
    arr[idx] = pivot
    
    return idx

# Complexity: O (n log n)
def quick_sort(arr: List[int]) -> List[int]:
    qs(arr, 0, len(arr) - 1)
    return arr