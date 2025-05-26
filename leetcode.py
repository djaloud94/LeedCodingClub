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
                   
    def isPalindrome(self, x: int) -> bool:
        if x<0:
           return False
        first = x
        reserved_number = 0
        while x>0:
            reste = x%10
            reserved_number = reserved_number*10+reste
            x = x//10
        return first == reserved_number

   