

class Solution(object):
    def regionsBySlashes(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """
        class UF:
            def __init__(self, M):
                self.parent = {}
                self.size = {}
                self.cnt = 0
                # 初始化 parent，size 和 cnt
                for i in range(M):
                    self.parent[i] = i
                    self.cnt += 1
                    self.size[i] = 1

            def find(self, x):
                if x != self.parent[x]:
                    self.parent[x] = self.find(self.parent[x])
                    return self.parent[x]
                return x

            def union(self, p, q):
                if self.connected(p, q): return
                # 小的树挂到大的树上， 使树尽量平衡
                leader_p = self.find(p)
                leader_q = self.find(q)
                if self.size[leader_p] < self.size[leader_q]:
                    self.parent[leader_p] = leader_q
                    self.size[leader_p] += self.size[leader_q]
                else:
                    self.parent[leader_q] = leader_p
                    self.size[leader_q] += self.size[leader_p]
                self.cnt -= 1

            def connected(self, p, q):
                return self.find(p) == self.find(q)  

        n = len(grid)
        uf = UF(4*n*n)

        def pos(row,col,i):
            return (row*n + col)*4 + i

        for row in range(n):
            line = grid[row]
            for col in range(n):
                s = line[col]
                if row > 0:
                    uf.union(pos(row-1,col,2),pos(row,col,0))
                if col > 0:
                    uf.union(pos(row,col-1,1),pos(row,col,3))                
                if s != '\\':
                    uf.union(pos(row,col,0),pos(row,col,3))
                    uf.union(pos(row,col,1),pos(row,col,2))
                if s != '/':
                    uf.union(pos(row,col,0),pos(row,col,1))
                    uf.union(pos(row,col,3),pos(row,col,2))
        return uf.cnt