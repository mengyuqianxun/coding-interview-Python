#并查集，将每个格子变成4份三角形，从上顺时针依次记为0，1，2，3
class Solution(object):
    def regionsBySlashes(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """
        class unionfind:
            def __init__(self,n):
                self.parent = list(range(4*n*n))
                self.count = 4*n*n

            def find(self,x):
                if self.parent[x] == x:
                    return x
                return self.find(self.parent[x])

            def union(self,x,y):
                xroot = self.find(x)
                yroot = self.find(y)
                if xroot == yroot:
                    return
                self.parent[xroot] = yroot
                self.count -= 1

        n = len(grid)
        uf = unionfind(n)

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
        return uf.count

#并查集，切分区域的思想
class Solution(object):
    def regionsBySlashes(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """
        class unionfind:
            def __init__(self, n):
                self.parent = range(n * n + 2 * n + 2)
                self.area = 1

            def find(self, x):
                if self.parent[x] != x:
                    self.parent[x] = self.find(self.parent[x])
                return self.parent[x]

            def union(self, x, y):
                xroot = self.find(x)
                yroot = self.find(y)
                self.parent[xroot] = yroot

            def isClosed(self, x, y):
                xroot = self.find(x)
                yroot = self.find(y)
                if xroot == yroot:
                    self.area += 1
                    return True
                else:
                    return False

        n = len(grid)
        uf = unionfind(n)
        
        # 连接边缘
        node = n * n + 2 * n + 1
        for i in range(n + 1):
            uf.union(node, i)   # 连接上边缘
            uf.union(node, n * n + n + i)   # 连接下边缘
            uf.union(node, i * (n + 1))     # 连接左边缘
            uf.union(node, i *  (n + 1) + n)    # 连接右边缘

        # 连接斜杠
        for i in range(n):
            for j in range(n):
                if grid[i][j] == '/':
                    node1 = (n + 1) * (i + 1) + j
                    node2 = (n + 1) * i + (j + 1)
                    if not uf.isClosed(node1, node2):
                        uf.union(node1, node2)
                elif grid[i][j] == '\\':
                    node1 = (n + 1) * i + j
                    node2 = (n + 1) * (i + 1) + (j + 1)
                    if not uf.isClosed(node1, node2):
                        uf.union(node1, node2)
        return uf.area

#带路径压缩的并查集，此题数据量小，因此速度反而慢
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