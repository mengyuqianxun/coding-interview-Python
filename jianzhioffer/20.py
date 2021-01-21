def count1(n):
	count = 0
	while n:
		if n&1:
			count += 1
			n >>= 1
	return count

def count2(n):
    if n < 0:
        s = bin(n & 0xffffffff)
    else:
        s = bin(n)
    return s.count('1')

def count3(n):
	count = 0
	while n:
		count += 1
		n = (n-1)&n
	return count

if __name__ == '__main__':
	print(count1(3),end="\n")
	print(count2(3),end="\n")
	print(count3(3))
