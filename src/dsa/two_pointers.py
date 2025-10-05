from typing import List

# Consider the arr is sorted
def two_pointers(arr: List[int], target: int) -> List[int]:
    lo, hi = 0, len(arr) - 1

    while lo < hi:
        result = arr[lo] + arr[hi]

        if (result == target):
            return [arr[lo], arr[hi]]
        if (result < target):
            lo += 1
        else:
            hi -= 1

    return []
