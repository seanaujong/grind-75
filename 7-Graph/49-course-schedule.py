"""
https://leetcode.com/problems/course-schedule/

Topics: Graph, Topological Sort, BFS, DFS

https://leetcode.com/problems/course-schedule/discuss/58509/C%2B%2B-BFSDFS

DFS Solution: https://www.youtube.com/watch?v=EgI5nU9etnU

O(V + E)
"""

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # adjacency list
        edges = [[] for i in range(numCourses)]
        # count how many prerequisites per course
        degrees = [0] * numCourses
        for course, pre_course in prerequisites:
            edges[pre_course].append(course)
            degrees[course] += 1
        
        # start with courses without prerequisites
        queue = deque(course for course, degree in enumerate(degrees) if not degree)
        while queue:
            course = queue.popleft()
            for next_course in edges[course]:
                degrees[next_course] -= 1
                if not degrees[next_course]:
                    queue.append(next_course)
        
        # success if we eliminated all edges
        return not sum(degrees)
