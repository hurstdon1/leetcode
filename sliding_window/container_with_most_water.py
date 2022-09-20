# You are given an integer array height of length n. 
# There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        # Create a variable for the resulting area
        res = 0
        
        # Create left an right pointers
        left = 0
        right = len(height)-1
        
        # While our pointers aren't equal
        while left < right:
            
            # Set current area to the minimum height between two lines times the horizontal axis
            currentArea = min(height[left], height[right]) * (right - left)
            
            # Set result to the max between current value and current max
            res = max(res, currentArea)
            
            # If the height of the left line is less than height of the right
            if height[left] < height[right]:
                # advance the left pointer
                left += 1
                
            # Otherwise, avance the right pointer
            else:
                right -= 1
                
        # Return the result
        return res


# Test Cases
sol = Solution()
height = [1,8,6,2,5,4,8,3,7]
print(sol.maxArea(height))      
height = [1,1]
print(sol.maxArea(height)) 