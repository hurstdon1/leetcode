# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

# In other words, return true if one of s1's permutations is the substring of s2.
from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        # if s1 is longer than s2, return False because it's impossible
        if len(s1) > len(s2):
            return False

        # Create count array for both s1 and s2
        s1Count, s2Count = [0] * 26, [0] * 26

        # For indexes in range of s1 
        for i in range(len(s1)):

            # increment corresponding array value for that letter
            s1Count[ord(s1[i]) - ord("a")] += 1
            s2Count[ord(s2[i]) - ord("a")] += 1

        # Instantiate matches variable
        matches = 0

        # For each index of the alphabet
        for i in range(26):

            # Increment matches if s1 and s2 have same count of that variable
            matches += 1 if s1Count[i] == s2Count[i] else 0

        # Instantiate left pointer
        l = 0

        # move right pointer( window starts at end of s1 length, goes the length of s2)
        for r in range(len(s1), len(s2)):

            # If matches is 26, return True (all characters in array match)
            if matches == 26:
                return True
            
            # Create an index variable for current position of right pointer
            index = ord(s2[r]) - ord("a")

            # increase that characters count in our s2count
            s2Count[index] += 1

            # If the count of s1 and s2 at this index are the same
            if s1Count[index] == s2Count[index]:
                # Increment matches
                matches += 1
            # If the count of s2's index is now 1 higher than s1,
            elif s1Count[index] + 1 == s2Count[index]:
                # Decrement match count;
                matches -= 1

            # Create index variable for current position of the left pointer
            index = ord(s2[l]) - ord("a")

            # decrement the count at that index (since we are moving the pointer)
            s2Count[index] -= 1
            # IF the index in s1Count is the same as s2Count
            if s1Count[index] == s2Count[index]:
                # increase number of matches 
                matches += 1
            # If the index at s1count -1 is the same as s2Count
            elif s1Count[index] - 1 == s2Count[index]:
                # Decrement the matches
                matches -= 1
            # Move the left pointer
            l += 1
        
        # If matches is 26, return True. Else, return False.
        return matches == 26

        

# Test Cases

sol = Solution()

s1 = "ab"
s2 = "eidbaooo"
print(sol.checkInclusion(s1, s2))
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").

s1 = "ab"
s2 = "eidboaoo"
print(sol.checkInclusion(s1, s2))
# Output: false
