class Node:
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None

	def __str__(self):
		return str(self.data)

class ArvoreBinaria:
	def __init__(self,data=None):
		if data:
			node = Node(data)
			self.root = node
		else:
			self.root = None

	def simetric_traversal(self, node=None):
		if node is None:
			node = self.root
		if node.left:
			print("(", end = "")
			self.simetric_traversal(node.left)
		print(node, end = "")
		if node.right:
			self.simetric_traversal(node.right)
			print(")", end = "")

	def postorder_traversal(self, node=None):
		if node is None:
			node = self.root
		if node.left:
			self.postorder_traversal(node.left)
		if node.right:
			self.postorder_traversal(node.right)
		print(node)

def postorder_example_tree():
	arvore = ArvoreBinaria()
	n1 = Node('I')
	n2 = Node('N')
	n3 = Node('S')
	n4 = Node('C')
	n5 = Node('R')
	n6 = Node('E')
	n7 = Node('V')
	n8 = Node('A')
	n9 = Node('5')
	n0 = Node('3')

	n0.left = n6
	n0.right = n9
	n6.left = n1
	n6.right = n5
	n5.left = n2
	n5.right = n4
	n4.right = n3
	n9.left = n8
	n8.right = n7

	arvore.root = n0
	return arvore

if __name__ == '__main__':
	arvore = postorder_example_tree()
	print("Percurso em pós ordem:")
	arvore.postorder_traversal()
	