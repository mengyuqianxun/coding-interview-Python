matrix = [[1,2],[3,4],[5,6]]
m,n = len(matrix), len(matrix[0])
# 建立
pre = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

for i in range(1, m+1):
    for j in range(1, n+1):
        pre[i][j] = pre[i-1][j]+ pre[i][j-1] - pre[i-1][j-1] + matrix[i-1][j-1]

print(matrix,pre)

