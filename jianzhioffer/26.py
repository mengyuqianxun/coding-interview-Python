def MaxSubArraySum(arr):
	cur_sum = 0
	max_sum = 0
	for i in range(len(arr)):
		if cur_sum < 0:
			cur_sum = 0
		cur_sum += arr[i]
		if cur_sum >= max_sum:
			max_sum = cur_sum
	return max_sum

#动态规划:和上面异曲同工

if __name__ == '__main__':
	arr = [1,-2,3,10,-4,7,2,-5]
	result = MaxSubArraySum(arr)
	print(result)