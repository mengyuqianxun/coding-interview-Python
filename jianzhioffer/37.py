def FindCertainNums(arr):
	if arr == None or len(arr)<2:
		return None
	tmp = 0
	for i in arr:
		tmp ^= i
	tmp = CreateJudge(tmp)
	a,b = 0,0
	for j in arr:
		if tmp & j:
			a ^= j
		else:
			b ^= j
	return a,b

def CreateJudge(num):
	tmp = 1
	while True:
		if tmp&num:
			break
		else:
			tmp <<= 1
	return tmp

if __name__ == '__main__':
	arr = [2,4,3,6,3,2,5,5]
	a,b = FindCertainNums(arr)
	print(a,b)