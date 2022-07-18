"""
https://leetcode.com/problems/rotting-oranges/

Topics: BFS, Connected Components, Matrix, Graph

The question wants to know if the graph has only
ONE connected component, and how many levels are in
its tree.

We answer the question through BFS.
"""

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        if not rows:
            return -1
        cols = len(grid[0])
        visited = set()
        rotten = deque()
        fresh = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    rotten.append((r,c,0))
                elif grid[r][c] == 1:
                    fresh += 1
        # aka how many levels in our bfs tree
        minutes = 0
        while rotten and fresh:
            r,c,minute = rotten.popleft()
            minutes = max(minutes, minute)
            if grid[r][c] == 1:
                grid[r][c] = 2
                fresh -= 1
            # append fresh apple neighbors only
            for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                xx, yy = r+dx, c+dy
                if not (0<=xx<rows and 0<=yy<cols):
                    continue
                if grid[xx][yy] != 1:
                    continue
                rotten.append((xx,yy,minute+1))
        return minutes if not fresh else -1
            
