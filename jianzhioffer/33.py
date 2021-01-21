def CountPairs(arr):
	count = 0
	result,count = InversePairs(arr,count)
	return result,count

def InversePairs(arr,count):
	if len(arr) <= 1:
		return arr,count
	mid = len(arr)>>1
	a,count = InversePairs(arr[:mid],count)
	b,count = InversePairs(arr[mid:],count)
	result,count = Merge(a,b,count)
	return result,count

def Merge(a,b,count):
	result = []
	p1 = len(a)-1
	p2 = len(b)-1
	while p1>=0 and p2>=0:
		if a[p1] > b[p2]:
			count += (p2+1)
			result.append(a[p1])
			p1 -= 1
		else:
			result.append(b[p2])
			p2 -= 1
	if p1 >= 0:
		#此处不能使用a[p1:-1:-1]，中间的-1会被认为是最后一个值
		result += a[p1::-1]
	else:
		result += b[p2::-1]
	result.reverse()
	return result,count

if __name__ == '__main__':
	arrs = [[7,5,6,4,8],[7,5,6,6,4],[5]]
	for i in arrs:
		_,nums = CountPairs(i)
		print(nums,end = " ")