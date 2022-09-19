# Given an integer array nums, return an array answer such that answer[i] is equal to the product of
# all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # Create arrays for left and right products
        leftArr = [0] * len(nums)
        rightArr = [0] * len(nums)
        
        # Set first values (from left or right) to 1
        leftArr[0] = 1
        rightArr[len(nums)-1] = 1

        # Create answer array
        answer = [0] * len(nums)
        
        # step through array from left to right
        for i in range(1, len(nums)):
            # set left array index to previous left index * previous nums index
            leftArr[i] = leftArr[i-1] * nums[i-1]
            
        # step through the array from right to left
        for i in reversed(range(len(nums) - 1)):
            # set right array index to previous right index * previous nums index
            rightArr[i] = rightArr[i+1] * nums[i+1]
            
        # for each index in the array
        for i in range(len(nums)):
            # set array equal to left * right
            answer[i] = leftArr[i] * rightArr[i]
            
        # return the answer
        return answer


# Test Cases
sol = Solution()
print(sol.productExceptSelf([1,2,3,4]))
print(sol.productExceptSelf([-1,-1,0,-3,3]))