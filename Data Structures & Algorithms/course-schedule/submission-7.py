class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        premap = {i:[] for i in range(numCourses)}
        for c, p in prerequisites:
            premap[c].append(p)
        visit = set()
        def dfs(c):
            if c in visit: return False
            if premap[c]==[]:return True
            visit.add(c)
            for p in premap[c]:
                if not dfs(p): return False
            visit.remove(c)
            premap[c]=[]
            return True
        for c in range(numCourses):
            if not dfs(c):return False
        return True