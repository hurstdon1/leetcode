# Given an integer array nums, return true if any value appears at least twice in the array, 
# and return false if every element is distinct.

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = {}

        for val in nums:

            if val not in d:
                d[val] = 1

            else:
                return True

        return False






# Example 1:

# Input: nums = [1,2,3,1]
# Output: true
# Example 2:

# Input: nums = [1,2,3,4]
# Output: false
# Example 3:

# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true

sol = Solution()
print(sol.containsDuplicate([1,2,3,1]))
print(sol.containsDuplicate([1,2,3,4]))
print(sol.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))