"""
https://leetcode.com/problems/binary-search/

Topics: Binary Search

https://leetcode.com/problems/binary-search/discuss/423162/Binary-Search-101
https://docs.google.com/document/d/1Syo9o83EEVB9orJSQS3zGkuQsF1sdNhqZaGvl6YGmjo/edit
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l < r: 
            mid = l + (r - l) // 2
			# in this case we know nums[mid] is not target
            # therefore mid + 1
            if nums[mid] < target: l = mid + 1
			# in this case nums[mid] >= target, so r might be target
            # therefore mid
            else: r = mid
		# right should contain the first number where
        # nums[mid] >= target
        return r if nums[r] == target else -1


