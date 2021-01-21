def ResortList(List):
	if List == None:
		print('数组为空')
		return None
	newList = List.copy()
	pre = 0
	nex = len(newList)-1
	while pre < nex:
		while pre < nex and (newList[pre] & 0x1 == 1):
			pre += 1
		while pre < nex and (newList[nex] & 0x1 == 0):
			nex -= 1
		newList[pre],newList[nex] = newList[nex],newList[pre]
	return newList

#可扩展函数
def ResortList2(List,func):
	if List == None:
		print('数组为空')
		return None
	newList = List.copy()
	pre = 0
	nex = len(newList)-1
	while pre < nex:
		while pre < nex and func(newList[pre]):
			pre += 1
		while pre < nex and not func(newList[nex]):
			nex -= 1
		newList[pre],newList[nex] = newList[nex],newList[pre]
	return newList

def isOdd(n):
	return (n & 0x1 == 1)


if __name__ == '__main__':
	List = [1,2,3,4,5,6]
	print(List)
	newList = ResortList2(List,isOdd)
	print(newList)
	newList = ResortList2(List,isOdd)
	print(newList)