"""
https://leetcode.com/problems/two-sum/

Keywords: dictionary, hashmap

Keep a cache of previous numbers, where the key
is the number, and the value is its index.
One-pass O(N) solution.

Alternative solutions:

O(N^2) nested loop
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = dict()
        for i in range(len(nums)):
            n = nums[i]
            other = target - n
            if other in cache:
                return [cache[other], i]
            cache[n] = i