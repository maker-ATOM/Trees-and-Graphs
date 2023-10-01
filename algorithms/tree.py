from collections import deque

# Definition for a binary tree node.
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

	
	def print_Inorder(self):
		"""
		Depth First Search Inorder Traversal
		"""
		if self.left is not None:
			self.left.print_Inorder()
		print(self.val, end=" ")
		if self.right is not None:
			self.right.print_Inorder()


	def print_Preorder(self):
		"""
		Depth First Search Preorder Traversal
		"""
		print(self.val, end=" ")
		if self.left is not None:
			self.left.print_Preorder()
		if self.right is not None:
			self.right.print_Preorder()

	def print_Postorder(self):
		"""
		Depth First Search Postorder Traversal
		"""
		if self.left is not None:
			self.left.print_Postorder()
		if self.right is not None:
			self.right.print_Postorder()
		print(self.val, end=" ")

	def print_BFS(self):
		"""
		Breadth First Search Traversal using Queue
		"""
		if not self:
			return []

		result = []
		queue = deque([self])

		while queue:
			level = []
			level_size = len(queue)

			for i in range(level_size):
				node = queue.popleft()

				if node:
					level.append(node.val)
					queue.append(node.left if node.left else None)
					queue.append(node.right if node.right else None)
				else:
					level.append(None)
					queue.append(None) # for left child
					queue.append(None) # for right child

			# Check if all nodes at this level are None (indicating end of tree)
			if all(node is None for node in level):
				break

			result.append(level)

		print(result)

sample_tree = TreeNode(1)
sample_tree.left = TreeNode(2)
sample_tree.right = TreeNode(3)
sample_tree.left.left = TreeNode(4)
sample_tree.left.right = TreeNode(5)
sample_tree.right.left = TreeNode(6)
sample_tree.right.right = TreeNode(7)

"""
     1
   /   \
  2     3
 / \   / \
4   5 6   7

"""


sample_binary_tree = TreeNode(7)
sample_binary_tree.left = TreeNode(4)
sample_binary_tree.right = TreeNode(10)
sample_binary_tree.left.left = TreeNode(2)
sample_binary_tree.left.right = TreeNode(5)
sample_binary_tree.right.left = TreeNode(9)
sample_binary_tree.right.right = TreeNode(12)
sample_binary_tree.left.left.left = TreeNode(1)
sample_binary_tree.right.right.right = TreeNode(13)

"""
		     7
		   /   \
		  4     10
		 / \   /  \
		2   5 9   12
	   /			\
      1				13
"""


if __name__ == '__main__':
	print("DFS Inorder: ", end="")
	sample_binary_tree.print_Inorder()
	print(" ")
	print("DFS Preorder: ", end="")
	sample_binary_tree.print_Preorder()
	print(" ")
	print("DFS Postorder: ", end="")
	sample_binary_tree.print_Postorder()
	print(" ")	
	print("BFS: ", end="")
	sample_binary_tree.print_BFS()
	print(" ")