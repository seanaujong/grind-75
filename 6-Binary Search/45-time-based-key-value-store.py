"""
https://leetcode.com/problems/time-based-key-value-store/

Topics: Binary Search, Design, Dictionary

https://github.com/python/cpython/blob/3.9/Lib/bisect.py#L15-L35
"""

class TimeMap:

    def __init__(self):
        self.dict = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dict[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        arr = self.dict[key]
        lo = 0
        hi = len(arr)
        result = ""
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if arr[mid][0] <= timestamp:
                # best result so far
                result = arr[mid][1]
                lo = mid + 1
            else:
                # invalid result
                hi = mid
        return result

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)