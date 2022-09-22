# You are given a string s and an integer k. 
# You can choose any character of the string and change it to any other uppercase English character. 
# You can perform this operation at most k times.

# Return the length of the longest substring containing the same letter you can get 
# after performing the above operations.

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        # Create a dict for the count
        count = {}
        # Create variable for result
        res = 0

        # Instantiate left pointer
        l = 0

        # Create variable for max frequency
        maxf = 0

        # loop over the string with the right pointer
        for r in range(len(s)):

            # set key to current string character and value to 1 + the number of same characters (or 0 if none)
            count[s[r]] = 1 + count.get(s[r], 0)

            # Set maximum frequency to current max or current count, whichever is biggest
            maxf = max(maxf, count[s[r]])

            # if the right-left pointer positions + 1 minus max frequency is greater than number of changes remaining
            if (r - l + 1) - maxf > k:
                #remove one from the left pointer count
                count[s[l]] -= 1
                # Advance the left pointer
                l += 1

            # Set the result to the max of current max and right - left + 1
            res = max(res, r - l + 1)
        return res

# Test Cases
sol = Solution()
s = "ABAB"
k = 2
print(sol.characterReplacement(s, k))

s = "AABABBA"
k = 1
print(sol.characterReplacement(s, k))