from tree import TreeNode

def findTarget(self, root: TreeNode, k: int) -> bool:
	if not root:
		return False
	stack = [root]
	dic = {}
	while stack:
		node = stack.pop()
		if node:
			if node.val in dic:
				return True
			else:
				dic[k-node.val] = 1
			stack.append(node.right)
			stack.append(node.left)
	return False