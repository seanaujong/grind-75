"""
https://leetcode.com/problems/01-matrix/

Topics: BFS, Dynamic Programming, Matrix

https://leetcode.com/problems/01-matrix/discuss/363902/BFS-python-explained-and-commneted-(two-approaches)
https://leetcode.com/problems/01-matrix/discuss/1369741/C%2B%2BJavaPython-BFS-DP-solutions-with-Picture-Clean-and-Concise-O(1)-Space
"""

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        from collections import deque
        queue = deque()
        visited = set()
        m, n = len(mat), len(mat[0])
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    visited.add((i, j))
                    queue.append((i, j))
                    
        while queue:
            x, y = queue.popleft()
            for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                xx, yy = x + dx, y + dy
                if 0<=xx<m and 0<=yy<n and (xx,yy) not in visited:
                    mat[xx][yy] = mat[x][y] + 1
                    visited.add((xx,yy))
                    queue.append((xx,yy))
        
        return mat
        
