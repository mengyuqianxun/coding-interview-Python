#方法一：二分法，广度优先遍历
class Solution(object):
    def minimumEffortPath(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: int
        """
        m,n = len(heights),len(heights[0])
        ans = 0
        left,right = 0,10**6-1

        while left <= right:
            mid = (left + right)//2
            q = collections.deque([(0,0)])
            set_h = {(0,0)}

            while q:
                x,y = q.popleft()
                for nx,ny in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
                    if 0 <= nx < m and 0 <= ny <n and \
                    (nx,ny) not in set_h and \
                    abs(heights[nx][ny]-heights[x][y]) <= mid:
                        q.append((nx,ny))
                        set_h.add((nx,ny))
            if (m-1,n-1) in set_h:
                ans = mid
                right = mid - 1
            else:
                    left = mid + 1
        return ans

#方法二：并查集
class Solution(object):
    def minimumEffortPath(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: int
        """
        class UnionFind:
            def __init__(self,n):
                self.parent = list(range(n))
                self.size = [1]*n
                self.cnt = n
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
                self.cnt -= 1
            def isConnected(self,x,y):
                return self.find(x) == self.find(y)

        m,n = len(heights),len(heights[0])
        
        edges = []
        for i in range(m):
            for j in range(n):
                here = i*n + j
                if i > 0:
                    edges.append((here - n,here,abs(heights[i-1][j]-heights[i][j])))
                if j > 0:
                    edges.append((here - 1,here,abs(heights[i][j-1]-heights[i][j])))
        edges.sort(key = lambda e:e[2])

        uf = UnionFind(m*n)
        ans = 0
        for x,y,h in edges:
            uf.union(x,y)
            if uf.isConnected(0,m*n-1):
                ans = h
                break
        return ans



