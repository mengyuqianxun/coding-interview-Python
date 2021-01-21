#假设二进制有32位
def FindSingleNum(arr):
	bitSum = [0]*32
	for i in range(len(arr)):
		bitMask = 1
		for j in range(32):
			if bitMask & arr[i] != 0:
				bitSum[j] += 1
			bitMask <<= 1
	result = 0
	for i in range(31,-1,-1):
		result <<= 1
		result += bitSum[i]%3
	return result

if __name__ == '__main__':
	arr = [2,5,2,4,3,4,6,4,3,2,5,3,5]
	num = FindSingleNum(arr)
	print(num)