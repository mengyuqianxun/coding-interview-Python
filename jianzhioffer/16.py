def constructRotateArr(arr,k):
	'''
	arr:递增排序数组
	k：旋转位置,第k个元素
	'''
	a = []
	a += arr[k-1:]
	a += arr[0:k-1]
	return a

def findMin(arr):
	'''
	二分查找通常用两个指针作为辅助来进行位置更新
	这里使用k和p2进行比较，可以兼容未旋转的初始数组
	'''
	p1,p2 = 0,len(arr)-1
	while p1 < p2:
		k = p1 + (p2-p1)//2
		if arr[k] > arr[p2]:
			p1 = k + 1
		elif arr[k] < arr[p2]:
			p2 = k
		#为[1,0,1,1,1]和[1,1,1,0,1]添加的分支
		else:
			for i in range(k+1,p2):
				if arr[i] < arr[p2]:
					p2 = i
					p1 = p2
					break
			if p1 != p2:
				p2 = k
	return arr[p2]

if __name__ == '__main__':
	'''
	升序数组本身
	升序数组的一个旋转，有重复数字，没有重复数字
	只包含一个数字的数组

	最难的是[1,0,1,1,1]和[1,1,1,0,1]
	'''
	arr1 = [2,3,5,6,8,9,12,16]
	arr2 = constructRotateArr(arr1,4)
	arr3 = [1]
	arr4 = [1,0,1,1,1]
	arr5 = [1,1,1,0,1]
	a1 = findMin(arr1)
	a2 = findMin(arr2)
	a3 = findMin(arr3)
	a4 = findMin(arr4)
	a5 = findMin(arr5)
	print(a1,a2,a3,a4,a5)


