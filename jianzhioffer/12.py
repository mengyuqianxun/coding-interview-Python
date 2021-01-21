#1.分片执行的是原列表的复制操作，达不到原地排序的目的，所以需要传上下边界
def QuickSort1(array,start,end): 
	if start >= end:
		return
	k = array[start]
	i,j = start,end
	while i < j:
		while array[j] >= k and i < j:
			j -= 1
		array[j],array[i] = array[i],array[j]
		while array[i] < k and i < j:
			i += 1
		array[i],array[j] = array[j],array[i]
	QuickSort1(array,start,i-1)
	QuickSort1(array,i+1,end)

#2.算法导论中的快速排序
def quick_sort2(array, l, r):
  if l < r:
    q = partition(array, l, r)
    quick_sort2(array, l, q - 1)
    quick_sort2(array, q + 1, r)
  
def partition(array,start,end):
	k = array[end]
	i = start - 1
	for j in range(start,end):
		if array[j] <= k:
			i += 1
			array[i],array[j] = array[j],array[i]
	array[i+1],array[end] = array[end],array[i+1]
	return i+1

if __name__ == '__main__':
	array1 = [47,29,71,99,78,19,24,47]
	array2 = [47,29,71,99,78,19,24,47]
	print(array1)
	QuickSort1(array1,0,len(array1)-1)
	print(array1)
	print(array2)
	quick_sort2(array2,0,len(array2)-1)
	print(array2)