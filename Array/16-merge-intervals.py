"""
https://leetcode.com/problems/merge-intervals/

Topics: Array, Sorting

Sort the intervals by start time. Merge when our current end time is
greater than or equal to the next start time.
"""

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        result = [intervals[0]]
        for i in range(1, len(intervals)):
            if result[-1][1] >= intervals[i][0]:
                # merge
                result[-1][1] = max(result[-1][1], intervals[i][1])
            else:
                result.append(intervals[i])
        return result
