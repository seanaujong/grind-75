"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/

Keywords: Dynamic Programming, Kadane's Algorithm

For each iteration, we can calculate info in the following order:

1. the minimum price SO FAR
2. the profit given the current price and minimum price SO FAR
3. the maximum profit SO FAR

The trick here is steps 1 and 2, where we calculate the minimum price SO FAR
before calculating the profit for this iteration. This means that the profit
variable will hold the max profit FOR THAT DAY.

However, sometimes the interviewer may give an *array of price differences* instead.
Now our solution won't work! For this, let us turn to Kadane's algorithm.

Kadane's Algorithm

https://leetcode.com/problems/best-time-to-buy-and-sell-stock/discuss/39038/Kadane's-Algorithm-Since-no-one-has-mentioned-about-this-so-far-%3A)-(In-case-if-interviewer-twists-the-input)
https://medium.com/@rsinghal757/kadanes-algorithm-dynamic-programming-how-and-why-does-it-work-3fd8849ed73d
https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/
https://www.youtube.com/watch?v=86CQq3pKSUw

The basic idea of this is that the local maximum subarray is either:
    - the current element alone OR
    - the current element combined with the previous maximum subarray
    
This translates to: local_max = max(A[i], local_max + A[i])

The global_max is the maximum local_max.
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit_so_far = 0
        min_price_so_far = float('inf')
        for price in prices:
            min_price_so_far = min(min_price_so_far, price)
            # now we can get local_profit
            local_profit = price - min_price_so_far
            max_profit_so_far = max(max_profit_so_far, local_profit)
        return max_profit_so_far
		
# Kadane's Algorithm
class Kadane:
    def maxSumSubarray(self, A: List[int]) -> int:
        local_max = global_max = A[0]
        for elem in A:
            local_max = max(elem, local_max + elem)
            global_max = max(global_max, local_max)
        return global_max
        
    def maxProfit(self, prices: List[int]) -> int:
        local_max = global_max = prices[0]
        for i in range(1, len(prices)):
            diff = prices[i] - prices[i-1]
            local_max = max(0, local_max + diff)
            global_max = max(global_max, local_max)
        return global_max        
