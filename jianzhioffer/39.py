def SumEqualS(arr,s):
	if len(arr)<2:
		return None,None
	start = 0
	end = len(arr)-1
	while start < end:
		if arr[start] + arr[end] == s:
			return arr[start],arr[end]
		elif arr[start] + arr[end] > s:
			end -= 1
		else:
			start += 1
	return None,None

if __name__ == '__main__':
	arr = [1,2,4,7,11,15]
	a,b = SumEqualS(arr,15)
	print(a,b)

