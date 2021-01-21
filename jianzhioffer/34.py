def TimesofNum(arr,k):
	a = getFirstk(arr,k,0,len(arr)-1)
	b = getLastk(arr,k,0,len(arr)-1)
	if a>=0 and b>=0:
		return b-a+1
	else:
		return 0

def getFirstk(arr,k,start,end):
	if start == end-1:
		if arr[start] == k:
			return start
		elif arr[end] == k:
			return end
		else:
			return -1
	mid = (start + end)>>1
	if arr[mid] == k:
		if mid == 0 or arr[mid-1] != k:
			return mid
		else:
			return getFirstk(arr,k,start,mid)
	elif arr[mid] > k:
		return getFirstk(arr,k,start,mid)
	else:
		return getFirstk(arr,k,mid,end)


def getLastk(arr,k,start,end):
	if start == end-1:
		if arr[end] == k:
			return end
		elif arr[start] == k:
			return start
		else:
			return -1
	mid = (start + end + 1)>>1
	if arr[mid] == k:
		if mid == len(arr)-1 or arr[mid+1] != k:
			return mid
		else:
			return getLastk(arr,k,mid,end)
	elif arr[mid]>k:
		return getLastk(arr,k,start,mid)
	else:
		return getLastk(arr,k,mid,end)

if __name__ == '__main__':
	arrs = [[1,2,3,3,3,3,4,5],[3,3,3,3,3],[1,1,1,1,1]]
	for i in arrs:
		times = TimesofNum(i,3)
		print(times,end=' ')
