"""
https://leetcode.com/problems/accounts-merge/

Topics: Graph, Union Find

https://www.youtube.com/watch?v=ayW5B2W9hfo
https://leetcode.com/problems/accounts-merge/discuss/1084738/Python-The-clean-Union-Find-solution-you-are-looking-for
"""

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        
    def union(self, child, parent):
        self.parent[self.find(child)] = self.find(parent)
        
    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))
        
        # create unions between indices
        ownership = dict()
        for i, (_, *emails) in enumerate(accounts):
            for email in emails:
                if email in ownership:
                    uf.union(i, ownership[email])
                ownership[email] = i
        
        # append emails to correct index
        result = defaultdict(list)
        for email, owner in ownership.items():
            result[uf.find(owner)].append(email)
            
        return [[accounts[i][0]] + sorted(emails)
            for i, emails in result.items()]
        
