"""
https://leetcode.com/problems/string-to-integer-atoi/

Topics: String, DFA

In interview, can just do simple edge cases.

You can also solve the problem with DFA
"""

"""
https://leetcode.com/problems/string-to-integer-atoi/discuss/4654/My-simple-solution
Interview-ready solution
1. Discard leading whitepsaces
2. Sign check
3. Append digits, stop on non-digits
4. Clamp for underflow/overflow
"""
class Solution:
    def myAtoi(self, s: str) -> int:
        sign = 1
        base = 0
        i = 0
        # discard leading whitespaces
        while i < len(s) and s[i] == ' ': i += 1
        if i >= len(s): return 0
        # sign check
        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            sign = 1
            i += 1
        # main loop
        while i < len(s) and s[i].isdigit():
            base = 10*base + int(s[i])
            i += 1
        # clamp
        value = sign*base
        value = min(value, 2 ** 31 - 1)
        value = max(-(2 ** 31), value)
        return value
        
"""
https://leetcode.com/problems/string-to-integer-atoi/discuss/798380/Fast-and-simpler-DFA-approach-(Python-3)
DFA, which stands for Deterministic Finite Automation,
is a state machine that either accepts or rejects a sequence
of symbols by running through a state sequence uniquely
determined by the string.
"""
class Solution:
    def myAtoi(self, str: str) -> int:
        value, state, pos, sign = 0, 0, 0, 1

        if len(str) == 0:
            return 0

        while pos < len(str):
            current_char = str[pos]
            if state == 0:
                if current_char == " ":
                    state = 0
                elif current_char == "+" or current_char == "-":
                    state = 1
                    sign = 1 if current_char == "+" else -1
                elif current_char.isdigit():
                    state = 2
                    value = value * 10 + int(current_char)
                else:
                    return 0
            elif state == 1:
                if current_char.isdigit():
                    state = 2
                    value = value * 10 + int(current_char)
                else:
                    return 0
            elif state == 2:
                if current_char.isdigit():
                    state = 2
                    value = value * 10 + int(current_char)
                else:
                    break
            else:
                return 0
            pos += 1

        value = sign * value
        value = min(value, 2 ** 31 - 1)
        value = max(-(2 ** 31), value)

        return value
