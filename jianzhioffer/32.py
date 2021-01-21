def solution1(n):
	flag,num = 0,0
	while flag<n:
		num += 1
		if  isUgly(num):
			flag += 1
	return num

def isUgly(num):
	while num % 2 == 0:
		num /= 2
	while num % 3 == 0:
		num /= 3
	while num % 5 == 0:
		num /= 5
	return num == 1

def solution2(n):
	arr = [1,2,3,4,5,6]
	if n <= len(arr):
		return arr[n-1]
	for _ in range(n-6):
		t2,t3,t5 = 0,0,0
		for i in range(len(arr)-1):
			if 2*arr[i] <= arr[-1] < 2*arr[i+1]:
				t2 = i+1
			if 3*arr[i] <= arr[-1] < 3*arr[i+1]:
				t3 = i+1
			if 5*arr[i] <= arr[-1] < 5*arr[i+1]:
				t5 = i+1
			if t2 and t3 and t5:
				break
		add = min(min(2*arr[t2],3*arr[t3]),5*arr[t5])
		arr.append(add)
	return arr[n-1]

if __name__ == '__main__':
	nums = [1,2,4,7,10,20]
	for i in nums:
		num = solution1(i)
		print(num,end = ' ')
	#solution1计算1500非常慢
	print('\n')
	nums.append(1500)
	for i in nums:
		num = solution2(i)
		print(num,end = ' ')