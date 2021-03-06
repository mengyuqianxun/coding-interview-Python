class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        f = [[True]*n for _ in range(n)]
        for i in range(n-1,-1,-1):
            for j in range(i + 1,n):
                f[i][j] = f[i + 1][j - 1] and (s[i] == s[j])
        res = list()
        ans = list()
        def dfs(i):
            if i == n:
                res.append(ans[:])
                return
            for j in range(i,n):
                if f[i][j]:
                    ans.append(s[i:j+1])
                    dfs(j + 1)
                    ans.pop()
        dfs(0)
        return res