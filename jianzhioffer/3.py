def solution(array,number):
	if number > array[-1][-1] or number < array[0][0]:
		return False
	row = 0
	col = len(array[0])-1
	while row < len(array) and col >= 0:
		if array[row][col] == number:
			return True
		elif array[row][col] > number:
			col -= 1
		else:
			row += 1
	return False

if __name__ == "__main__":
	array = [[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]
	number = [5,7,20]
	for i in range(len(number)):
		print(solution(array,number[i]),end = ' ')

