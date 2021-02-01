class Solution(object):
    def numSimilarGroups(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        class Unionfind:
            def __init__(self,n):
                self.parent = list(range(n))
                self.size = [1]*n
                self.cnt = n
            def find(self,x):
                if self.parent[x] != x:
                    self.parent[x] = self.find(self.parent[x])
                    return self. parent[x]
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
                self.cnt -= 1
            def isConnected(self,x,y):
                return self.find(x) == self.find(y)

        n = len(strs)
        uf = Unionfind(n)
        for i in range(n):
            for j in range(i+1,n):
                if not uf.isConnected(i,j) and \
                self.isSimilar(strs[i],strs[j]):
                    uf.union(i,j)
        return uf.cnt

    def isSimilar(self,x,y):
        num = 0
        for a,b in zip(x,y):
            if a != b:
                num += 1
            if num > 2:
                return False
        return True