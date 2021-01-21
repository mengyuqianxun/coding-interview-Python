def ProductArr(arr):
	arr1 = [1]*len(arr)
	arr2 = [1]*len(arr)
	for i in range(2,len(arr1)):
		arr1[i] = arr1[i-1] * arr[i-1]
	for i in range(len(arr2)-2,-1,-1):
		arr2[i] = arr2[i+1] * arr[i+1]
	for i in range(len(arr)):
		arr[i] = arr1[i]*arr2[i]
	return arr

if __name__ == '__main__':
	arr = [1,2,3,4,5]
	b = ProductArr(arr)
	print(b)