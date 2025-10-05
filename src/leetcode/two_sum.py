from typing import List

def two_sum(nums: List[int], target: int) -> List[int]:
    dc = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in dc:
            return [dc[complement], i]
        dc[nums[i]] = i
