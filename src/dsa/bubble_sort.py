# Complexity: O (N^2)

from typing import List

def bubble(arr: List[int]) -> List[int]:
    for i in range(len(arr)):
        for j in range(len(arr) - (i + 1)):
            if arr[j] > arr[j + 1]:
                # switch
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr