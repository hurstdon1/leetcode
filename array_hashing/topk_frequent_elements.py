# Given an integer array nums and an integer k, 
# return the k most frequent elements. 
# You may return the answer in any order.

from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Create a dictionary for the counter
        count = {}
        
        # Create a list for the frequency of numbers based on the list size
        freq = [[] for i in range(len(nums) + 1)]
        
        # For numbers in nums
        for n in nums:
            
            # If the value is not in the count dict, add it
            if n not in count:
                count[n] = 1
                
            # Otherwise, add 1 to the existing count
            else:
                count[n] += 1
        
        # for key and value in the dictionary
        for n, c in count.items():
            
            # append the key to the frequency list
            freq[c].append(n)
            
        # Create a result list
        res = []
        
        # For variable in range of the frequency list
        for i in range(len(freq) - 1, 0, -1):
            
            
            # For n in that number
            for n in freq[i]:
                
                # Append the n to the result
                res.append(n)
                
                # If the length of the result is equal to the kth most values, return the result
                if len(res) == k:
                    return res


# Test Cases
sol = Solution()
print(sol.topKFrequent([1,1,1,2,2,3], 2))
print(sol.topKFrequent([1], 1))

