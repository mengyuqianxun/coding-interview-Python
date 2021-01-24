def solution1(array):
	array = sorted(array)
	if array[0]< 0 or array[-1]>= len(array):
		print("出现异常数字")
		return None

	for i in range(len(array)-1):
		if array[i] == array[i+1]:
			return array[i]
	print("没有重复元素")
	return None


def solution2(array):
	dic = {}
	a = None
	for i in range(len(array)):
		if array[i] >= len(array) or array[i]<0:
			print("出现异常值")
			return None
		if array[i] not in dic:
			dic[array[i]] = i
		else:
			a = array[i]
	if a != None:
		return a
	else:
		print("没有重复元素")
		return None

def solution3(array):
	for i in range(len(array)):
		if array[i] < 0 or array[i] >= len(array):
			print("出现异常值")
			return None
		while array[i] != i:
			if array[array[i]] == array[i]:
				return array[i]
			tmp = array[i]
			array[i] = array[tmp]
			array[tmp] = tmp
	print("没有重复元素")
	return None

if __name__ == "__main__":
	array = [[2,3,1,0,2,5,3],[0,1,2,3,4,5,6],\
	[2,3,5,1,16,6,0]]
	for i in range(len(array)):
		output = solution3(array[i])
		print(output,end=' ')