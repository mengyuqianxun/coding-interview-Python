def move_num(rows,cols,k):
	visited = [False]*(rows*cols)
	nums = moveCore(0,0,rows,cols,k,visited)
	return nums

def moveCore(row,col,rows,cols,k,visited):
	count = 0
	if row>=0 and row<rows and col>=0 and col<cols and \
	count_sum(row,col)<=k and not visited[row*cols+col]:
		visited[row*cols+col] = True
		count = 1 + moveCore(row-1,col,rows,cols,k,visited)+ \
					moveCore(row+1,col,rows,cols,k,visited)+ \
					moveCore(row,col-1,rows,cols,k,visited)+ \
					moveCore(row,col+1,rows,cols,k,visited)
	return count

def count_sum(a,b):
	'''
	计算两个数字各位数之和
	'''
	sum_ab = 0
	while a > 0:
		sum_ab += (a%10)
		a = a//10
	while b > 0:
		sum_ab += (b%10)
		b = b//10
	return sum_ab

if __name__ == '__main__':
	num = move_num(10,10,5)
	print(num)
	