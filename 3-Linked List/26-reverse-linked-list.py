"""
https://leetcode.com/problems/reverse-linked-list/

Topics: Linked List, Recursion

https://www.youtube.com/watch?v=NhapasNIKuQ
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head:
            nxt = head.next
            head.next = prev
            prev = head
            head = nxt
        return prev
        
