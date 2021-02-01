class Solution(object):
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        class UnionFind:
            def __init__(self,n):
                self.parent = list(range(n))
                self.size = [1]*n
            def find(self,x):
                if self.parent[x] != x:
                    self.parent[x] = self.find(self.parent[x])
                    return self.parent[x]
                return x
            def union(self,x,y):
                xroot = self.find(x)
                yroot = self.find(y)
                if xroot == yroot:
                    return
                if self.size[xroot] < self.size[yroot]:
                    xroot,yroot = yroot,xroot
                self.parent[yroot] = xroot
                self.size[xroot] += self.size[yroot]
            def isConnected(self,x,y):
                return self.find(x) == self.find(y)
        m,n = len(grid),len(grid[0])
        uf = UnionFind(m*n)
        
        edges = []
        for i in range(m):
            for j in range(n):
                edges.append((grid[i][j],i,j))
        edges.sort(key = lambda x:x[0])
        for t,i,j in edges:
            for u,v in [(i-1,j),(i+1,j),(i,j+1),(i,j-1)]:
                if 0 <= u < m and 0 <= v < n:
                    if grid[u][v] < t:
                        uf.union(i*n+j,u*n+v)
            if uf.isConnected(0,m*n-1):
                return t