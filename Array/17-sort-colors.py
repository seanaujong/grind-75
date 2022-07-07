"""
https://leetcode.com/problems/sort-colors/

Topics: Array, Two Pointers, Sorting

https://leetcode.com/problems/sort-colors/discuss/681526/Python-O(n)-3-pointers-in-place-approach-explained

Keep 3 pointers, where red, white, and blue point at elements
just after the last 0 (red), after the last 1 (white), and before the first 2 (blue).

The idea is to put sorted 0's and 1's to the beginning, and sorted 2's to the end.
"""

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red = 0 # after the last 0
        white = 0 # after the last 1
        blue = len(nums) - 1 # before the last 2
        while white <= blue:
            # if white pointer is red...
            if nums[white] == 0:
                nums[red], nums[white] = nums[white], nums[red]
                white += 1
                red += 1
            elif nums[white] == 1:
                # white is in the correct place
                white += 1
            else:
                # nums[white] == 2, aka blue
                nums[white], nums[blue] = nums[blue], nums[white]
                blue -= 1
        