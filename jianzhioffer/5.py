class LNode:
	def __init__(self,x):
		self.data = x
		self.next = None

def print_list(head):
    stack = []
    while head != None:
        stack.append(head.data)
        head = head.next
    print('打印列表:',end = " ")
    while len(stack) > 0:
        print(stack.pop(),end = " ")

def print_Recursive(head):
	if head != None:
		print_Recursive(head.next)
		print(head.data,end = ' ')

if __name__ == "__main__":
	i = 1
	head = LNode(0)
	cur = head
	#构造单链表
	while i<8:
		tmp = LNode(i)
		cur.next = tmp
		cur = tmp
		i += 1
	print('原始链表:',end = " ")
	cur = head.next
	while cur != None:
		print(cur.data,end =" ")
		cur = cur.next
	print('\n')
	print_list(head.next)
	print('\n')

	print('打印列表:',end = " ")
	print_Recursive(head.next)
	print('\n')



