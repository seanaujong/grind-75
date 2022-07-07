"""
https://leetcode.com/problems/largest-rectangle-in-histogram/submissions/

Topics: Stack

https://leetcode.com/problems/largest-rectangle-in-histogram/discuss/28917/AC-Python-clean-solution-using-stack-76ms/492440
"""

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        stack = [-1]
        largest = 0
        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                largest = max(largest, h*w)
            stack.append(i)
        return largest
        
