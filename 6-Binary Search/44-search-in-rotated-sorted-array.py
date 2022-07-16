"""
https://leetcode.com/problems/search-in-rotated-sorted-array/

Topics: Binary Search
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo = 0
        hi = len(nums) - 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] > nums[hi]:
                lo = mid + 1
            else:
                hi = mid
        pivot = lo

        lo = 0
        hi = len(nums)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            pmid = (mid + pivot) % len(nums)
            if nums[pmid] == target:
                return pmid
            if nums[pmid] > target:
                hi = mid
            else:
                lo = mid + 1
        return -1
        
                    
