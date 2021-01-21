def InsertSort(arr):
	for i in range(1,len(arr)):
		insert = arr[i]
		j = i-1
		while j >= 0 and arr[j] > insert:
			arr[j+1] = arr[j]
			j -= 1
		arr[j+1] = insert

if __name__ == '__main__':
	array = [47,29,71,99,78,19,24,47]
	InsertSort(array)
	for i in range(len(array)):
		print(array[i],end = ' ')
	print('\n')