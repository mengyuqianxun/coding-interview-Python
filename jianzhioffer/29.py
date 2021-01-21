def CountTranslation(num):
	if num < 0:
		return 0
	s = str(num)
	arr = [0]*(len(s)+1)
	arr[-1] = 1
	for i in range(len(s)-1,-1,-1):
		if i == len(s) - 1:
			arr[i] = arr[i+1]
		if i < len(s) - 1:
			if '10' <= s[i]+s[i+1] <= '25':
				arr[i] = arr[i+1] + arr[i+2]
			else:
				arr[i] = arr[i+1]
	return arr[0]

if __name__ == '__main__':
	num = [5,25,26,12258]
	for i in num:
		count = CountTranslation(i)
		print(count,end=' ') 