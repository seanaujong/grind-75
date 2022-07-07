"""
https://leetcode.com/problems/product-of-array-except-self/

Topics: Array, Prefix Sum

https://leetcode.com/problems/product-of-array-except-self/discuss/1597994/C%2B%2BPython-4-Simple-Solutions-w-Explanation-or-Prefix-and-Suffix-product-O(1)-space-approach
"""

"""
Solution 1: Calculate product of whole array, divide product by nums[i]

3 cases

1. zeroes > 1, then the array is all 0
2. zeroes == 1, then the array is all 0 except where the 0 was,
which will be the product of the rest of the array
3. zeroes == 0, simple case
"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # non-zero product
        prod = 1
        # zero count
        zeros = 0
        for n in nums:
            if n == 0:
                zeros += 1
            else:
                prod *= n
        if zeros > 1:
            # case 3, zeros > 1
            return [0] * len(nums)
        for i, n in enumerate(nums):
            if zeros:
                # case 2, zeros == 1
                nums[i] = 0 if n else prod
            else:
                # case 1, zeros == 0
                nums[i] = prod // n
        return nums
        
"""
Solution 2: Prefix and Suffix Products

To solve the problem without the division operator, calculate two arrays pre
and suf where pre[i] contains the product leading up to nums[i], and suf[i]
contains the product following after nums[i]. Then multiply them respectively.

ans[i] = pre[i-1] * suf[i+1]
"""

"""
Solution 3: Space-Optimized Prefix and Suffix Products

Two-pass solution

Initialize an array filled with 1's.
First pass, for each i, calculate prefix product before i
ans[i] = ans[i-1] * nums[i-1]
Second pass, go backwards, keep a variable suffixProd = 1
For each i, ans[i] *= suffixProd and suffixProd *= nums[i] to update it
"""

"""
Solution 4: One-Pass Prefix and Suffix Products

Calculate the prefix product from the beginning, and the suffix product from the end
at the same time.
"""
class Solution:
    def productExceptSelf(self, nums):
        ans, suf, pre = [1]*len(nums), 1, 1
        for i in range(len(nums)):
            ans[i] *= pre               # prefix product from one end
            pre *= nums[i]
			ans[-1-i] *= suf            # suffix product from other end
			suf *= nums[-1-i]
        return ans
