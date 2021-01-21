#省略将扑克牌转化为数字的过程,假设输入合法且非空
def isContinues(arr):
	arr.sort()

	zero_num = 0
	for i in range(0,len(arr)):
		if arr[i] != 0:
			break
		zero_num += 1
	if zero_num >= len(arr) - 1:
		return True
	
	cur = zero_num
	gap_num = 0
	while cur < len(arr)-1:
		if arr[cur] == arr[cur + 1]:
			return False
		gap_num += (arr[cur+1]-arr[cur]-1)
		cur += 1
	return True if gap_num<=zero_num else False


if __name__ == '__main__':
	arrs = [[4,5,1,3,0],[3,1,7,0,0],[0,0,0,0,0],\
	[6,9,8,7,10],[12,12,10,11,9]]
	for arr in arrs:
		print(isContinues(arr),end = ' ')