class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        winsize = n - k
        s = sum(cardPoints[:winsize])
        minsum = s
        for i in range(winsize,n):
            s = s + cardPoints[i] - cardPoints[i - winsize]
            minsum = min(s,minsum)
        return sum(cardPoints) - minsum