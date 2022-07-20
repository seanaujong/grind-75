"""
https://leetcode.com/problems/word-search/

Topics: Backtracking, DFS
"""

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board: return false
        
        def dfs(board, i, j, word):
            if not len(word): return True
            if not (0<=i<len(board) and 0<=j<len(board[0])):
                return False
            if word[0] != board[i][j]: return False
            # remember letter and mark visited
            letter = board[i][j]
            board[i][j] = '#'
            result = dfs(board,i+1,j,word[1:]) or \
                dfs(board,i-1,j,word[1:]) or \
                dfs(board,i,j+1,word[1:]) or \
                dfs(board,i,j-1,word[1:])
            board[i][j] = letter
            return result
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(board, i, j, word):
                    return True
        return False
        
