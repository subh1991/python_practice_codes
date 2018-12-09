class Node():
	def __init__(self, val = 0, left = None, right = None):
		self.val = val
		self.left = left
		self.right = right

class Tree():
	def __init__(self):
		self.root = None
	
	def insert_(self, current_node, val):
		if current_node.val < val:
			if current_node.right == None:
				current_node.right = Node(val)
			else:
				self.insert_(current_node.right, val)
		elif current_node.val > val:
			if current_node.left == None:
				current_node.left = Node(val)
			else:
				self.insert_(current_node.left, val)

	def insert(self, val):
		if self.root == None:
			self.root = Node(val)
			return
		current_node = self.root
		self.insert_(current_node, val)

def print_inorder(root):
	if root:
		print_inorder(root.left)
		print root.val
		print_inorder(root.right)
	
def print_preorder(root):
	if root:
		print root.val
		print_preorder(root.left)
		print_preorder(root.right)

def print_postorder(root):
	if root:
		print_postorder(root.left)
		print_postorder(root.right)
		print root.val

def sortedArr2BST(arr):
	if not arr:
		return
	mid = len(arr) / 2
	root = Node(arr[mid])
	root.left = sortedArr2BST(arr[:mid])
	root.right = sortedArr2BST(arr[mid+1:])
	return root

def lowestValInTree(root):
	while True:
		if root.left is None:
			return root
		root = root.left

def deleteNode(root, val):
	if root is None:
		return root
	if val < root.val:
		root.left = deleteNode(root.left, val)
	elif val > root.val:
		root.right = deleteNode(root.right, val)
	else:
		if root.left == None:
			temp = root.right
			root = None
			return temp
		elif root.right == None:
			temp = root.left
			root = None
			return temp

		temp = lowestValInTree(root.right)
		root.val = temp.val
		deleteNode(root.right, temp.val)
	return root
	

def main():
	print "Hello World"
#	tree = Tree()
#
#	tree.insert(5)
#	tree.insert(3)
#	tree.insert(2)
#	tree.insert(4)
#	tree.insert(7)
#	tree.insert(6)
#	tree.insert(8)
#
#	print "inorder..."
#	print_inorder(tree.root)
#	print "preorder..."
#	print_preorder(tree.root)
#	print "postorder..."
#	print_postorder(tree.root)

def main2():
	root = sortedArr2BST([2,3,4,5,7,8,9,10,11,12,13])
	print "inorder..."
	print_inorder(root)
	deleteNode(root, 10)
	print "deleted inorder..."
	print_inorder(root)
	deleteNode(root, 5)
	print "deleted inorder..."
	print_inorder(root)
#	print "preorder..."
#	print_preorder(root)
#	print "postorder..."
#	print_postorder(root)

def inorder_no_rec(root):
        node_stack = []
        l = []
        current_node = root
        while True:
            if current_node is not None:
                node_stack.append(current_node)
                current_node = current_node.left
            else:
                a = node_stack.pop()
                l.append(a.val)
                print l
                current_node = a.right
            if current_node is None and node_stack == []:
                break

def postorder_no_rec(root):
        node_stack = []
        l = []
        current_node = root
        while True:
            if current_node is not None:
                node_stack.append(current_node)
                current_node = current_node.left
            else:
                a = node_stack.pop()
                l.append(a.val)
                print l
                current_node = node_stack[-1].right
            if current_node is None and node_stack == []:
                break

def main3():
	root = sortedArr2BST([2,1,3,4,5])
	inorder_no_rec(root)
	postorder_no_rec(root)

if __name__ == "__main__":
	main3()
















