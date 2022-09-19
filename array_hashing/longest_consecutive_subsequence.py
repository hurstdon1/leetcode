# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.

from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # turn the list/array into a set
        nums = set(nums)
        
        # Create a variable for the best streak
        best = 0
        
        # step through the nums set
        for x in nums:
            
            # Check if we are at the start of a sequence
            if x - 1 not in nums:
                
                # add 1 to our value if we are at the start of a sequence
                y = x + 1
                
                # While the y value is in our set
                while y in nums:
                    
                    # Add 1 to y
                    y += 1
                    
                    # maximum sequence is the max between the current best and current value minus start of sequence
                    best = max(best, y - x)
        
        # return the longest sequence
        return best

# Test Cases
sol = Solution()
print(sol.longestConsecutive([100,4,200,1,3,2]))
print(sol.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))