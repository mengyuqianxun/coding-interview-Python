def MergeSort(arr):
	if len(arr) <= 1:
		return arr
	mid = len(arr)//2
	a = MergeSort(arr[:mid])
	b = MergeSort(arr[mid:])
	return Merge(a,b)

def Merge(a,b):
	'''合并两个排好序的数组'''
	result = []
	i,j = 0,0
	while i < len(a) and j < len(b):
		if a[i] < b[j]:
			result.append(a[i])
			i += 1
		else:
			result.append(b[j])
			j += 1
	if i == len(a):
		result += b[j:]
	else:
		result += a[i:]
	return result

if __name__ == '__main__':
	array = [47,29,71,99,78,19,24,47,1]
	array = MergeSort(array)
	for i in range(len(array)):
		print(array[i],end = ' ')
	print('\n')