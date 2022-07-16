"""
https://leetcode.com/problems/maximum-profit-in-job-scheduling/

Topics: Dynamic Programming, Binary Search

https://leetcode.com/problems/maximum-profit-in-job-scheduling/discuss/918804/Python-Top-Down-and-Bottom-Up-DP-7-lines-each

Time Complexity: O(n·log(n)) because bisect.bisect_left is a log(n) operation.
Space Complexity: O(n)

Approach:
Step 1: Sort start, end and profit according to the start time (some test cases are not sorted - the examples are misleading in this respect)
Step 2: If you choose to take job i skip all jobs that start before job i ends. jump is used to find the index of the first job that starts after job i ends.
Step 3: Take a dynamic programming approach to determine the optimal profit. At each step you can choose:

    i. to take the job for profit[i] + helper(jump[i])
	ii. or to skip the job for helper(i+1)
"""

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        start, end, profit = zip(*sorted(zip(startTime, endTime, profit)))
        jump = {i: bisect.bisect_left(start, end[i]) for i in range(n)}
        
        @functools.lru_cache(None)
        def helper(i):
            if i == len(start): return 0
            return max(
                helper(i + 1),
                profit[i] + helper(jump[i])
            )
        
        return helper(0)
