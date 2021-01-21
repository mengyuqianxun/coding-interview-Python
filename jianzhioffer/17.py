def hasPath(matrix,rows,cols,path):
	if matrix == None or rows<1 or cols<1 or path==None:
		return False
	visited = [0]*(rows*cols)

	pathLength = 0
	for row in range(rows):
		for col in range(cols):
			if hasPathCore(matrix,rows,cols,row,col,path,pathLength,visited):
				return True
	return False

def hasPathCore(matrix,rows,cols,row,col,path,pathLength,visited):
	if pathLength == len(path):
		return True
	has = False 
	if row>=0 and row<rows and col>=0 and col<cols and \
	matrix[row*cols+col] == path[pathLength] and \
	not visited[row*cols+col]:
		pathLength += 1
		visited[row*cols+col] = True
		has = hasPathCore(matrix,rows,cols,row-1,col,path,pathLength,visited) or \
		hasPathCore(matrix,rows,cols,row+1,col,path,pathLength,visited) or \
		hasPathCore(matrix,rows,cols,row,col-1,path,pathLength,visited) or \
		hasPathCore(matrix,rows,cols,row,col+1,path,pathLength,visited)
		if not has:
			pathLength -= 1
			visited[row*cols+col] = False
	return has


if __name__ == '__main__':
	matrix1 = 'ABCESFCSADEF'
	rows1,cols1 = 3,4
	path1 = 'ABCCED'
	print(hasPath(matrix1,rows1,cols1,path1))
	matrix2 = 'abtgcfcsjdeh'
	rows2,cols2 = 3,4
	path2 = 'bfce'	
	path3 = 'abfb'
	print(hasPath(matrix2,rows2,cols2,path2))
	print(hasPath(matrix2,rows2,cols2,path3))

