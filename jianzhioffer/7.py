class BiTNode():
    def __init__(self,data):
        self.data = data
        self.lchild = None
        self.rchild = None
        self.father = None

def constructTree():
    node1,node2,node3,node4 = [BiTNode(i) for i in ['a','b','c','d']]
    node5,node6,node7,node8,node9 = [BiTNode(i) for i in ['e','f','g','h','i']]
    node1.lchild,node1.rchild = node2,node3
    node2.lchild = node4
    node2.rchild = node5
    node3.lchild,node3.rchild = node6,node7
    node5.lchild,node5.rchild = node8,node9

    node2.father,node3.father = node1,node1
    node4.father,node5.father = node2,node2
    node6.father,node7.father = node3,node3  
    node8.father,node9.father = node5,node5
    return node1

def findNextNode(node):
	if node == None:
		return None
	if node.rchild != None:
		node = node.rchild
		while node.lchild != None:
			node = node.lchild
		return node
	else:
		while node.father != None:
			if node.father.lchild == node:
				return node.father
			node = node.father
		print('没有下一个节点')
		return None


if __name__ =='__main__':
	root = constructTree()
	node1 = findNextNode(root)
	print(root.data + '的下一个节点是：' + node1.data)
	node2 = findNextNode(root.lchild.lchild)
	print(root.lchild.lchild.data + '的下一个节点是：' + node2.data)
	node3 = findNextNode(root.lchild.rchild.rchild)
	print(root.lchild.rchild.rchild.data + '的下一个节点是：' + node3.data)
	node4 = findNextNode(root.rchild.rchild)
	
