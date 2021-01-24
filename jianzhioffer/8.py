'''
实现栈
functions:
	isEmpty()
	size()
	push(item)
	pop()
	top()
'''
#1数组实现
class Stack1():
	def __init__(self):
		self.items = []
	#判断栈是否为空
	def isEmpty(self):
		return len(self.items)== 0
	#获取栈中元素个数
	def size(self):
		return len(self.items)
	#压栈
	def push(self,item):
		self.items.append(item)
	#弹栈
	def pop(self):
		if not self.isEmpty():
			return self.items.pop()
		else:
			print('栈已经为空，弹栈失败')
			return None
	#取栈顶元素
	def top(self):
		if not self.isEmpty():
			return self.items[-1]
		else:
			return None

#2链表实现
class LNode:
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack2():
	def __init__(self):
		self.items = None
		self.next = None
	#判断栈是否为空
	def isEmpty(self):
		return self.next == None
	#获取栈中元素个数
	def size(self):
		n = 0
		p = self.next
		while p!=None:
			p = p.next
			n += 1
		return n
	#压栈
	def push(self,item):
		p = LNode(item)
		p.next = self.next
		self.next = p
	#弹栈
	def pop(self):
		if not self.isEmpty():
			tmp = self.next
			self.next = tmp.next
			return tmp.data
		else:
			print('栈已经为空，弹栈失败')
			return None
	#取栈顶元素
	def top(self):
		if not self.isEmpty():
			return self.next.data
		else:
			return None

if __name__=="__main__":
    s1 = Stack1()
    s1.push(4)
    print('栈顶元素为：'+ str(s1.top()))
    print('栈大小为：'+ str(s1.size()))
    s1.pop()
    print('弹栈成功')
    s1.pop()
    print('******'*6)
    s2 = Stack2()
    s2.push(4)
    print('栈顶元素为：'+ str(s2.top()))
    print('栈大小为：'+ str(s2.size()))
    s2.pop()
    print('弹栈成功')
    s2.pop()

