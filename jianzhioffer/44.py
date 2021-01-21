class LNode:
	def __init__(self,x):
		self.data = x
		self.next = None

def CreateList(n):
	first = LNode(0)
	cur = first
	for i in range(1,n):
		tmp = LNode(i)
		cur.next = tmp
		cur = tmp
	cur.next = first
	return first

#假设m>0
def RemainEle(n,m):
	first = CreateList(n)
	if m == 1:
		return n-1
	while first.next.data != first.data:
		for i in range(m-2):
			first = first.next
		first.next = first.next.next
		first = first.next
	return first.data

def mathSolv(n,m):
	result = 0
	for i in range(2,n+1):
		result = (result + m)%i
	return result

if __name__ == '__main__':
	arrs = [[5,3],[6,7],[5,1],[4000,997]]
	for n,m in arrs:
		num = RemainEle(n,m)
		print(num,end=' ')
	print('\n')
	for n,m in arrs:
		num = mathSolv(n,m)
		print(num,end=' ')
		

