"""
https://leetcode.com/problems/container-with-most-water/

Topics: Array, Two Pointers, Greedy

Start with two pointers i,j with one on each end.
Calculate water with (j-i) * min(height[i], height[j]).
For each iteration, we move the pointer with the lower height
because keeping that lower height will always lead to a worse
answer given any length <= (j-i).
"""

class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        water = 0
        while i < j:
            water = max(
                water,
                (j-i) * min(height[i], height[j])
            )
            # eliminate the lower height
            # because that height always leads to a lower answer
            # given the same length
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return water
