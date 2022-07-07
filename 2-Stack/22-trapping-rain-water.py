"""
https://leetcode.com/problems/trapping-rain-water/

Topics: Two Pointers

https://leetcode.com/problems/trapping-rain-water/discuss/17391/Share-my-short-solution./185869
"""

class Solution:
    def trap(self, height: List[int]) -> int:
        trapped = 0
        l, r = 0, len(height) - 1
        lmax, rmax = 0, 0
        while (l <= r):
            lmax = max(lmax, height[l])
            rmax = max(rmax, height[r])
            if lmax < rmax:
                trapped += (lmax - height[l])
                l += 1
            else:
                trapped += (rmax - height[r])
                r -= 1
        return trapped
