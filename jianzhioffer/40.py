def printSumS(s):
	if s < 3:
		print('s过小')
	small,big = 1,2
	curSum = small + big
	while small <= s>>1:
		if curSum == s:
			printa2b(small,big)
			curSum -= small
			small += 1
		elif curSum > s:
			curSum -= small
			small += 1
		else:
			big += 1
			curSum += big

def printa2b(a,b):
	for i in range(a,b+1):
		print(i,end=',')
	print('\n')

if __name__ == '__main__':
	ss = [1,2,3,4,15,30]
	for s in ss:
		printSumS(s)
		print('*******')
