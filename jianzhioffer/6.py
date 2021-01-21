class BiTNode():
    def __init__(self,data):
        self.data = data
        self.lchild = None
        self.rchild = None

def reConstructTree(pre,mid):
	if not pre or not mid:
		return None
	root = BiTNode(pre[0])
	root_n = mid.index(pre[0])
	
	ltree_pre = pre[1:root_n+1]
	rtree_pre = pre[root_n+1:]

	ltree_mid = mid[0:root_n]
	rtree_mid = mid[root_n+1:]
	root.lchild = reConstructTree(ltree_pre,ltree_mid)
	root.rchild = reConstructTree(rtree_pre,rtree_mid)
	return root

if __name__ == "__main__":
    preOrder = [1,2,4,7,3,5,6,8]
    midOrder = [4,7,2,1,5,3,8,6]
    root = reConstructTree(preOrder,midOrder)
    print(root.lchild.data)
    print(root.rchild.data)
    print(root.lchild.lchild.data)
    print(root.rchild.lchild.data)
    print(root.rchild.rchild.data)
    print(root.lchild.lchild.rchild.data)
    print(root.rchild.rchild.lchild.data)




