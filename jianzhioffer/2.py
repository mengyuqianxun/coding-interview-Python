def solution(array):
	if len(array) == 0:
		print('数组为空')
	for i in range(len(array)):
		if array[i] < 1 or array[i] > len(array) -1:
			print('出现异常元素')
			return None
	start = 1
	end = len(array) - 1
	while start <= end:
		middle = int((end - start)/2) + start
		count = countRange(array,start,middle)
		if start == end:
			if count > 1:
				return start
			else:
				print('error')
				return None
		else:
			if count > middle-start+1:
				end = middle
			else:
				start = middle+1
	return None

def countRange(array,start,end):
	if array == None:
		return 0
	count = 0
	for i in range(len(array)):
		if array[i] >= start and array[i] <= end:
			count += 1
	return count

if __name__ == "__main__":
	array = [[2,3,5,4,3,2,6,7],[0,1,2,3,4,5,6,7],\
	[]]
	for i in range(len(array)):
		output = solution(array[i])
		print(output)
		print("---"*6)

