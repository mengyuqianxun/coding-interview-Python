##只显示了出现次数，没有除以6^n
#solution1
def printProb(n):
	if n < 1:
		return
	maxSum = 6*n
	probList = [0]*(maxSum - n + 1)
	Prob(n,n,0,probList)
	for i in range(len(probList)):
		print('{0}:{1}'.format(i+n,probList[i]),end = ' ')
	print('\n')

def Prob(n,cur,sum_n,probList):
	if cur == 0:
		probList[sum_n - n] += 1
	else:
		for i in range(1,7):
			Prob(n,cur - 1,i + sum_n,probList)

#solution2
def sol2(n):
	arr = [0]*(6*n+1)
	for i in range(1,7):
		arr[i] = 1
	if n == 1:
		return arr
	flag = 2
	while flag <= n:
		for i in range(flag*6,flag*1-1,-1):
			arr[i] = 0
			if i >= 6:
				for j in range(i-6,i):
					arr[i] += arr[j]
			else:
				for j in range(i-1,0,-1):
					arr[i] += arr[j]
		for i in range(0,flag*1):
			arr[i] = 0
		flag += 1
	return arr

def printProb2(n):
	arr = sol2(n)
	for i in range(n,6*n+1):
		print('{0}:{1}'.format(i,arr[i]),end = ' ')
	print('\n')	

if __name__ == '__main__':
	n = 6
	printProb(n)
	printProb2(n)