# Given an array of integers nums and an integer target, 
# return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # Create a dictionary
        d = {}

        # step through the list
        for i in range(len(nums)):

            # If our target value is already in dict, return that index and the current index
            if target-nums[i] in d:
                return(i, d[target-nums[i]])

            # If the current value isnt in dictionary, add it
            if nums[i] not in d:
                d[nums[i]] = i


# Test cases
sol = Solution()
print(sol.twoSum([2,7,11,15], 9))
print(sol.twoSum([3,2,4], 6))
print(sol.twoSum([3,3], 6))