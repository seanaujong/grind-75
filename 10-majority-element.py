"""
https://leetcode.com/problems/majority-element/

Topics: Array, Hash Table, Divide and Conquer, Sorting, Counting

https://leetcode.com/problems/majority-element/discuss/51712/Python-different-solutions
https://www.cs.utexas.edu/~moore/best-ideas/mjrty/index.html

Two obvious solutions involve sorting or a dictionary.
There is also a solution involving Boyer Moore's Algorithm, O(1) space.
"""

# the majority element will be the middle sorted element by definition
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return sorted(nums)[len(nums) // 2]

# dictionary solution
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cache = dict()
        threshold = len(nums) / 2
        for element in nums:
            if element not in cache:
                cache[element] = 0
            cache[element] += 1
            if cache[element] > threshold:
                return element

# Boyer Moore's Algorithm --> O(1) Space
class Solution:
    def majorityElement(self, nums):
        # first assume that the first element is the majority element
        count = 1
        result = nums[0]
        
        for num in nums[1:]:
            if num != result:
                # decrement when we get a different element
                count -= 1
                if count == 0:
                    # if the counter is 0, we use a new candidate (num)
                    result = num
                    count = 1            
            else:
                # increment when we get the same element
                count += 1
        # there is always a majority element in this case;
        # otherwise, you must take one more linear pass through
        # the data to count the element
        return result
        