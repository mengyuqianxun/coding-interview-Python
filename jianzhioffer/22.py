#字符串模拟数字加法
def SpecialPrint(n):
	if n <= 0:
		return 
	number = ['0']*n
	while not Increment(number):
		PrintNumber(number)

def Increment(number):
    isOverflow = False
    nTakeOver = 0
    for i in range(len(number)-1, -1, -1):
        nSum = int(number[i]) + nTakeOver
        if i == len(number) - 1:
            nSum += 1
        if nSum >= 10:
            if i == 0:
                isOverflow = True
            else:
                nSum -= 10
                nTakeOver = 1
                number[i] = str(nSum)
        else:
            number[i] = str(nSum)
            break
    return isOverflow

def PrintNumber(number):
	'''打印表示数字的字符串，省略前面的0
	number：表示数字的字符串
	'''
	for i in range(len(number)):
		if number[i] != '0':
			start = i
			break
	for i in range(start,len(number)):
		print(number[i],end='')
	print('\t')

if __name__ == '__main__':
	SpecialPrint(2)