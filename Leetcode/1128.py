#字典存储
class Solution(object):
    def numEquivDominoPairs(self, dominoes):
        """
        :type dominoes: List[List[int]]
        :rtype: int
        """
        d,ans= {},0
        for i,j in dominoes:
            tmp = i*10 + j if i<j else j*10 + i
            d[tmp] = d.get(tmp,0) + 1
            ans += d[tmp] - 1
        return ans

#数组存储
class Solution(object):
    def numEquivDominoPairs(self, dominoes):
        """
        :type dominoes: List[List[int]]
        :rtype: int
        """
        lis,ans = [0]*100,0  
        for i,j in dominoes:
            tmp = i*10 + j if i<j else j*10 + i
            lis[tmp] += 1
            ans += lis[tmp]-1
        return ans