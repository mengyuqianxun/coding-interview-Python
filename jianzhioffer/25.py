#1.快速查找法
def MoreThanHalfNum1(array):
	if array == None:
		return None
	middle = len(array)>>1
	start = 0
	end = len(array) - 1
	index = Partition(array,start,end)
	while index != middle:
		if index > middle:
			end = index - 1
			index = Partition(array,start,end)
		else:
			start = index + 1
			index = Partition(array,start,end)
	return array[index]

#比array[end]大的在右边，小的在左边，输出该数调整后的位置
def Partition(array,start,end):
	k = array[end]
	i = start - 1
	for j in range(start,end):
		if array[j] <= k:
			i += 1
			array[i],array[j] = array[j],array[i]
	array[i+1],array[end] = array[end],array[i+1]
	return i+1

#2.数组特点法
def MoreThanHalfNum2(array):
	num = array[0]
	time = 1
	for i in range(1,len(array)):
		if time == 0:
			num = array[i]
			time = 1
		else:
			if array[i] == num:
				time += 1
			else:
				time -= 1
	return num

if __name__ == '__main__':
	array = [1,2,3,2,2,5,4,2]
	num1 = MoreThanHalfNum1(array)
	num2 = MoreThanHalfNum2(array)
	print(num1,num2)

