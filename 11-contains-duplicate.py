"""
https://leetcode.com/problems/contains-duplicate/

Topics: Array, Hash Map, Sorting, Set
"""

# O(n logn) time
# sorting
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        prev = nums[0]
        for n in nums[1:]:
            if prev == n:
                return True
            prev = n
        return False
		
# O(n) time, O(n) space
# set (or dict)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        cache = set()
        for n in nums:
            if n in cache:
                return True
            cache.add(n)
        return False
