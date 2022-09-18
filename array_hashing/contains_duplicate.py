# Given an integer array nums, return true if any value appears at least twice in the array, 
# and return false if every element is distinct.

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Instantiate a dictionary
        d = {}

        # Loop over the list of numbers. Return true if any appears more than once
        for val in nums:

            if val not in d:
                d[val] = 1

            else:
                return True

        return False


# Test Cases
sol = Solution()
print(sol.containsDuplicate([1,2,3,1]))
print(sol.containsDuplicate([1,2,3,4]))
print(sol.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))