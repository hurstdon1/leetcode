# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
# typically using all the original letters exactly once.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        sd = {}
        td = {}

        for c in s:
            if c not in sd:
                sd[c] = 1
            else:
                sd[c] += 1

        for c in t:
            if c not in td:
                td[c] = 1
            else:
                td[c] += 1

        if sd == td:
            return True

        else:
            return False


# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:

# Input: s = "rat", t = "car"
# Output: false

# Test Cases
sol = Solution()
print(sol.isAnagram('anagram', 'nagaram'))
print(sol.isAnagram('rat', 'car'))
