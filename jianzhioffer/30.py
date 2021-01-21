#1.辅助空间为二维
def FindMaxValue1(gift):
	row,col = len(gift),len(gift[0])
	path = [[0]*col for _ in range(row)]
	for i in range(row):
		for j in range(col):
			if i == 0 and j == 0:
				path[i][j] = gift[i][j]
			elif i == 0:
				path[i][j] = gift[i][j] + path[i][j-1]
			elif j == 0:
				path[i][j] = gift[i][j] + path[i-1][j]
			else:
				path[i][j] = max(path[i-1][j],path[i][j-1]) + gift[i][j]
	return path[-1][-1]

#2.辅助空间为一维
def FindMaxValue2(gift):
	row,col = len(gift),len(gift[0])
	path = [0]*col
	for i in range(row):
		for j in range(col):
			if i == 0 and j == 0:
				path[j] = gift[i][j]
			elif i == 0:
				path[j] = gift[i][j] + path[j-1]
			elif j == 0:
				path[j] = gift[i][j] + path[j]
			else:
				path[j] = max(path[j],path[j-1]) + gift[i][j]
	return path[-1]

if __name__ == '__main__':
	gift =[[1,10,3,8],[12,2,9,6],\
	[5,7,4,11],[3,7,16,5]]
	max_gift1 = FindMaxValue1(gift) 
	print(max_gift1)
	max_gift2 = FindMaxValue2(gift) 
	print(max_gift2)