"""
https://leetcode.com/problems/lru-cache/

Topics: Dictionary, Doubly Linked List, Design

https://leetcode.com/problems/lru-cache/discuss/45911/Java-Hashtable-%2B-Double-linked-list-(with-a-touch-of-pseudo-nodes)

For this problem, we had to:

- make our own Node class
- use sentinel nodes to make remove/add easy
- know how to remove/add in a LinkedList
- keep a dictionary
"""

# custom node class
class Node:
    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dict = dict()
		# we use dummy start/end nodes so remove is always middle node case
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.dict:
            n = self.dict[key]
            # put node at end of the list since we used it
            self._remove(n)
            self._add(n)
            return n.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            self._remove(self.dict[key])
        n = Node(key, value)
        self._add(n)
        self.dict[key] = n
        if len(self.dict) > self.capacity:
            # if over capacity, remove least recently used node (next of head)
            n = self.head.next
            self._remove(n)
            del self.dict[n.key]
    
	# custom methods
	
    # sentinel nodes means it is always middle node case
    def _remove(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p
        
    # add node to the end of the linked list
    def _add(self, node):
        p = self.tail.prev
        p.next = node
        self.tail.prev = node
        node.prev = p
        node.next = self.tail


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
