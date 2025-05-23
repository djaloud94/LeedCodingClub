"""
*leetcode.py contains
"""
from typing import List
class LeetCode:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)): # Browse the table from 0 to the size of the list
            for j in range(i+1, len(nums)): 
                if j<len(nums): # we must not exceed the size of the list
                   if nums[i]+nums[j] == target:
                      return [i,j]