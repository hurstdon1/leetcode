# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
# such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Create an array for the result
        res = []
        # Sort the numbers array
        nums.sort()
        
        # loop over the nums 
        for i, a in enumerate(nums):
            
            # if the index is the same as previous, move to next index
            if i > 0 and a == nums[i-1]:
                continue
            
            # Create pointers for the left and right side of the array
            left, right = i+1, len(nums)-1
            
            # while the indices aren't equal
            while left < right:
                
                # Calculate the three sum of current index, left, and right pointers
                threeSum = a + nums[left] + nums[right]
                
                # If that sum is greater than 0 (target), move the right pointer back 1
                if threeSum > 0:
                    right -= 1
                
                # If that sum is less than 0 (target), move the left pointer forward 1
                if threeSum < 0:
                    left += 1
                    
                # If that sum is equal to 0 (target)
                if threeSum == 0:
                    
                    # Append the index, left pointer, and right pointer values to the results
                    res.append([a, nums[left], nums[right]])
                    # Move the left pointer forward one space
                    left += 1
                    # If the new left pointer is the same as the previous index and not equal to the right pointer
                    while nums[left] == nums[left-1] and left < right:
                        # Advance the left pointer one space
                        left += 1
                        
        return res


# Test Cases
sol = Solution()
print(sol.threeSum([-1,0,1,2,-1,-4]))
print(sol.threeSum([0,1,1]))
print(sol.threeSum([0,0,0]))