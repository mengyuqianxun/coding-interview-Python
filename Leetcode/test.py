from typing import List
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        sumcus = sum(c for c,g in zip(customers,grumpy) if g == 0)
        maxincrease = tmp = sum(c*g for c,g in zip(customers[:X],grumpy[:X]))
        for i in range(X,len(customers)):
        	tmp = tmp + customers[i]*grumpy[i] - customers[i-X]*grumpy[i-X]
        	maxincrease = max(tmp,maxincrease)
        return sumcus + maxincrease

if __name__ == '__main__':
	sol = Solution()
	arr1 = [1,0,1,2,1,1,7,5]
	arr2 = [0,1,0,1,0,1,0,1]
	X = 3
	ans = sol.maxSatisfied(arr1,arr2,X)
	print(ans)