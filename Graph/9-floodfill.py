"""
https://leetcode.com/problems/flood-fill/

Topics: DFS, BFS, 2D Array

https://drive.google.com/drive/u/0/folders/1i8y3oBULlcPcedkuk7sT8usYoB_1izIR
"""

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        # kick it off with the first pixel given
        stack = [(sr, sc)]
        # boundaries
        m, n = len(image), len(image[0])
        # store to compare later
        oldColor = image[sr][sc]
        # edge case where it is "already floodfilled" to this color
        if oldColor == newColor: return image
        # floodfill
        while stack:
            r, c = stack.pop()
            image[r][c] = newColor
            # for each neighbor
            for nr, nc in ((r-1,c),(r+1,c),(r,c-1),(r,c+1)):
                # floodfill if within boundaries and is of the oldColor
                if 0 <= nr < m and 0 <= nc < n and image[nr][nc] == oldColor:
                    stack.append((nr,nc))
        return image
        