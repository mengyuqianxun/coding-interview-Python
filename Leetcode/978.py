class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 1
        if len(arr) == 0:
            return 0
        tmp = arr[1] - arr[0]
        if tmp == 0:
            maxlen = 1
        else:
            maxlen = curlen = 2
        for i in range(2,len(arr)):
            if tmp == 0:
                curlen = 1
            elif arr[i] - arr[i - 1] == 0:
                curlen = 0
            else:
                if curlen < 2:
                    curlen = 2
            if tmp * (arr[i] - arr[i - 1]) < 0:
                curlen += 1
            elif tmp * (arr[i] - arr[i - 1]) > 0:
                curlen = 2
            if maxlen < curlen:
                maxlen = curlen
            tmp = arr[i] - arr[i - 1]
        return maxlen