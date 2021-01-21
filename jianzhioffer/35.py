def FindLostNum(arr):
	if arr == None:
		return -1
	start = 0
	end = len(arr)-1
	while start <= end:
		mid = (start + end)>>1
		if arr[mid] == mid:
			start = mid + 1
		else:
			if mid == 0 or arr[mid-1] == mid-1:
				return mid
			else:
				end = mid-1
	if start == len(arr):
		return start
	return -1

if __name__ == '__main__':
	arrs = [[0,1,2,3,4,6],[1,2,3,4],[0,1,2,3,4],[0],[1]]
	for i in arrs:
		num = FindLostNum(i)
		print(num,end=' ') 