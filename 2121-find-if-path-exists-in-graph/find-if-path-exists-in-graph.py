class DSU:
    def __init__(self,n):
        self.fa = list(range(n))
    def find(self,x):
        if (self.fa[x]!=x):
            self.fa[x] = self.find(self.fa[x])
        return self.fa[x]

    def union(self,x,y):
        self.fa[self.find(x)]=self.find(y)



class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        dsu = DSU(n)
        for (u,v) in edges:
            dsu.union(u,v)

        return dsu.find(source)==dsu.find(destination)     

"""
Practice a simple question for DSU
"""