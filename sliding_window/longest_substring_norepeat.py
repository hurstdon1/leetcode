# Given a string s, find the length of the longest substring without repeating characters.

# Explanation: We can "slide" the window over by updating our pointers. We move the right pointer continuously
# and add the right value to the character set. If the right value is already in the character set,
# we pop the existing value from the set, and update the left pointer until it's no longer in the right set.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # Create a character set
        charSet = set()
        
        # Create a left pointer
        left = 0
        
        # Create a result variable
        result = 0
        
        # Move the right pointer through the array
        for right in range(len(s)):

            # If the right pointer is in charSet
            while s[right] in charSet:

                # Remove the left value from the charset
                charSet.remove(s[left])
                # Move the left pointer
                left += 1
                
            # Add the right value to the charset
            charSet.add(s[right])
            # Update the result to the current result or the current charset
            result = max(result, right-left + 1)
            
        return result
                

# Test Cases
sol = Solution()
s = "abcabcbb"
print(sol.lengthOfLongestSubstring(s))
s= "bbbbb"
print(sol.lengthOfLongestSubstring(s))
s = "pwwkew"
print(sol.lengthOfLongestSubstring(s))