"""
https://leetcode.com/problems/insert-interval/

Topics: Array

https://leetcode.com/problems/insert-interval/discuss/21602/Short-and-straight-forward-Java-solution

This is a good problem to think up test cases on.
"""

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = list()
        # add all the intervals ending before newInterval starts
        i = 0
        while (i < len(intervals) and intervals[i][1] < newInterval[0]):
            result.append(intervals[i])
            i += 1
        # now all the intervals left end after newInterval starts
        # therefore they are overlapping!
        # merge all intervals overlapping with newInterval
        while (i < len(intervals) and intervals[i][0] <= newInterval[1]):
            newInterval = [
                min(newInterval[0], intervals[i][0]),
                max(newInterval[1], intervals[i][1])
            ]
            i += 1
        result.append(newInterval)
        # now all the intervals left begin after newInterval ends
        # add these
        while (i < len(intervals)):
            result.append(intervals[i])
            i += 1
        return result
        
