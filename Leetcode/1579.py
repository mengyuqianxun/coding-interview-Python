class UF:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        # 当前连通分量数目
        self.cnt = n

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]
        return x
    def union(self, x,y):
        x, y = self.find(x), self.find(y)
        if x == y:
            return False
        if self.size[x] < self.size[y]:
            x, y = y, x
        self.parent[y] = x
        self.size[x] += self.size[y]
        self.cnt -= 1
        return True
                      
    def connected(self, x, y):
        x, y = self.find(x), self.find(y)
        return x == y

class Solution:
    def maxNumEdgesToRemove(self, n, edges):
        ufa, ufb = UF(n), UF(n)
        ans = 0
        
        # 节点编号改为从 0 开始
        for edge in edges:
            edge[1] -= 1
            edge[2] -= 1

        # 公共边
        for t, u, v in edges:
            if t == 3:
                if not ufa.union(u, v):
                    ans += 1
                else:
                    ufb.union(u, v)

        # 独占边
        for t, u, v in edges:
            if t == 1:
                # Alice 独占边
                if not ufa.union(u, v):
                    ans += 1
            elif t == 2:
                # Bob 独占边
                if not ufb.union(u, v):
                    ans += 1

        if ufa.cnt != 1 or ufb.cnt != 1:
            return -1
        return ans