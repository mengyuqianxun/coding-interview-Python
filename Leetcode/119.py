class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = [1]
        for length in range(1, rowIndex+1):
            tmp = [1]
            for i in range(1, length):
                tmp.append(ans[i] + ans[i-1])
            tmp.append(1)
            ans = tmp
        return ans