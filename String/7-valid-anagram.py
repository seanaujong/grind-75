"""
https://leetcode.com/problems/valid-anagram/

Topics: Hash Map, String, Sorting

https://leetcode.com/problems/valid-anagram/discuss/66499/Python-solutions-(sort-and-dictionary).

One solution is to count the frequency of each unique character, then
subtract from those frequencies using the other string. An anagram will zero
this out.

You can also sort the strings, and see if they equal each other.

In Python, you can use a defaultdict OR a Counter.

https://stackoverflow.com/questions/19883015/python-collections-counter-vs-defaultdictint

Counter doesn't automatically create a missing key if you query it, which
might be useful behavior. Counter also has a method called most_common that lets
you sort items by their count. defaultdict needs to have sorted called on it to
do the same thing.
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # anagrams must be the same length!
        if len(s) != len(t):
            return False
        counter = dict()
        # get unique character count
        for c in s:
            if c not in counter:
                counter[c] = 0
            counter[c] += 1
        # how many unique characters do we need to match?
        unique_left = len(counter)
        for c in t:
            # either this character is not in the other one, or
            # we have too much of one character
            if c not in counter or not counter[c]:
                return False
            counter[c] -= 1
            if not counter[c]:
                unique_left -= 1
        return True
        
