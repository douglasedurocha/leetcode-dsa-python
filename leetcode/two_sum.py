from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    dc = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in dc:
            return [dc[complement], i]
        dc[nums[i]] = i
        
arr = [2,7,11,15]
target = 9
print(twoSum(arr, target))