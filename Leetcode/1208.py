class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n = len(s)
        record = []
        for i in range(n):
            record.append(abs(ord(t[i]) - ord(s[i])))
            
        start, end = 0, 0
        windowsum = 0
        res = 0
        for end in range(n):
            windowsum += record[end]
            while windowsum > maxCost:
                windowsum -= record[start]
                start += 1
            res = max(res, end - start + 1)
        return res