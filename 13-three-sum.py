"""
https://leetcode.com/problems/3sum/

Topics: Array, Two Pointers, Sorting

Sorting allows us to check for duplicates easily.

We iterate through the list with the left pointer, trying
to find two extra numbers to sum to 0. Since the list is sorted,
the right pointer will always be higher than the mid pointer.
If the sum is too small, we can increase the mid pointer.
If the sum is too large, we can decrease the right pointer.
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
		nums.sort()
		result = []
		for left in range(len(nums)-2)):
			# duplicate check
			if left > 0 and nums[left] == nums[left-1]: continue
			mid = left + 1
			right = len(nums-1)
			while mid < right:
				sum = nums[left] + nums[mid] + nums[right]
				if sum < 0:
					# sum is too small, increase mid
					mid += 1
				elif sum > 0:
					# sum is too large, decrease right
					right -= 1
				else:
					# sum == 0, success case
					result.append([nums[left], nums[mid], nums[right])
                    # duplicate checks
					while mid < right and nums[mid] == nums[mid+1]: mid += 1
					while mid < right and nums[right] == nums[right-1]: right -= 1
                    # end up pointing to the last duplicate, so shift one more time
					mid += 1
					right -= 1
		return result
