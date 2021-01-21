def BubbleSort(array):
	if len(array) == 0:
		print('数组为空')
		return []
	if len(array) == 1:
		return array
	for i in range(len(array)-1):
		for j in range(len(array)-i-1):
			if array[j] > array[j+1]:
				array[j],array[j+1] = array[j+1],array[j]
	return array


if __name__ == '__main__':
	array = [13,2,8,3,40,3,9,0,7]
	array = BubbleSort(array)
	for i in range(len(array)):
		print(array[i],end = ' ')
	print('\n')

