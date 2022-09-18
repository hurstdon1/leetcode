# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
# typically using all the original letters exactly once.
from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # Instantiate a dictionary
        d = defaultdict(list)

        # loop over strings
        for s in strs:
            
            # Create an array for each letter of the alphabet
            count = [0] * 26
            
            # loop over characters in the string
            for c in s:
                
                # Add 1 to the appropriate array index
                count[ord(c) - ord('a')] += 1
                
            # add the count to the dictionary with the string as the value
            d[tuple(count)].append(s)
            
        # return the values from the dictionary
        return d.values()


# Test Cases
sol = Solution()
print(sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
print(sol.groupAnagrams([""]))
print(sol.groupAnagrams(["a"]))