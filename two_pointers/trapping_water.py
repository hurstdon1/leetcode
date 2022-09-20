# Given n non-negative integers representing an elevation map where the width of each bar is 1,
# compute how much water it can trap after raining.


from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        
        # If there is no values, return 0
        if not height: return 0
        
        # Create pointers for left and right
        left = 0
        right = len(height) - 1
        
        # Create max variables for left and right
        leftMax = height[left]
        rightMax = height[right]

        # Create a result variable
        res = 0
        
        # While pointers aren't equal
        while left < right:
            
            # If the left max is less than the right max
            if leftMax < rightMax:

                # Increase the left pointer
                left += 1
                # set left max to the max between current max an the height at the left pointer
                leftMax = max(leftMax, height[left])
                # Store the left max minus current height in the result
                res += (leftMax - height[left])
                
            else:

                # Decrease the right pointer
                right -= 1
                # Set the right max to the max between the current max and the height at the right pointer
                rightMax = max(rightMax, height[right])
                # Store the right max minus current height in the result
                res += (rightMax - height[right])

        # Return the result        
        return res


# Test Cases
sol = Solution()
height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(sol.trap(height))
height = [4,2,0,3,2,5]
print(sol.trap(height))