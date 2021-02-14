class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        class FindUnion:
            def __init__(self,n):
                self.parent = list(range(n))
            def find(self,x):
                if self.parent[x] != x:
                    self.parent[x] = self.find(self.parent[x])
                    return self.parent[x]
                return x
            def union(self,x,y):
                xroot,yroot = self.find(x),self.find(y)
                if xroot == yroot:
                    return
                self.parent[yroot] = xroot
        
        n = len(row)>>1
        uf = FindUnion(n)
        for i in range(n):
            uf.union(row[2*i]>>1,row[2*i + 1]>>1)
        ans = 0
        for i in range(n):
            if uf.parent[i] != i:
                ans += 1
        return ans

#爆破法
class Solution:
    def minSwapsCouples(self, row: List[int]) -> int: # 暴力解，异或运算
        result = 0
        for i in range(0, len(row), 2):
            if row[i] == row[i + 1] ^ 1: # 运用异或运算判断是不是一对情侣
                continue
            for j in range(i + 2, len(row), 1): # 如果不是，再进行搜寻
                if row[j] ^ 1 == row[i]: # 搜到了，那么接下来进行座位交换
                    row[i + 1], row[j] = row[j], row[i + 1]
                    result += 1 # 交换次数+1
                    break
        return result # 得到总的交换次数