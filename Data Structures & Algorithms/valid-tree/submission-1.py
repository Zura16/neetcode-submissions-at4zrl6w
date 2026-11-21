class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj={i:[] for i in range(n)}
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        visit = set()
        def dfs(a, b):
            if a in visit: return False
            visit.add(a)
            for c in adj[a]:
                if c == b: continue
                if not dfs(c, a): return False
            return True
        return dfs(0, -1) and len(visit) == n