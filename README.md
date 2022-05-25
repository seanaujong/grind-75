# Grind 75

My solutions to [Grind 75](https://www.techinterviewhandbook.org/grind75).

# Coding Interview Tips

- Speak through your thought process!

- What are the big ideas of the problem?

    - Data structures, algorithms, special characteristics of the data
    - Ask clarifying questions!

- What is the time/space complexity of the solution?

- What about alternative solutions?

    - What are the trade-offs, or how is it worse?
    - Recursive vs. iterative

# Sean Prashad Tips

If input array is sorted then:

- Binary search
- Two pointers

If asked for all permutations/subsets then:

- Backtracking

If given a tree then:

- DFS
- BFS

If given a graph then:

- DFS
- BFS

If given a linked list then:

- Two pointers

If recursion is banned then:

- Stack

If must solve in-place then:

- Swap corresponding values
- Store one or more different values in the same pointer

If asked for maximum/minimum subarray/subset/options then:

- Dynamic programming

If asked for top/least K items then:

- Heap

If asked for common strings then:

- Map
- Trie

Else:

- Map/Set for O(1) time & O(n) space
- Sort input for O(nlogn) time and O(1) space

# Patterns

## Dictionary (Hash Map)

- Can be used as a cache

## Stack

- Good when you need to keep track of "last seen"/"history" order

## Linked Lists

- Do we need to keep a reference to a sentinel node?

    - Recall the sentinel node points to the head of the linked list
