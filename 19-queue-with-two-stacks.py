"""
https://leetcode.com/problems/implement-queue-using-stacks

Topics: Stack, Design, Queue

https://leetcode.com/problems/implement-queue-using-stacks/discuss/64198/Share-my-python-solution-(32ms)/179427
"""

class MyQueue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x):
        self.s1.append(x)

    def pop(self):
        self.peek()
        return self.s2.pop()

    def peek(self):
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2[-1]        

    def empty(self):
        return not self.s1 and not self.s2
