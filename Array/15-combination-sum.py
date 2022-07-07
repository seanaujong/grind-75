"""
https://leetcode.com/problems/combination-sum/

Topics: Array, backtracking

https://leetcode.com/problems/combination-sum/discuss/16502/A-general-approach-to-backtracking-questions-in-Java-(Subsets-Permutations-Combination-Sum-Palindrome-Partitioning)
https://leetcode.com/problems/combination-sum/discuss/1755084/Detailed-Time-and-Space-Complecity-analysisc++javabacktracking
"""

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        self.backtrack(candidates, target, [], result, 0)
        return result
    
    def backtrack(self, candidates, remain, path, result, start):
        # base case: we overshot target
        if remain < 0: return
        # base case: hit target, success
        elif remain == 0: result.append(path)
        # backtracking
        else:
            for i in range(start, len(candidates)):
                self.backtrack(
                    candidates,
                    remain - candidates[i],
                    path + [candidates[i]], # append/remove
                    result,
                    i
                )
