"""
https://leetcode.com/problems/number-of-islands/

Topics: DFS, BFS, Matrix, Connected Components
"""

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        def dfs(grid, i, j):
            if 0<=i<len(grid) and 0<=j<len(grid[0]) and grid[i][j] == '1':
                grid[i][j] = '-1'
                dfs(grid, i+1, j)
                dfs(grid, i-1, j)
                dfs(grid, i, j+1)
                dfs(grid, i, j-1)
        
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(grid, i, j)
                    count += 1
        return count
        
