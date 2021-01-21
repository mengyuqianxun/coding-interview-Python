def NumEqualIndex(arr):
	if len(arr) == 1:
		if arr[0] == 0:
			return 0
		else:
			return None
	if arr[-1] <= 0 or arr[0] >= len(arr)-1:
		return None
	start = 0
	end = len(arr)-1
	while start <= end:
		mid = (start + end)>>1
		if arr[mid] == mid:
			return mid
		elif arr[mid] < mid:
			start = mid + 1
		else:
			end = mid -1
	return None

if __name__ == '__main__':
	arrs = [[-3,-1,1,3,5],[-3,-1,1,4,6],\
	[0],[1],[0,3,5],[-3,-1,1,2,4]]
	for i in arrs:
		num = NumEqualIndex(i)
		print(num,end=' ')