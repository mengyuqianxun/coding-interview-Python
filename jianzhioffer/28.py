def SortMinNum(arr):
	arr = [str(i) for i in arr]
	Quick_sort(arr,0,len(arr)-1)
	num = ''.join(arr)
	return num

def Quick_sort(arr,start,end):
	if start < end:
		middle = Partition(arr,start,end)
		Quick_sort(arr,start,middle-1)
		Quick_sort(arr,middle+1,end)

def Partition(arr,start,end):
	k = arr[end]
	mid = start - 1
	for i in range(start,end):
		if Greater(k,arr[i]):
			mid += 1
			arr[i],arr[mid] = arr[mid],arr[i]
	arr[mid+1],arr[end] = arr[end],arr[mid+1]
	return mid + 1

def Greater(m,n):
	return (m+n)>(n+m)

if __name__ == '__main__':
	arr = [3,32,321]
	num = SortMinNum(arr)
	print(num)
