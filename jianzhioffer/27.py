#1.低时间效率
def CountNum1Times1(n):
	sums = 0
	for i in range(1,n+1):
		sums += CountNumof1(i)
	return sums

def CountNumof1(n):
	count = 0
	while n >= 10:
		if n % 10 == 1:
			count += 1
		n //= 10
	if n == 1:
		count += 1
	return count

#2.数学规律
def CountNum1Times2(n):
	if n <= 0:
		return None
	s = str(n)
	return Numof1(s)

def Numof1(s):
	#假设是21345
	if len(s) == 1 and s[0] != '0':
		return 1
	if len(s) == 1 and s[0] == '0':
		return 0
	if s[0] != '0':
		if s[0] > '1':
			tmp = 10**(len(s)-1)
		if s[0] == '1':
			tmp = int(s[1:]) + 1
		tmp += int(s[0])*(len(s)-1)*(10**(len(s)-2))
		num = Numof1(s[1:]) + tmp
	else:
		num = Numof1(s[1:])
	return num

if __name__ == '__main__':
	num1 = CountNum1Times1(21345)
	num2 = CountNum1Times2(21345)
	print(num1,num2)
