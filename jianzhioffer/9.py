'''
实现队列
functions:
	isEmpty()
	size()
	addQueue(item)
	deQueue()
	getFront()
	getBack()
'''
#1.数组实现
class Queue1():
	def __init__(self):
		self.items = []
		self.front = 0
		self.rear = 0
	#判断队列是否为空
	def isEmpty(self):
		return self.front == self.rear
	#获取队列中元素个数
	def size(self):
		return self.rear - self.front
	#元素入队列:添加到队尾
	def addQueue(self,item):
		self.items.append(item)
		self.rear += 1
	#元素出队列：删除队首元素
	def deQueue(self):
		if not self.isEmpty():
			self.front += 1
		else:
			print('队列为空，出队列失败')
			return None
	#获取队首元素
	def getFront(self):
		if not self.isEmpty():
			return self.items[self.front]
		else:
			return None
	#获取队尾元素
	def getBack(self):
		if not self.isEmpty():
			return self.items[self.rear-1]
		else:
			return None

#2.链表实现
class LNode():
	def __init__(self,data):
		self.data = data
		self.next = None

class Queue2():
	def __init__(self):
		self.front = None
		self.rear = None
	#判断队列是否为空
	def isEmpty(self):
		return self.front == None
	#获取队列中元素个数
	def size(self):
		n = 0
		p = self.front
		while p != None:
			p = p.next
			n += 1
		return n
	#元素入队列:添加到队尾
	def addQueue(self,item):
		tmp = LNode(item)
		if self.front == None:
			self.front = self.rear = tmp
		else:
			self.rear.next = tmp
			self.rear = tmp
	#元素出队列：删除队首元素
	def deQueue(self):
		if not self.isEmpty():
			self.front = self.front.next
		else:
			print('队列为空，出队列失败')
			return None
	#获取队首元素
	def getFront(self):
		if not self.isEmpty():
			return self.front.data
		else:
			return None
	#获取队尾元素
	def getBack(self):
		if not self.isEmpty():
			return self.rear.data
		else:
			return None

if __name__ == "__main__":
    queue1 = Queue1()
    queue1.addQueue(1)
    queue1.addQueue(2)
    print(u'队列头元素为：'+str(queue1.getFront()))
    print(u'队列尾元素为:'+str(queue1.getBack()))
    print(u'队列大小为:'+str(queue1.size()))
    queue1.deQueue()
    queue1.deQueue()
    queue1.deQueue()

    print('******'*6)    

    queue2 = Queue2()
    queue2.addQueue(1)
    queue2.addQueue(2)
    print(u'队列头元素为：'+str(queue2.getFront()))
    print(u'队列尾元素为:'+str(queue2.getBack()))
    print(u'队列大小为:'+str(queue2.size()))
    queue2.deQueue()
    queue2.deQueue()
    queue2.deQueue()
