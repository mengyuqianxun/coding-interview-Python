class Solution(object):
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        diff = sum(A) - sum(B)
        a = set(A)
        for y in B:
            x = y + diff//2
            if x in a:
                return [x,y]