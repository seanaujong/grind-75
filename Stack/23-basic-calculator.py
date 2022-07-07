"""
https://leetcode.com/problems/basic-calculator/

Topics: Math, Stack, Recursion

https://leetcode.com/problems/basic-calculator/discuss/62361/Iterative-Java-solution-with-stack
"""

class Solution:
    def calculate(self, s: str) -> int:
        result = 0
        number = 0
        sign = 1
        stack = []
        for c in s:
            if c.isnumeric():
                # append digit
                number = 10*number + int(c)
            elif c == "+":
                result += sign*number
                number = 0
                sign = 1
            elif c == "-":
                result += sign*number
                number = 0
                sign = -1
            elif c == "(":
                stack.append(result)
                stack.append(sign)
                sign = 1
                result = 0
            elif c == ")":
                result += sign*number
                number = 0
                result *= stack.pop()
                result += stack.pop()
        return result + (sign*number)
        
